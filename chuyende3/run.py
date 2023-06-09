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


    return lstWordIndex








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


    matrix = np.zeros([len(lstTongDoc), len(lstWordIndex)], dtype=int)




# tao ra ma tran d trang 18 tai lieu
    for j in range(len(lstWordIndex)):
        # list cac doc chua term co chi so lstWordIndex[j]
        lstDocTerm = lstTermDoc[lstWordIndex[j]].split()
        # print("N= ",len(lstVocab))
        # print("n= ",len(lstDocTerm))


        for i in lstDocTerm:
            indexHang=search(lstTongDoc,i)
            matrix[indexHang, j] = 1

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
                matrixTfIdf[i, j] = matrix[i, j] * lstIdf[j]
    return matrixTfIdf



def ketQuaDauTien(matrixTfIdf):
    h, c = matrixTfIdf.shape
    lstResultSim=[]
    for i in range(h):
        docI=matrixTfIdf[i]
        tong = 0
        for t in docI:
            tong=tong+t
        lstResultSim.append(tong)
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



def tinhPiRi(lstTongDocSort,slV,lstTongDoc, lstWordIndex, lstTermDoc, lenLstDoc):
    vSet=lstTongDocSort[:slV]
    lstResultRi=[]
    lstResultPi=[]
    lstResultCi=[]
    for i in lstWordIndex:
        pi=0
        ri=0
        slVI=0

        lstDocTerm=lstTermDoc[i].split()
        ni=len(lstDocTerm)
        #print(lstDocTerm)
        for j in vSet:
            if search(lstDocTerm,j)!=-1:
                slVI+=1
        pi=(slVI+0.5)/(slV+1)
        ri=(ni-slVI+0.5)/(lenLstDoc-slV+1)
        lstResultPi.append(pi)
        lstResultRi.append(ri)
        ci=cI(pi,ri)
        lstResultCi.append(ci)

    print("vSet: ",vSet)





    return lstResultCi
def doMatrixRSV( lstResultCi, matrix):

    h, c = matrix.shape
    matrixRSV = np.zeros([h, c], dtype=float)

    for i in range(h):
        for j in range(c):
            if matrix[i, j] != 0:
                matrixRSV[i, j] = matrix[i, j] * lstResultCi[j]
    return matrixRSV

def compare2lst( lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] !=  lst2[i]: return False
    return True

if __name__ == "__main__":
    slV=20
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
    #for q in range(1,len(lstQuery)):
    for q in range(1,len(lstQuery)):

        query=lstQuery[q]
        lstTongDoc, lstWordIndex, matrix= doMatrixFtd(query, lstDoc, lstTermDoc, lstVocab)



        print("------------------------------------")
        print("query: ",q)
        print("TU KHOA: \n")
        "lan 1 tinh lstTongDoc sort theo idf"

        for i in lstWordIndex: print(lstVocab[i])
        # print(matrix)
        matrixTfIdf = doMatrixWtIdf(lstWordIndex, matrix, lstTermDoc, len(lstDoc))
        lstResult = ketQuaDauTien(matrixTfIdf)
        lstResult2, lstTongDocSort = sortKetQua(lstTongDoc, lstResult)

        print("//////////////////////////////////////////////////////////////////////////////////////")
        gioiHan=0
        gioiHanTren=10
        done=False
        while not done and gioiHan<gioiHanTren:
            "2 tro di tinh lstTongDoc sort theo RSV"
            gioiHan+=1
            print("lan lap so: ",gioiHan)
            oldVSet=lstTongDocSort[:slV]
            ci= tinhPiRi(lstTongDocSort,slV,lstTongDoc,lstWordIndex,lstTermDoc,len(lstDoc))
            RSVLstDoc=doMatrixRSV(ci,matrix)
            RSVLst=ketQuaDauTien(RSVLstDoc)
            #print(matrix)
            lstResult2,lstTongDocSort=sortKetQua(lstTongDoc,RSVLst)
            newVSet=lstTongDocSort[:slV]
            done=compare2lst(oldVSet,newVSet)

            print("RANKING: ")
            print(newVSet)
            print("------------------------------------")
        if gioiHan >= gioiHanTren:        
            print("vuot qua so lan lap")
        else:      
            print("Da hoi tu")

















