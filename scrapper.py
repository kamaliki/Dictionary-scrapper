# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:17:23 2022

@author: kamaliki
"""
import re
import requests
import operator
from bs4 import BeautifulSoup
from collections import Counter

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="lxml")
    for x in soup.findAll('p'):
        content = x.text
        #print(content)
        words = content.lower().split()
        for i in words:
            #print(i)
            word_list.append(i)
            #print(type(word_list))
            pass
        clean_up_list(word_list)
        pass
    pass

def clean_up_list(word_list):
    clean_word_list =[]
    for word in word_list:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
            if len(word) > 1:
                #print(word)
                clean_word_list.append(word)
            pass
        pass
    create_dictionary(clean_word_list)
    pass


"""
def clean_up_string(str(word_list):

    # keep only vocabularies

    pattern = re.compile(r'[a-zA-Z]+')

    match = pattern.findall(word_list)

    return [word.lower() for word in match]
"""

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        pass
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        #print("% s: % s" % (key,value))
        
        c = Counter(word_count)
        top = c.most_common(10)
        print(top)
        pass
    pass
start('https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer?ft_source=LinkedIn_1000080706&ft_medium=Job%20Boards_1000074720')