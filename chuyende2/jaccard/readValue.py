# doc lst tu vung
from main import *
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
print("press E to exit")

print(jaccaard(lstDoc, lstQuery[1], 2))

'''
while 1 == 1:
    print('enter your query: ')
    x = input()
    if x == 'E': break
    print(jaccaard(lstDoc, x, 5))
'''



