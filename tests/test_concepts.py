import pytest
import nltk
import spacy
import project1
from project1 import redactor

p= " Nowadays, it is very difficult to take care of babies. And difficult to pay attention to them. Youngsters are always using their phones. "

def test_concepts():
    (data, all_concepts, count) = redactor.sanitize_concepts (p, ['kids'])
    assert  count == 2
