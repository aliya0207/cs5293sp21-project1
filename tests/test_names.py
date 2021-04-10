
import pytest
import nltk
import spacy
import project1
from project1 import redactor

s = " Lily Potter died saving her son Harry Potter which ended up creating a shield and helped him survive against the villain. However, Tom Riddle still managed to survive but was very weak."


def test_names():
    data, list_names, count = redactor.redact_names (s)
    
    # there are 3 names in this file [Lily Potter , Harry Potter , James Potter]
    assert len(list_names) == 3
