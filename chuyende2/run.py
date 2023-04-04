"""
Nguyen Tran Duc Thuan
MSSV: N19DCN203
Vu Cao Ky
MSSV: N19DCN048
Vu Trung An
MSSV: N19DCN003
"""

import numpy as np
from readValue import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bisect import bisect_left
import pandas as pd
from func import *

stop_words = set(stopwords.words('english'))

lstVocab.sort()

np.set_printoptions(threshold=np.inf)
def search(alist, item):
    'Locate the leftmost value exactly equal to item'
    i = bisect_left(alist, item)
    if i != len(alist) and alist[i] == item:
        return i
    else:
        return -1


# tach str query thanh list index term bo stop word
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


# tra ve list result co so item bang voi lstTongDoc voi moi item la so luong cua tu vung trong doc o index tuong ung voi TongDoc
def doFtd(term, lstDocTerm, lstTongDoc, lstDoc):
    result = [0] * len(lstTongDoc)
    # print("term: ",term)
    for doc in lstDocTerm:
        # print(doc)
        index = search(lstTongDoc, doc)
        if index != -1:
            sl=lstDoc[int(doc)].count(term.lower())
            # print(lstDoc[int(doc)])
            # print("sl ", sl)
            result[index] = sl
            if sl==0 : print("co van de 0: ",sl)
        else:
            print("list Tong Doc ko day du")
    return result


# tao matrix ftdt theo query
def doMatrix(query, lstDoc, lstTermDoc, lstVocab):
    # list tat ca cac doc chua tu trong query
    lstTongDoc = []

    # lst tat ca chi so cac tu trong query bo stop word
    lstWordIndex = genQuery(query)

    # Cap nhat lstTongDoc
    for indexTerm in lstWordIndex:
        # list cac doc chua term co chi so indexTerm
        lstDocTerm = lstTermDoc[indexTerm].split()

        lstTongDoc = [*lstTongDoc, *lstDocTerm]

    # Set tat ca cac doc chua tu trong query (ko trung)
    lstTongDoc = list(set(lstTongDoc))

    # Sx  lstTongDoc de tim kiem nhi phan
    lstTongDoc.sort()

    # Sx lstWordIndeX de cho dep :)
    # lstWordIndex.sort()

    matrix = np.zeros([len(lstTongDoc), len(lstWordIndex)], dtype=int)

    for j in range(len(lstWordIndex)):
        # list cac doc chua term co chi so lstWordIndex[j]
        lstDocTerm = lstTermDoc[lstWordIndex[j]].split()
        # print(lstDocTerm)
        result = doFtd(lstVocab[lstWordIndex[j]], lstDocTerm,lstTongDoc, lstDoc)
        # print(result)

        for i in range(len(lstTongDoc)):
            matrix[i, j] = result[i]

    return lstTongDoc, lstWordIndex, matrix


# DS DOC CHUA full TU KHOA (tra theo index) ["DOC1 DOC2","DOC1 DOC3"]
lstTermDoc = [""] * len(lstVocab)
f = open("save.txt", "r")
iterFile = iter(f)
strI = ""
strI2 = ""

while True:
    try:
        strI = next(iterFile).strip()
        # print(strI)
        strI2 = next(iterFile).strip()
        # print(strI2)
        # DS DOC CHUA full TU KHOA (tra theo index) ["DOC1 DOC2","DOC1 DOC3"]
        lstTermDoc[search(lstVocab, strI.upper())] = strI2

    except StopIteration as e:
        print( "Stop iter")
        break
# print(lstDoc)
f.close()

# print(lstTermDoc)

lstTongDoc, lstWordIndex, matrix = doMatrix(lstQuery[3], lstDoc, lstTermDoc, lstVocab)
print(lstTongDoc)
for i in lstWordIndex: print(lstVocab[i])
print(matrix)


# lstWordIndex=genQuery(lstQuery[1])
# print(lstWordIndex)
# for i in lstWordIndex:
#     print(lstVocab[i])