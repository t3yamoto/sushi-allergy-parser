from src.sushi_allergy_parser import (
    __version__,
    KuraAllergyParser,
    SushiroAllergyParser,
)
import pandas as pd

EXPECTED_COLUMNS = [
    "name",
    "category",
    "egg",
    "wheat",
    "milk",
    "peanut",
    "buckwheat",
    "shrimp",
    "crab",
    "squid",
    "salmonRoe",
    "salmon",
    "mackerel",
    "beef",
    "chicken",
    "pork",
    "soybean",
    "orange",
    "apple",
    "gelatin",
    "walnut",
    "banana",
    "kiwi",
    "yamOrSweetPotato",
    "peach",
    "sesame",
    "abalone",
    "cashewNut",
    "matsutakeMushroom",
]


def test_version():
    assert __version__ == "0.1.1"


def test_sushiro():
    df = KuraAllergyParser().parse()
    assert isinstance(df, pd.DataFrame)

    for column in EXPECTED_COLUMNS:
        assert isinstance(df[column], pd.Series)


def test_kura():
    df = SushiroAllergyParser().parse()
    assert isinstance(df, pd.DataFrame)

    for column in EXPECTED_COLUMNS:
        assert isinstance(df[column], pd.Series)
