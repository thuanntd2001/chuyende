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


# giu nguyen so luong tu trung chi bo stopword
def genQuery2(query):
    lstWordIndex = []
    word_tokens = word_tokenize(query)
    filtered_query = [w.upper().strip() for w in word_tokens if not w.lower() in stop_words]

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
            sl = lstDoc[int(doc)].count(term.lower())
            # print(lstDoc[int(doc)])
            # print("sl ", sl)
            result[index] = sl
            if sl == 0: print("co van de 0: ", sl)
        else:
            print("list Tong Doc ko day du")
    return result


def doFtdQuery(query, lstWordIndex, lstVocab):
    lstFtdQuery = []
    # print("term: ",term)
    #print(query)
    for term in lstWordIndex:
        #print(lstVocab[term].lower())
        sl = query.count(lstVocab[term].upper())
        lstFtdQuery.append(sl)

    return lstFtdQuery


def logarithmQuery(query, lstWordIndex, lstVocab):
    lstFtdQuery=doFtdQuery(query, lstWordIndex, lstVocab)
    lstLogarithmQuery = []
    for i in lstFtdQuery:
        #print("i= ",i)
        if i!=0:
            lstLogarithmQuery.append(logarithm(i))
    return lstLogarithmQuery


# tao matrix ftdt theo query
def doMatrixFtd(query, lstDoc, lstTermDoc, lstVocab):
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
        result = doFtd(lstVocab[lstWordIndex[j]], lstDocTerm, lstTongDoc, lstDoc)
        # print(result)

        for i in range(len(lstTongDoc)):
            matrix[i, j] = result[i]

    return lstTongDoc, lstWordIndex, matrix


def doMatrixWtIdf( lstWordIndex, matrix, lstTermDoc, N):
    # chua idf cua tu co index theo lstWordIndex
    lstIdf = []
    for i in lstWordIndex:
        lstIdf.append(idf(N, len(lstTermDoc[i].split())))
        # print(len(lstTermDoc[i].split()))
    # print(N)
    # print(lstIdf)
    h, c = matrix.shape
    matrixTfIdf = np.zeros([h, c], dtype=float)

    for i in range(h):
        for j in range(c):
            if matrix[i, j] != 0:
                matrixTfIdf[i, j] = logarithm(matrix[i, j]) * lstIdf[j]
    return matrixTfIdf

def calSimCosChuanHoaCosin(matrixTfIdf,lstSmartQuery):
    h, c = matrixTfIdf.shape
    lstResultSim=[]
    for i in range(h):
        docI=matrixTfIdf[i]
        lstResultSim.append(tichVoHuong(docI,lstSmartQuery))
    #print(lstResultSim)
    return lstResultSim

def sortKetQua(lstTongDoc,lstResultSim):
    lstTongDocSort=lstTongDoc.copy()
    n=len(lstResultSim)
    for i in range(n):
        for j in range(0, n - i - 1):

            if lstResultSim[j] < lstResultSim[j + 1]:
                lstResultSim[j], lstResultSim[j + 1] = lstResultSim[j + 1], lstResultSim[j]
                lstTongDocSort[j], lstTongDocSort[j + 1] = lstTongDocSort[j + 1], lstTongDocSort[j]
    return lstResultSim,lstTongDocSort


# DS DOC CHUA full TU KHOA (tra theo index) ["DOC1 DOC2","DOC1 DOC3"]
lstTermDoc = [""] * len(lstVocab)
f = open("save.txt", "r")
iterFile = iter(f)
strI = ""
strI2 = ""

#Doc File Chi Muc Nguoc De Tiet Kiem Thoi Gian tinh toan chi muc nguoc
while True:
    try:
        strI = next(iterFile).strip()
        # print(strI)
        strI2 = next(iterFile).strip()
        # print(strI2)
        # DS DOC CHUA full TU KHOA (tra theo index) ["DOC1 DOC2","DOC1 DOC3"]
        lstTermDoc[search(lstVocab, strI.upper())] = strI2

    except StopIteration as e:
        break
# print(lstDoc)
f.close()

# print(lstTermDoc)
q = 1
for q in range(1,len(lstQuery)):
    query=lstQuery[q]
    lstTongDoc, lstWordIndex, matrix = doMatrixFtd(query, lstDoc, lstTermDoc, lstVocab)
    # print(lstTongDoc)
    print("query: ",q)
    print("------------------------------------")
    print("TU KHOA: \n")

    for i in lstWordIndex: print(lstVocab[i])
    # print(matrix)


    matrixTfIdf = doMatrixWtIdf( lstWordIndex, matrix, lstTermDoc, len(lstDoc))
    lstSmartQuery=logarithmQuery(query, lstWordIndex, lstVocab)
    lstResultSim=calSimCosChuanHoaCosin(matrixTfIdf,lstSmartQuery)
    lstResultSim2,lstTongDocSort=sortKetQua(lstTongDoc,lstResultSim)
    print("------------------------------------")
    print("RANKING: ")
    print(lstTongDocSort)
    print("------------------------------------")
    print("GIA TRI TICH VO HUONG: ")
    print(lstResultSim2)
    print("//////////////////////////////////////////////////////////////////////////////////////")


