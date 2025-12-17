filename="txtfileshiyan.txt"
jiamiwrfilename="txtfileoddjianmilist1.txt"
jiemiwrfilename1 = "txtfileoddjianjiemilist1.txt"

# # # jiafa加密方案
# 验证加法加密
# for i in listjia2:
#     num=251
#     ad=(i+num)
#     ai=ad%256
#     ak=(ai-i+256)%256
#     print(i,ak)
# with open(file=filename, mode="rb") as filerd, open(file=jiamiwrfilename, mode="wb") as filewd:
#     while True:
#         numtree=filerd.read(64)
#         if len(numtree)<64:
#             filewd.write(numtree)
#             break
#         for i in range(len(listjiafa)):
#             ad=(listjiafa[i]+numtree[i])%256
#             filewd.write(ad.to_bytes(length=1,byteorder="little"))


# with open(file=jiamiwrfilename, mode="rb") as filerd, open(file=jiemiwrfilename1, mode="wb") as filewd:
#     while True:
#         numtree=filerd.read(64)
#         if len(numtree)<64:
#             filewd.write(numtree)
#             break
#         for i in range(len(listjiafa)):
#             ad=(numtree[i]-listjiafa[i]+256)%256
#             filewd.write(ad.to_bytes(length=1,byteorder="little"))

# 验证减法
# for i in listjia29:
#     num=1
#     ad=(num-i+256)
#
#     ai=ad%256
#     ak=(ai+i)%256
#     print(ai,i,ak)
# with open(file=filename, mode="rb") as filerd, open(file=jiamiwrfilename, mode="wb") as filewd:
#     while True:
#         numtree=filerd.read(len(listjianfa))
#         if len(numtree)<len(listjianfa):
#             filewd.write(numtree)
#             break
#         for i in range(len(listjianfa)):
#             ad=(numtree[i]-listjianfa[i]+256)%256
#             filewd.write(ad.to_bytes(length=1,byteorder="little"))

with open(file=jiamiwrfilename, mode="rb") as filerd, open(file=jiemiwrfilename1, mode="wb") as filewd:
    while True:
        numtree = filerd.read(len(listjianfa))
        if len(numtree) < len(listjianfa):
            filewd.write(numtree)
            break
        for i in range(len(listjianfa)):
            ad = (numtree[i] + listjianfa[i]) % 256
            filewd.write(ad.to_bytes(length=1, byteorder="little"))

