from collections import Counter
from itertools import count
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict
from zipfile import ZipFile

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

_DATASET_ID = "rtatman/english-word-frequency"
_FILENAME = "unigram_freq.csv"
_PATH = Path(__file__).parent.resolve() / _FILENAME
_MIN_COUNT = 10**6


def _download_corpus(client: KaggleApi) -> pd.DataFrame:
    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        client.dataset_download_file(dataset=_DATASET_ID, file_name=_FILENAME, path=temp_dir)
        with ZipFile(temp_dir/ f"{_FILENAME}.zip") as zip_ref:
            zip_ref.extract(_FILENAME, temp_dir)
            return pd.read_csv(temp_dir / _FILENAME)


def _process_corpus(corpus: pd.DataFrame) -> pd.DataFrame:
    corpus = corpus[corpus["count"] > _MIN_COUNT].reset_index(drop=True)
    corpus = corpus[corpus.word.str.len() >= 4]
    return corpus


def _authenticated_client():
    client = KaggleApi()
    client.authenticate()
    return client


def download_corpus():
    client = _authenticated_client()
    corpus = _download_corpus(client)
    corpus = _process_corpus(corpus)
    corpus.to_csv(_PATH, index=False)


def read_corpus() -> pd.DataFrame:
    try:
        corpus = pd.read_csv(_PATH)
    except FileNotFoundError as error:
        raise FileNotFoundError("Corpus file not found. Please run `download_corpus` first.") from error
    corpus["word"] = corpus.word.astype("str")
    return corpus
