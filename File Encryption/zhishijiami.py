import random
import time

zhishulist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]


# 测试dict的聚合特性   已知 24 - 22
# def listtodict(list):
#     dict1={}
#     for i in list:
#         if i not in dict1.keys():
#             dict1[i]=1
#         else:
#             dict1[i]+=1
#     print(max(dict1.values()))
#     return dict1
# 固定数据下0-255集合  转变为 176个不同的可重复数据，长效数据下 减弱 0.31 效用百分比 可作为文件压缩的一种加密。
# 从随机性质上进行研究后，此加密法，压缩可能性正数几率过于低下。
# 仅作为加密方式来使用。

# """测试实例"""
# afblis=[]
# for i in range(3000):
#     afblis.append(random.randint(0,255))
#
# # print(afblis)
#
# alist=[]
# for i in range(len(afblis)):
#     # for j in range(256):
#     alist.append((afblis[i]-zhishulist[i%54]+256)%256)
#
#
#
# print(alist)
# tlist=[]
# for i in range(len(alist)):
#     tlist.append((alist[i]+zhishulist[i%54])%256)
#
# adict={}
# bdict={}
# cdict={}
#
#
# adict=listtodict(alist)
# cdict=listtodict(afblis)
#
# print(afblis)
# print(tlist)
# print(len(afblis),len(tlist))
# for i in range(len(afblis)):
#     if afblis[i]!=tlist[i]:
#         print(i)
#
# set1=set()
# for i in alist:
#     if i not in set1:
#         set1.add(i)
#
# print(len(set1))
# print(adict)
# print(cdict)



# 测试实例如上述
def zhishujiami(fileread,filewrite):
    global zhishulist
    filefr = open(file=fileread, mode="rb")
    filewr = open(file=filewrite, mode="wb")

    while True:
        rd54 = filefr.read(54)
        if len(rd54) != 54:
            filewr.write(rd54)
            break
        for i in range(54):
            rword = rd54[i]
            nums = ((rword - zhishulist[i] + 256) % 256)
            filewr.write(nums.to_bytes(length=1, byteorder="little"))
    filewr.close()
    filefr.close()

def zhishujiemi(fileread,filewrite):
    filerq = open(file=fileread, mode="rb")
    filewq = open(file=filewrite, mode="wb")

    while True:
        rd54 = filerq.read(54)
        if len(rd54) != 54:
            filewq.write(rd54)
            break
        for i in range(54):
            rword = rd54[i]
            nums = ((rword + zhishulist[i]) % 256)
            filewq.write(nums.to_bytes(length=1, byteorder="little"))

    filewq.close()
    filerq.close()


# 调用方式
zhishujiami("file1.7z","filejiami.7z")
time.sleep(.5)
zhishujiemi("filejiami.7z","filejiemi.7z")
