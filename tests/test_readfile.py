import pytest
import project1
from project1 import redactor
import nltk

files = 'project1/doc1.txt'


def test_readfile():
    files_data ,file_list  = (redactor.Read_files(files))
    assert type(files_data) == list
    assert type(file_list) == list
    for i in range(len(files_data)):
        temp_file = files_data[i]
        assert (len(temp_file)) > 10
    return 0
