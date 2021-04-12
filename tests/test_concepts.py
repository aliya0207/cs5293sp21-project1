import pytest
import nltk
import spacy
import project1
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from project1 import redactor

p= " Nowadays, it is very difficult to take care of a child. "

def test_concepts():
    (data, all_concepts, count) = redactor.sanitize_concepts (p,'kids')
    assert  count == 1
