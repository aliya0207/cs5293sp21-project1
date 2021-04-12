
import pytest
import nltk
import spacy
import project1
from project1 import redactor

s = "His mother died saving her son Harry Potter which ended up creating a shield and helped him survive against the villain. However, Tom Riddle still managed to survive but was very weak."


def test_names():
    data, list_names, count = redactor.sanitize_names(s)
    
    # there are 2 names in this file [ Harry Potter , James Potter]
    assert len(list_names) == 2
