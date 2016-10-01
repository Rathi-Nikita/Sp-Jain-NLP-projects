#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:59:09 2016

@author: nikitarathi
"""
###import modules
import pandas as pd
import numpy as np
import nltk
#from nltk.book import *
from nltk.tokenize import sent_tokenize,word_tokenize
##read file
file=open("Dipankar.txt").read()
##file data in to clean tokens                                 
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
clean_token=tokenizer.tokenize(file)

###frquency for each tokens
freq = nltk.FreqDist(clean_token)
freq
###sort the frequency with descending order
sort=sorted(freq.items(),key=lambda x:x[1],reverse=True)
sort[1:10]
###function to input no of words to be printed with frequency
n=input("enter the no of high frequency words to be printed")
output_file=open("output file.txt","w")
def no_of_words(n):
    words=sort[1:n+1]
    for k in range(len(words)):
        word=str(words[k]).lstrip("(").rstrip(")")
        output_file.write(word + "\n")
    output_file.close()
            


 
