import numpy as np
from readValue import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bisect import bisect_left

stop_words = set(stopwords.words('english'))
lstVocab.sort()

matrix = np.zeros([len(lstDoc) + 1, len(lstVocab), ], dtype=int)


def search(alist, item):
    'Locate the leftmost value exactly equal to item'
    i = bisect_left(alist, item)
    if i != len(alist) and alist[i] == item:
        return i
    else:
        return -1


def genQuery(query):
    lstWord = np.zeros(len(lstVocab), dtype=int)
    word_tokens = word_tokenize(query)
    filtered_query = [w.upper() for w in word_tokens if not w.lower() in stop_words]
    for strI in filtered_query:
        j = search(lstVocab, strI)
        # print(j)
        if j != -1:
            lstWord[j] = 1
    return lstWord


def doQuery(matrix, lstWord):
    pass


# print(lstVocab)
for i in range(len(lstDoc)):
    doc = lstDoc[i]

    word_tokens = word_tokenize(doc)
    # converts the words in word_tokens to lower case and then checks whether
    # they are present in stop_words or not
    filtered_sentence = [w.upper() for w in word_tokens if not w.lower() in stop_words]
    # print(filtered_sentence)

    for strI in filtered_sentence:
        j = search(lstVocab, strI)
        # print(j)
        if j != -1:
            matrix[i, j] = 1
