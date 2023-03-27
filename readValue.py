# doc lst tu vung
f = open("npl/term-vocab", "r")
lstVocab = []

for i in f:
    record = i.split()

    try:
        lstVocab.append(record[1])
    except Exception:
        break
# doc lst van ban
f = open("npl/doc-text", "r")
lstDoc = [""]*8000
iterFile = iter(f)
strI = next(iterFile)
while strI:

    try:
        i = int(strI)
        print("doc i= ",i )
    except ValueError:
        break
    strI = next(iterFile)

    while strI != "   /":
        lstDoc[i] += strI
        print(strI)
        strI = next(iterFile)
    print("xong doc", i)


