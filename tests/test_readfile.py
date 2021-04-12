from project1 import redactor
import nltk

files =  [['*.txt'], ['project1\\doc1.txt']]


def test_readfile():
    files_data = (redactor.Read_files(files))
    assert type(redactor.Read_files(files)) == str
    for i in range(len(files_data)):
        temp_file = files_data[i]
        assert (len(temp_file)) > 10
    return 0
