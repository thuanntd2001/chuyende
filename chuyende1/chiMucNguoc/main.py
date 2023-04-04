
"""
Nguyen Tran Duc Thuan
MSSV: N19DCN203
Vu Cao Ky
MSSV: N19DCN048
Vu Trung An
MSSV: N19DCN003
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def filterStopWords(a):
    stop_words = set(stopwords.words('english'))

    filtered_sentence=[]
    for w in a:
        if w not in stop_words:
            filtered_sentence.append(w)
  
    return filtered_sentence

def trans(a):
    b = []
    for strin in a:
        c = filterStopWords(word_tokenize(strin))
        b.append(c)
    return b


def search(vocab, doc):
    vocab.sort()
    le = len(vocab) - 1
    res = {}
    i = 0
    for x in doc:
        k = list(set(word_tokenize(x)))
        for z in k:
            if bin_search(z, vocab, 0, le) != 0:    
                if z not in res: res[z] = []
                res[z].append(i)
        i = i + 1
    return res

def bin_search(x, a, left_idx, right_idx):
    if left_idx > right_idx:
        return 0
    mid_idx = left_idx + (right_idx - left_idx) // 2
    mid = a[mid_idx]
    if x == mid:
        return 1
    elif x < mid:
        return bin_search(x, a, left_idx, mid_idx - 1)
    else:
        return bin_search(x, a, mid_idx + 1, right_idx)

def intersect(a, b):
    a.sort()
    b.sort()
    res = []
    x, y = 0,0
    while x < len(a) and y < len(b):
        if a[x] == b[y]:
            res.append(a[x])
            x = x+1
            y= y+1
        elif a[x] < b[y]:
            x = x+1
        else:
            y = y+1
    return res

def intersectWithSkips(a, b):
    a.sort()
    b.sort()
    res = []
    x, y = 0,0
    while x < len(a) and y < len(b):
        if a[x] == b[y]:
            res.append(a[x])
            x = x+1
            y= y+1
        elif a[x] < b[y]:
            while a[x] < b[y] and x < len(a):
                x = x+1
        else:
            while a[x] > b[y] and y< len(b):
                y =y+1
    return res

def find(quer, ivi):
    res = []
    run = []
    for qu in quer:
        if qu in ivi:
            run.append(ivi[qu])

    run.sort(key = len)
    if len(run) == 0: return res
    res = run[0]
    for x in run:
        res = intersect(res, x)
    return res

def pri(res, doc):
    for i in res:
        print(doc[i])

