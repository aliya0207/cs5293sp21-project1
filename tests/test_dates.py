import project1
import spacy
from project1 import redactor
import nltk
import pytest




d = """Susie was born in Germany in April 1980. However, due to certain issues her family moved to Spain in 1990."""


def test_date():
    (data, list_dates, count) = redactor.sanitize_dates(d)
    assert count == 2
   
