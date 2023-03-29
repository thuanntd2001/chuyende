import numpy as np
from readValue import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bisect import bisect_left

stop_words = set(stopwords.words('english'))

lstVocab.sort()
# print("lstvobcab sort: ", lstVocab)
matrix = np.zeros([len(lstVocab), len(lstDoc)], dtype=int)


def search(alist, item):
    'Locate the leftmost value exactly equal to item'
    i = bisect_left(alist, item)
    if i != len(alist) and alist[i] == item:
        return i
    else:
        return -1


def genQuery(query):
    lstWordIndex = []
    word_tokens = word_tokenize(query)
    filtered_query = [w.upper() for w in word_tokens if not w.lower() in stop_words]


    for strI in filtered_query:
        j = search(lstVocab, strI)
        if j != -1:
            lstWordIndex.append(j)

    # print(lstWordIndex)
    return lstWordIndex


def doAnd(lst1, lst2):
    lstkq = []
    for i in range(len(lst1)):
        lstkq.append(lst1[i] * lst2[i])
    return lstkq


def doQuery(matrix, lstWordIndex):
    lstKq = []
    matrixWordBool = []
    if len(lstWordIndex) >= 1:
        matrixWordBool = [1] * len(matrix[0])
    for i in range(len(lstWordIndex)):
        matrixWordBool = doAnd(matrixWordBool, matrix[lstWordIndex[i]])
    # print("ma tran tim kiem: ", matrixWordBool)
    for i in range(len(matrixWordBool)):
        if matrixWordBool[i] == 1:
            # print(i)
            lstKq.append(i)
    return lstKq










for i in range(len(lstDoc)):

    doc = lstDoc[i]

    word_tokens = word_tokenize(doc)
    # converts the words in word_tokens to lower case and then checks whether
    # they are present in stop_words or not
    filtered_sentence = [w.upper() for w in word_tokens if not w.lower() in stop_words]
    # print("list tu: ", filtered_sentence)

    for strI in filtered_sentence:
        j = search(lstVocab, strI)
        if j != -1:
            matrix[j][i] = 1


# print(matrix)
lstKqQuery = []
for i in range(len(lstQuery)):
    lstKqQuery.append(doQuery(matrix, list(genQuery(lstQuery[i]))))


for i in range(len(lstQuery)):
    print("query ",i,": ",lstKqQuery[i])
