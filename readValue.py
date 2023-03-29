# doc lst tu vung
f = open("npl/term-vocab", "r")

lstVocab = []

lstDoc = [""]
lstQuery = [""]

for i in f:
    record = i.split()

    try:
        lstVocab.append(record[1])
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
        lstDoc.append("")

        # print("doc i= ", i)
    except ValueError:
        print("format tai lieu ", i)
        break
    except StopIteration as e:
        print(e)
        break

    strI = next(iterFile)
    while "/" not in strI:
        lstDoc[i] += strI
        strI = next(iterFile)

f.close()




# doc lst query

f = open("npl/query-text", "r")
iterFile = iter(f)

strI = ""
while True:

    try:
        strI = next(iterFile)
        i = int(strI)
        lstQuery.append("")

    except ValueError:
        print("format tai lieu ", i)
        break
    except StopIteration as e:
        print(e)
        break

    strI = next(iterFile)

    while "/" not in strI:
        lstQuery[i] += strI
        strI = next(iterFile)

f.close()
