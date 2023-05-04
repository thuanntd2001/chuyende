"""
Nguyen Tran Duc Thuan
MSSV: N19DCN203
Vu Cao Ky
MSSV: N19DCN048
Vu Trung An
MSSV: N19DCN003
"""

import math


#               TERM FREQUENCY
def natural(tf):
    return tf


def logarithm(tf):
    return (1 + math.log10(tf))


# list_tf_in_document là list chứa tần suất xuất hiện của các từ trong 1 tài liệu
def augmented(tf, list_tf_in_document):
    return (0.5 + (0.5 * tf) / (max(list_tf_in_document)))


def booleann(tf):
    if tf > 0:
        return 1
    else:
        return 0


#               DOCUMENT FREQUENCY

def no(N, dft):
    return 1


# N  : là số tài liệu
# dft: là số tài liệu chứa từ t
def idf(N, dft):
    return math.log10((N  + 0.5)/ (dft + 0.5))


def p(N, dft):
    return max(0, math.log10((N - dft) / dft))  


#               Normalization

def none():
    return 1


def cosine(lstWeight):
    return (1 / (math.sqrt(sum(t ^ 2 for t in lstWeight))))


def doDaiVector(vtA):
    t2 = 0
    for i in vtA:
        t2 += i * i

    return math.sqrt(t2)


def tichVoHuong(vtA, vtB):
    tong = 0
    for i in range(len(vtA)):
        tong+=vtA[i] * vtB[i]
    return tong



#              Ci
def cI(pi, ri):
    return  math.log10(pi*(1 - ri) / ri*(1-pi))
