from collections import Counter
from itertools import islice
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def find_anagrams(words: List[str], corpus: pd.DataFrame, n_anagrams: Optional[int] = 1):
    words = Counter("".join(words))
    corpus = {word: Counter(word) for word in corpus.word}
    result = _search(words, corpus, [], set())
    for anagram in islice(result, n_anagrams):
        yield anagram


def _search(words: Counter, corpus: Dict[str, Counter], result: Dict[str, int], previous_results: Set[Tuple]) -> List[str]:
    if all(v == 0 for v in words.values()):
        yield result
    for w, c in corpus.items():
        new_words = Counter(words)
        new_words.subtract(c)
        if all(v >= 0 for v in new_words.values()):
            new_result = dict(result)
            new_result[w] = new_result.get(w, 0) + 1
            new_result_t = tuple(new_result.items())
            if new_result_t in previous_results:
                continue
            previous_results.add(new_result_t)
            for res in _search(new_words, corpus, new_result, previous_results):
                yield res
