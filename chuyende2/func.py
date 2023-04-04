import math

#               TERM FREQUENCY
def natural(tf):
    return tf

def logarithm(tf):
    return round(1 + math.log10(tf), 2)

#list_tf_in_document là list chứa tần suất xuất hiện của các từ trong 1 tài liệu
def augmented(tf, list_tf_in_document):
    return 0.5 + (0.5*tf)/(max(list_tf_in_document))

def booleann(tf):
    if tf > 0:
        return 1
    else: return 0

#               DOCUMENT FREQUENCY

def no():
    return 1

# N  : là số tài liệu
# dft: là số tài liệu chứa từ t
def t(N, dft):
    return math.log10(N, dft)

def p(N, dft):
    return max(0, math.log10((N-dft)/dft))
#               Normalization

def none():
    return 1

def cosine(lstWeight):
    return 1/(sqrt(sum(t^2 for t in lstWeight)))


