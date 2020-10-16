# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:44:43 2020

@author: mathi
"""



#Remove UKNOW label trial

def Duplicate_Text2List(PATH): 
    file = open(PATH)
    file = file.read()
    ligne =[]
    label=[]
    texte_label =[]
    texte = []
    file =file.split('\n')
    for i in range (0,len(file)-1,1):
        file[i] = file[i].split(',')
        ligne =  file[i][0]
        label = file[i][1]
        texte_label.append(label)
        texte.append(ligne)
    return texte, texte_label
    file.close()

def WritingFileSentence_non_duplicateLines(file_name, LIST, LABEL_LIST):
    sentence=[]
    List_sentence = (sentence)
    f= open(file_name,"w+")
    #Middle_CONTENT
    for j in range(0, len(LIST), 1):
        sentence=LIST[j]
        List_sentence.append(sentence)
    for m in range(0,len(LIST)-2,1):
        f.write(List_sentence[m]+' ')
        f.write(','+LABEL_LIST[m])
        f.write('\n') 
    return f.close()


def removeUNK(Input_file, Output_file):
    Pos_0=[]
    LIST, LABEL_LIST = Duplicate_Text2List(Input_file)
    print(LABEL_LIST)
    print(len(LABEL_LIST))
    LEN = len(LABEL_LIST)
    print(LEN)
    for i in reversed(range (1, LEN-1, 1)):
        if LABEL_LIST[i] == "0" :
            Pos_0.append(i)
            unk = LABEL_LIST.pop(i)
            text_unk = LIST.pop(i)
            print("LABEL", len(LABEL_LIST))
            print(unk)
            print(i)
    WritingFileSentence_non_duplicateLines(Output_file, LIST, LABEL_LIST)
    return LABEL_LIST


print("START")
#proportion

# removeUNK('removed.txt', 'removed_processed_1.txt')
# removeUNK('removed_processed_1.txt', 'removed_processed_2.txt')
# removeUNK('removed_processed_2.txt', 'removed_processed_3.txt')
removeUNK('sentence_duplicated_doc_text.txt', 'removed_duplicated_0.txt')


print("HAPPY END")    
            
        