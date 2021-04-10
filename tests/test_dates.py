import project1
import spacy
from project1 import redactor
import nltk
import pytest




d = """ Born and raised in central Argentina, Messi relocated to Spain to join Barcelona at age 13, for whom he made his competitive debut aged 17 in October 2004. He established himself as an integral player for the club within the next three years, and in his first uninterrupted season in 2008"""


def test_date():
    (data, list_dates, count) = redactor.sanitize_dates(d)
    assert c ==2
    assert ['October 2004' , '2008'] == list_dates
