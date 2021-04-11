import os
import spacy
import glob
import re
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize

stats_list=[]
def Read_files(text_files):
    # print(text_files)
    data = []
    files = nltk.flatten(text_files)

    for i in range(len(files)):
        # print(files[i])
        text_files1 = glob.glob(files[i])
        # print(text_files1)
        for j in range(len(text_files1)):
            # print(text_files1[j])
            data1 = open(text_files1[j]).read()
            # print(data1)
            data.append(data1)
    # print(type(data))
    print(len(data),data)
    return data

nlp = spacy.load('en_core_web_sm')
#docx1 = nlp(data)

#for ent in docx1.ents:
#    print(ent.text,ent.label_)

def sanitize_dates(data):
    docx = nlp(data)
    dates_list=[]
    list_dates=[]
    for ent in docx.ents:
        if ent.label_ == 'DATE':
            list_dates.append(ent)
    
    count=0
    for all_dates in list_dates:
        count +=len(re.findall(str(all_dates), data))
        print(all_dates)
        dates_list.append(all_dates)
        data=data.replace(str(all_dates),'\u2588')
    selection= "redacted_dates"
    redacted_stats(selection,len(dates_list))
    return data,list_dates,count
sanitize_dates(data)

def sanitize_names(data):
    docx = nlp(data)
    redacted_sentences = []
    list_names=[]
    names_list=[]
    for ent in docx.ents:
        if ent.label_ == 'PERSON':
            list_names.append(ent)
    
    count=0
    for found_names in list_names:
        count +=len(re.findall(str(found_names), data))
        print(found_names)
        names_list.append(found_names)
        data=data.replace(str(found_names),'\u2588')
    selection= "redacted_names"
    redacted_stats(selection,len(names_list))
    return data,list_names,count
sanitize_names(data)


def sanitize_phones (data):
    count = 0
    numbers = list()
    phone_number= re.findall (r'(?:\s+(?:\+|00)?[1-9]\d{,2}(?:\s+|\-|\.)?)?\(?\d{2,4}\)?(?:\s|\-|\.)+(?:(?:\d{3,4}(?:\s|\-|\.)+\d{4})|[a-zA-Z0-9]{3}\-[a-zA-Z0-9]{4})', data)
    numbers += phone_number
    count = count + len(phone_number)
    phone_number.sort (key =len, reverse=True)
    for i in phone_number:
        data = data.replace (i,'\u2588')
    selection= "redacted_phones"
    redacted_stats(selection,count)
    return data,phone_number,count
sanitize_phones(data)


def sanitize_concepts (data, key):
    #key="kids"
    concepts = list(key)
    sent_list=[]
    synset= wordnet.synsets(key)
    for concept in synset:
        lemmas1 = concept.lemma_names()
        for lemma in lemmas1:
            concepts.append(lemma)
                
        hypl= concept.hypernyms()
        for i in hypl:
            x = i.lemma_names()
            for lemma in x:
                concepts.append(lemma)
         
        hypol = concept.hyponyms()
        for i in hypol:
            x = i.lemma_names()
            for lemma in x:
                concepts.append(lemma)
        
    concepts = set(concepts)
    concepts = concepts & set(nltk.word_tokenize(data))
    print (concepts)
    sentences = nltk.sent_tokenize(data)
    count = 0
    all_concepts = list()
    for concept in concepts:
        count += len(re.findall(concept, data))
        for i in range(len(sentences)):
            if sentences[i].lower().find(concept) != -1:
                all_concepts.append (sentences[i])
                print (sentences[i])
                sentences[i] = '\u2588'
                sent_list.append(all_concepts)
    data = ''
    for sent in sentences:
        data = data + sent
    selection= "redacted_concept"
    redacted_stats(selection,count)
    return data,all_concepts,count
redact_concepts (data, key)

print(len(stats_list), stats_list)


def redacted_stats(redacted_selection= 'none', count=0):
    if redacted_selection =='redacted_names':
        a1 = "The count of " + redacted_type + " is : " + str(count)
        stats_list.append(a1)
        # print(stats_list)
    elif redacted_selection == 'redacted_dates':
        a1 = "The count of " + redacted_type + " is : " + str(count)
        stats_list.append(a1)
    elif redacted_selection == 'redacted_phones':
        a1 = "The count of " + redacted_type + " is : " + str(count)
        stats_list.append(a1)
    elif redacted_selection == 'redacted_concept':
        a1 = "The count of " + redacted_type + " is : " + str(count)
        stats_list.append(a1)
    # print(len(stats_list))
    return stats_list

def final_output(text_files,data,output_path):
    # print((output_path))
    file_names =[]
    all_files = nltk.flatten(text_files)
    for i in range(len(all_files)):
        text_files1 = glob.glob(all_files[i])
        # print(text_files1)
        for j in range(len(text_files1)):
            # print(type(text_files1[j]))
            if '.txt' in  text_files1[j]:
                text_files1[j] = text_files1[j].replace(".txt", ".redacted.txt")
            if '.md' in text_files1[j]:
                text_files1[j] = text_files1[j].replace(".md", ".redacted.txt")
            if '\\' in text_files1[j]:
                text_files1[j]= text_files1[j].split("\\")
                text_files1[j] = text_files1[j][1]
                # print(text_files1[j])
            file_names.append(text_files1[j])

    for i in range(len(data)):
        for j in range(len(file_names)):
            if i==j:
                file_data =data[i]
                # print((file_names[i]))
                path1 = (os.getcwd())
                # print(output_path+file_names[j])
                path2 = (output_path+'/'+file_names[j])
                result_file = open(os.path.join(path1,path2), "w" ,encoding="utf-8")
                # print(os.path.join(path1,path2))
                result_file.write(file_data)
                result_file.close()
    return len(file_names)


def update_statlist(stats_list=stats_list):

    path = ('stderr/stderr.txt')
    # print(os.path.join(path1,path2))
    file = open(path, "w", encoding="utf-8")
    for i in range(len(stats_list)):
        file.write(stats_list[i])
        file.write("\n")
    file.close()
    # print(stats_list)
    return stats_list
