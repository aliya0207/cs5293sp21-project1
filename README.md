# cs5293sp21-project1
Project 1:

## ALIYA SHAIKH EMAIL: aliyashaikh02@ou.edu
## The Redactor
### Introduction
Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.
### CODE STRUCTURE:

```
cs5293p20-project1/
├── COLLABORATORS
├── LICENSE
├── README
├── requirements.txt
├── project1
│   ├── __init__.py
│   └── main.py
│   └── ... 
├── docs/
├── setup.cfg
├── setup.py
└── tests/
    ├── test_names.py
    └── test_genders.py
    └── ... 
```    
### PACKAGES REQUIRED:
1. spacy
2. nltk
3. os
4. glob
5. argparse
6. re
7. wordnet

### Function Description:

In this project there are various functions that are used to read a .txt file and then redact sensitive information such as names, date, phone number, and a concept = "kids" which will redact all sentences that consist of words similar to the concept given.

#### def Read_files(text_files):
This function reads the .txt files in the directory.

#### def sanitize_names(data):

This function makes use of SPACY to redact the names from the text file. We load the (“en_core_web_sm”) language model to use the PERSONS label to detect the names of persons from the text file and then use the block character i.e '\u2588' to redact the name and replace with the block character. Also, the list and count of redacted names is stored for the statistics.

#### def sanitize_dates(data):

This function makes use of SPACY to redact the names from the text file. We load the (“en_core_web_sm”) language model to use the DATE label to detect the dates from the text file and then use the block character i.e '\u2588' to redact the dates and replace with the block character. Also, the list and count of redacted dates is stored for the statistics.

#### def sanitize_phone(data):

Phone numbers are sensitive information and hence need to be redacted. I have used RE packages to find phone number style and redact them and count them for statistics.

#### def sanitize_concepts(data, key):

The concept in this case is "kids". Which is passed through key. The nltk.corpus import wordnet package and synset helps us in the getting the words that are similar to the given concept. Once, the word in the list appears in any sentence, the whole sentence gets redacted and is replaced by a block character.
The sentences to be redacted are also stored in a list along with the count for statistics.

#### def update_statlist(stats_list):

This function is used to print the count of each function above.

#### def final_output(text_files,data,output_path):

This function is used for output. As given in the project we need to store all the redacted file as written to text files Each file will have the same name as the original file with the extension .redacted appended to the file name. 

### Check the project result:
By running the following command and the appropriate paths, we can see the output.
```
pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
 ```
 
 ### TESTS:
 
 ## 1. test names:
 For this test, we call the sanitize_names function in redactor.py.
 Here, to test, I have given the text and then by calling to the function in redactor.py we will get the names and the number of names to be redacted. 
 
 ## 2. test dates:
 For this test, we call the sanitize_dates function in redactor.py.
 Here, to test, I have given the text and then by calling to the function in redactor.py we will get the dates and the number of dates to be redacted. 
 
 ## 3. test phone number:
 For this test, we call the sanitize_phones function in redactor.py.
 Here, to test, I have given the text and then by calling to the function in redactor.py we will get the phone numbers and the number of phone numbers to be redacted. 
 
 ## 4. test concept:
 For this test, we call the sanitize_concept function in redactor.py.
 Here, to test, I have given the text and then by calling to the function in redactor.py we will get the number of sentences to be redacted. 
                    
 ## 5. test input:
 For this test, we call the Read_files function in redactor.py.
 Here, to test, I have given the path and then by calling to the function in redactor.py we check if the data matches the datatype we have given or not.
                    
