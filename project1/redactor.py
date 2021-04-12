import os
import spacy
import glob
import re
import nltk
import argparse
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize

stats_list=[]
def Read_files(text_files):
    # print(text_files)
    data = []
    #files = nltk.flatten(text_files)
    #print(files)
    #for i in range(len(files)):
    #print(os.getcwd())
    filenames =[]
    for filename in glob.glob(os.path.join(os.getcwd(),text_files)):
        #print(filename)
        filenames.append(filename.split('/')[-1])
        print(filenames)
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            data1 = f.read()
            data.append(data1)

        #if(filename.endswith(text_files)!= -1):
         #   print(filename)
          #  with open(os.path.join(os.getcwd()+"/"+output_path, filename), "r") as f:
           #     data1 = f.read()
            #    data.append(data1)

    # print(type(data))
    #print(len(data),data)
    return data, filenames

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
        #print(all_dates)
        dates_list.append(all_dates)
        data=data.replace(str(all_dates),'\u2588')
    selection= "redacted_dates"
    redacted_stats(selection,len(dates_list))
    print(list_dates)
    return data,list_dates,count
#sanitize_dates(data)

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
        #print(found_names)
        names_list.append(found_names)
        data=data.replace(str(found_names),'\u2588')
    selection= "redacted_names"
    redacted_stats(selection,len(names_list))
    print(list_names)
    return data,list_names,count
#sanitize_names(data)


def sanitize_phones (data):
    count = 0
    numbers = list()
    phone_number= re.findall (r'(?:\s+(?:\+|00)?[1-9]\d{,2}(?:\s+|\-|\.)?)?\(?\d{2,4}\)?(?:\s|\-|\.)+(?:(?:\d{3,4}(?:\s|\-|\.)+\d{4})|[a-zA-Z0-9]{3}\-[a-zA-Z0-9]{4})', data)
    numbers += phone_number
    count = count + len(phone_number)
    phone_number.sort (key =len, reverse=True)
    for i in phone_number:
        data = data.replace (i,'\u2588')
   # print(data)
    selection= "redacted_phones"
    redacted_stats(selection,count)
    print(phone_number)
    return data,phone_number,count
#sanitize_phones(data)


def sanitize_concepts (data, key):
    #key="kids"
    concepts = []
    concepts.append(key)
    sent_list=[]
    synset= wordnet.synsets(key)
    for concept in synset:
        lemmas1 = concept.lemma_names()
        for lemma in lemmas1:
            if len(lemma)>1:
                concepts.append(lemma)
                
        hypl= concept.hypernyms()
        for i in hypl:
            x = i.lemma_names()
            for lemma in x:
                if len(lemma)>1:
                    concepts.append(lemma)
         
        hypol = concept.hyponyms()
        for i in hypol:
            x = i.lemma_names()
            for lemma in x:
                if len(lemma)>1:
                    concepts.append(lemma)
    #print(concepts)
    concepts = set(concepts)
    #print(concepts)
    concepts = concepts & set(nltk.word_tokenize(data))
    print (concepts)
    sentences = nltk.sent_tokenize(data)
    count = 0
    print("concept")
    data2 = ""
    print(data)
    print("################")
    all_concepts = list()
    #for concept in concepts:
        #print(concept)
    # count += len(re.findall(concept, data))

    for i in range(len(sentences)):
        for concept in concepts:
        #print(sentences[i])
            if sentences[i].lower().find(concept) != -1:
                count+=1
                #print("True")
                all_concepts.append (sentences[i])
                #print (sentences[i])
                sentences[i] = '\u2588'
                sent_list.append(all_concepts)
                break
        data2 =data2 + sentences[i]
   # data = ''
    #print(concepts)
    #print(sentences)
    #for sent in sentences:
     #   data +=  sent
    print("################")
    print(data2)
    selection= "redacted_concept"
    redacted_stats(selection,count)
    #print(data)
    return data2,all_concepts,count
#redact_concepts (data, key)

#print(len(stats_list), stats_list)


def redacted_stats(redacted_selection= 'none', count=0):
    if redacted_selection =='redacted_names':
        a1 = "The count of " + redacted_selection + " is : " + str(count)
        stats_list.append(a1)
        # print(stats_list)
    elif redacted_selection == 'redacted_dates':
        a1 = "The count of " + redacted_selection + " is : " + str(count)
        stats_list.append(a1)
    elif redacted_selection == 'redacted_phones':
        a1 = "The count of " + redacted_selection + " is : " + str(count)
        stats_list.append(a1)
    elif redacted_selection == 'redacted_concept':
        a1 = "The count of " + redacted_selection + " is : " + str(count)
        stats_list.append(a1)
    # print(len(stats_list))
    return stats_list

def final_output(text_files,data,output_path):
    # print((output_path))
    file_names =[]
    #all_files = nltk.flatten(text_files)
    
    #for filename in glob.glob(os.path.join(os.getcwd(),text_files)):
        #if text_files
    folder = os.getcwd() + '/'+output_path
   
    new_file = text_files.replace(".txt", ".redacted.txt")
    isFolder = os.path.isdir(folder)
    if isFolder== False:
        os.makedirs(os.path.dirname(folder))
    with open( os.path.join(folder, new_file), "w+") as f:
        #print(data)
        #strs = data.split("\n")
        #print(strs)
        data1 = f.write(data)
            #print(strdat)
        #with open(os.path.join(os.getcwd(), filename), "r") as f:
            #data1 = f.read()
            #data.append(data1)   
        #return len(file_names)


def update_statlist(stats_list=stats_list):

    path = ('stderr.txt')
    # print(os.path.join(path1,path2))
    file = open(path, "w+", encoding="utf-8")
    for i in range(len(stats_list)):
        file.write(stats_list[i])
        file.write("\n")

    file.close()
    # print(stats_list)
    return stats_list

if __name__== '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=str, required=True, help="Files to be redacted.")
    
    parser.add_argument("--names", help="Redact names", action='store_true')
    
    parser.add_argument("--dates", help="Redact dates", action='store_true')
    
    parser.add_argument("--phones",help="Redact phones", action='store_true')
    
    parser.add_argument("--stats", help="Statistics of redacted types", action='store_true')
    
    parser.add_argument("--concept", type=str, required=False, help="to redact the given concept words")
    
    parser.add_argument("--output", type=str, required=True, help="Redacted Output Files")
    

    args, un = parser.parse_known_args()
    #print(args.input)
    temp, filenames_1 =Read_files(args.input)
    str1 = ""
    count = 0
    for i in temp:
        str1 = i
        if (args.names):
            str1, list_names, count_names  = sanitize_names(str1)
        
        if (args.phones):
            str1, list_phones, count_phones  = sanitize_phones(str1)
        if (args.dates):
            str1, list_dates, count_dates  = sanitize_dates(str1)
        if (args.concept):
            str1, list_concept, count_concept = sanitize_concepts(str1, args.concept)
        if (args.output):
            count_files = final_output(filenames_1[count], str1, args.output)
        count = count+1
    if (args.stats):
        update_statlist()

