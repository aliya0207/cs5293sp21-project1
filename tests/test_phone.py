import pytest
import spacy
import nltk
import re
import project1
from project1 import redactor

t= "You can reach me at 123-678-2234. If not available, then please leave a voice message at 507-113-2567"

def test_phones():
    (data, phone_number,count) = redactor.sanitize_phones(t)
    print(phone_number)
    assert  count == 2
    assert phone_number == ['123-678-2234', '507-113-2567']
