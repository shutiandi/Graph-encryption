
filename="10474_clipped.MP4"
jiamiwrfilename="10474_clipped.MP4fanzhuanjianjianmilist1.txt"
jiemiwrfilename1 = "10474_clipped.MP4fanzhuanjianjianjiemilist1.txt"


with open(file=filename, mode="rb") as filerd, open(file=jiamiwrfilename, mode="wb") as filewd:
    while True:
        numtree=filerd.read(2)
        if len(numtree)<2:
            filewd.write(numtree)
            break
        for i in numtree:
            ssq=""
            shi=0
            ge = i % 10
            if i>100:
                shi = (i // 10)% 10
            if i < 10:
                ssq=str(i)
            elif i % 10 == 0:
                ssq=str(i)
            elif shi % 10 == 0:
                ssq=str(i)
            elif i < 100:
                sst = str(i)
                ssq=sst[1] + sst[0]
            elif i > 100 and i < 200:
                sst = str(i)
                ssq=sst[0] + sst[2] + sst[1]
            elif i > 200 and ge >= 6:
                ssq=str(i)
            elif i>200 and ge<=5:
                sst = str(i)
                ssq=sst[0] + sst[2] + sst[1]
            filewd.write(int(ssq).to_bytes(length=1,byteorder="little"))

with open(file=jiamiwrfilename, mode="rb") as filerd, open(file=jiemiwrfilename1, mode="wb") as filewd:
    while True:
        numtree=filerd.read(2)
        if len(numtree)<2:
            filewd.write(numtree)
            break
        for i in numtree:
            ssq = ""
            shi = 0
            ge = i % 10
            if i > 100:
                shi = (i // 10)% 10
            if i < 10:
                ssq = str(i)
            elif i % 10 == 0:
                ssq = str(i)
            elif shi % 10 == 0:
                ssq = str(i)
            elif i < 100:
                sst = str(i)
                ssq = sst[1] + sst[0]
            elif i > 100 and i < 200:
                sst = str(i)
                ssq = sst[0] + sst[2] + sst[1]
            elif i > 200 and ge >= 6:
                ssq = str(i)
            elif i > 200 and ge <= 5:
                sst = str(i)
                ssq = sst[0] + sst[2] + sst[1]
            filewd.write(int(ssq).to_bytes(length=1,byteorder="little"))

# 由于数据处于变体加密方式，非常规数据，在数据压缩后，略微大于原本数据压缩的压缩比例。%3往上的比例范围，越大文件则比例约高
