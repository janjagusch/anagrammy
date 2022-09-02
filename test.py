from anagrammy.corpus import download_corpus, read_corpus
from anagrammy.search import find_anagrams

# download_corpus()
corpus = read_corpus()
corpus["word_length"] = corpus.word.str.len()
corpus = corpus.sort_values("word_length", ascending=False).reset_index(drop=True)
words = "i n e e d m o r e s p a c e".split()
n_anagrams = 100

for anagram in find_anagrams(words, corpus, n_anagrams):
    print(anagram)
