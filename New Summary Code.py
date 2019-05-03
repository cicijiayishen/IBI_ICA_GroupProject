#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:35:36 2019

@author: Group 2
"""
import re

#To detect the validity of the DNA sequence given by the user
def detect_DNA(DNA):
    #Use regex to check if the sequence only contains A,T,G,C letter
    if re.match(r'[ATGC]+$',DNA):
        return True
    else:
        print('It is an invalid DNA sequence')
        #if invalid sequence, the main_menu option will show again
        main_menu()
        return    

def task1(DNA):
    A=0
    T=0
    C=0
    G=0
    for i in DNA:
        #To count the number of each base in a given sequence
        if i == "A":
            A += 1
        elif i == "T":
            T += 1
        elif i == "C":
            C += 1
        elif i == "G":
            G += 1
    #GC formula
    P = (G+C)/(len(DNA))*100
    print("The proportion of Guanine-Cytosine base pairs in the DNA sequence is", P, "%")
    return

def task2(DNA):
    Complementary=""
    for i in DNA:
        #remember the principle of DNA base pairing: A-T and C-G
        if i == 'A':
            Complementary += 'T'
        elif i=='T':
            Complementary += 'A'
        elif i=='G':
            Complementary += 'C'
        elif i=='C':
            Complementary += 'G'
    print(Complementary)
    #To reverse the sequence to make it antiparallel
    Complementary_sequence=Complementary[::-1]
    print('The complementary DNA sequence (5’ to 3’):', Complementary_sequence) 
    return

def task3(DNA):
    mRNA=""
    for i in DNA:
        #in RNA, no T, but U
        if i == 'A':
            mRNA += 'U'
        elif i=='T':
            mRNA +='A'
        elif i=='G':
            mRNA +='C'
        elif i=='C':
            mRNA +='G'
    print('The mRNA sequence is:', mRNA)
    return


def task4(mRNA): 
    #To detect the validity of the mRNA sequence given by the user     
    def detect(mRNA):
        #use regex to check if the sequence only contains A,U,G and C letter
        if re.match(r'[AUGC]+$',mRNA):
            return True
        else:
            print("it is an invalid mRNA sequence")
            main_menu()
        return
  
    #To check if the sequence contains start codon
    def start(mRNA):
        global start_index
        #Check if there is any AUG codon in the sequence
        if re.search('AUG',mRNA):
            #return the index position to the first occurrence of AUG 
           start_index = mRNA.index('AUG')
        else:
            print("error: no start codon found")
            main_menu
        return
            
    def stop(mRNA):
        print("error: no stop codon found")
        main_menu()
        return
        
    amino_acid=''
    sequence=''
    #amino acid dictionary. '' refers to stop codon
    AA = {'U':{'U':{'U':'F','C':'F','A':'L','G':'L'},
               'C':{'U':'S','C':'S','A':'S','G':'S'},
               'A':{'U':'Y','C':'Y','A':' ','G':' '},
               'G':{'U':'C','C':'C','A':' ','G':'W'}},
          'C':{'U':{'U':'L','C':'L','A':'L','G':'L'},
               'C':{'U':'P','C':'P','A':'P','G':'P'},
               'A':{'U':'H','C':'H','A':'Q','G':'Q'},
               'G':{'U':'R','C':'R','A':'R','G':'R'}},
          'A':{'U':{'U':'I','C':'I','A':'I','G':'M'},
               'C':{'U':'T','C':'T','A':'T','G':'T'},
               'A':{'U':'N','C':'N','A':'K','G':'K'},
               'G':{'U':'S','C':'S','A':'R','G':'R'}},
          'G':{'U':{'U':'V','C':'V','A':'V','G':'V'},
               'C':{'U':'A','C':'A','A':'A','G':'A'},
               'A':{'U':'D','C':'D','A':'E','G':'E'},
               'G':{'U':'G','C':'G','A':'G','G':'G'}}} 

    if detect (mRNA) == True:
        start (mRNA)
        #Use step size 3 to loop through the sequence and access 3 elements at the same time
        for i in range (start_index,len(mRNA),3):
            if i <= len(mRNA)-3:
                # 3 bases form a codon and its 1-letter-code will be retrieved from the dictionary
               amino_acid = AA[mRNA[i]][mRNA[i+1]][mRNA[i+2]]
               """if the codon encodes an amino acid(not a stop codon),
               then its 1-letter-code will be used to form a sequence"""
               if amino_acid != ' ' and i<len(mRNA)-3:
                  sequence += amino_acid
                #To check if the sequence contains stop codon
               elif amino_acid !=' ' and i == len(mRNA)-3:
                    stop(mRNA)
               else:
                   break
            else:
                stop(mRNA)
        print('The protein sequence is:',sequence)   

def task5():
    from collections import Counter
    filename=input('Input the file path of your sequence:')
    reference=input('Input the reference sequence:')
    n=int(input('Input the length of the start primer:'))
    m=int(input('Input the length of the end primer:'))
    t=int(input('Input the length of the tag:'))
    target=int(input('Input the length of target sequence:'))
    data=open(filename)
    list=[]
    for line in data.readlines():
        temp1=line.strip('\n')
        list.append(temp1)
    data.close()
    newlist=[]
    newlist.append(list[1])
    for i in range(1,len(list)):
        if list[i] not in newlist:
            newlist.append(list[i])
    print(newlist)            
    newnewlist=[]
    for j in range(0, len(newlist)):
        s=newlist[j][n:len(newlist[j])-m-t]
        newnewlist.append(s)
    print(newnewlist)
    abc=[]
    for i in range(0,len(reference)-target+1):
        for j in newnewlist:
            if j==reference[i:i+target]:
                abc.append(j)
    counter=Counter(abc)
    L=tuple(counter.keys())
    T=tuple(counter.values())
    for z in range(0,len(L)):
        print(L[z],counter[L[z]]/len(abc)*100 , "%")
    import numpy as np
    import matplotlib.pyplot as plt
    con = np.arange(len(L))
    means = (T)
    width = 0.8
    plt.bar(con,means,width, color = 'lightgrey')
    plt.xticks(con,(L))
    plt.ylabel('amount')
    plt.title('Affinity of different DNA domains')
    plt.show()
    return

def task6():
    print("We are Adele, Alana, Ashley, Cici and Pan Hobing,")
    print("first year Biomedical Informatics students at ZJU-UoE Institute.")
    print('Thank you for using our program!')
    return
    
#main menu where the users can choose which program they want to run
def main_menu():
    #The list of options 
    task = input('Please select the task you want to do:\n 1. GC content claculator\n 2. Complementary DNA strand calculator\n 3. DNA to mRNA convertor (transcription)\n 4. mRNA to protein (translation)\n 5. effective motif analysis\n 6. about us\n') 
    if task == '1':   
        DNA=input("Please input the DNA sequence:\n")
        if detect_DNA(DNA) == True:
            task1(DNA)
            main_menu()
    elif task == '2':
        DNA=input("Please input the DNA sequence (5’ to 3’):\n")
        if detect_DNA(DNA) == True:
            task2(DNA)
            main_menu()
    elif task == '3':
        DNA=input("Please input the DNA sequence (5’ to 3’):\n")
        if detect_DNA(DNA) == True:
            task3(DNA)
            main_menu()
    elif task == '4':
        mRNA = input("Please input the mRNA sequence:\n")
        task4(mRNA)
        main_menu()
    elif task == '5':
        task5()
        main_menu()
    elif task == '6':
        task6()
        exit
    return

main_menu()