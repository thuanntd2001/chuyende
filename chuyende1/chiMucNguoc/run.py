"""
Nguyen Tran Duc Thuan
MSSV: N19DCN203
Vu Cao Ky
MSSV: N19DCN048
Vu Trung An
MSSV: N19DCN003
"""
# doc lst tu vung
from main import filterStopWords, trans, search, find, pri
from nltk.tokenize import word_tokenize
f = open("npl/term-vocab", "r")
lstVocab = []
lstDoc = [""] * 12000
lstQuery = [""] * 100


for i in f:
    record = i.split()
    try:
        lstVocab.append(record[1].lower())
    except Exception:
        break
f.close()


# doc lst van ban
f = open("npl/doc-text", "r")
iterFile = iter(f)

strI = ""
while True:

    try:
        strI = next(iterFile)
        i = int(strI)
        
    except ValueError:
        print("format tai lieu ", i)
        break
    except StopIteration as e:
        print(e)
        break

    strI = next(iterFile)

    while "/" not in strI:
        lstDoc[i] += strI.lower()
        
        strI = next(iterFile)
    

#print(lstDoc[1])
f.close()
# doc lst query

f = open("npl/query-text", "r")
iterFile = iter(f)

strI = ""
while True:

    try:
        strI = next(iterFile)
        i = int(strI)
        
    except ValueError:
        print("format tai lieu ", i)
        break
    except StopIteration as e:
        print(e)
        break

    strI = next(iterFile)

    while "/" not in strI:
        lstQuery[i] += strI.lower()
        
        strI = next(iterFile)
    

#print(lstQuery[1])
f.close()
lstQuery1 = trans(lstQuery)
print('done query')
ivindex = search(lstVocab, lstDoc)
y = 0
for i in lstQuery1:
    print('query', y, find(i, ivindex))
    y=y+1


# luu file
f = open("save.txt", "w")
for i in ivindex:
    f.write(i)
    f.write("\n")
    for j in ivindex[i]:
        f.write(str(j))
        f.write(" ")
    f.write("\n")
f.close()




