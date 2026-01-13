import os
import time






adlist=[[1, 0, 2, 3, 4, 5, 6, 7, 8], [2, 0, 1, 3, 4, 5, 6, 7, 8], [3, 0, 1, 2, 4, 5, 6, 7, 8], [4, 0, 1, 2, 3, 5, 6, 7, 8], [5, 0, 1, 2, 3, 4, 6, 7, 8], [6, 0, 1, 2, 3, 4, 5, 7, 8], [7, 0, 1, 2, 3, 4, 5, 6, 8], [8, 0, 1, 2, 3, 4, 5, 6, 7]]
bdlist=[[1, 0, 2, 3], [1, 0, 3, 2], [2, 0, 1, 3], [2, 0, 3, 1], [3, 0, 1, 2], [3, 0, 2, 1], [1, 2, 0, 3], [2, 3, 0, 1]]
dlist=[[1, 0, 2], [1, 2, 0], [2, 0, 1], [0, 2, 1]]

# for i in dlist:
#     list=[]
#     for j in i:
#         list.append(j-1)
#     dlist1.append(list)
# print(dlist1)

# print(len(adlist))
# print(len(bdlist))
# print(len(dlist))
# 获取修改值
# for i in range(1,10):
#     a=i
#     list1=[]
#     list1.append(a)
#     for j in range(1,10):
#         if j ==a:
#             continue
#         list1.append(j)
#     adist.append(list1)
#     print(list1)
#
# print(adist)


# print(time.thread_time())
# print(time.asctime())
#
# filename=r"E:\xinyuan\zuiku\zuiku.zip - 副本.037.txt"
# # 加密数据
# with open(filename,mode="rb") as filerd,open(filename+"majiangjiami.date",mode="wb") as filewb1:
#     while True:
#         title = 0
#         for fi in range(8):
#             dataall=[]
#             dd1list=[]#9
#             dd2list=[]#9
#             dd3list=[]#9
#             d2list=[]#4
#             d3list=[]#3
#             ddb = filerd.read(34)
#             if len(ddb) < 34:
#                 filewb1.write(ddb)
#                 break
#             for qq in range(27):
#                 if qq<9:
#                     dd1list.append(ddb[qq])
#                 elif qq>17:
#                     dd3list.append(ddb[qq])
#                 else:
#                     dd2list.append(ddb[qq])
#             for tt in range(27,34):
#                 if tt>30:
#                     d3list.append(ddb[tt])
#                 else:
#                     d2list.append(ddb[tt])
#             # print(dd1list,dd2list,dd3list,d2list,d3list)
#
#             for i in range(9):
#                 dataall.append(dd1list[adlist[title][i]])
#             for i in range(9):
#                 dataall.append(dd2list[adlist[title][i]])
#             for i in range(9):
#                 dataall.append(dd3list[adlist[title][i]])
#             for i in range(4):
#                 dataall.append(d2list[bdlist[title][i]])
#             for i in range(3):
#                 dataall.append(d3list[dlist[title%4][i]])
#
#             for it in dataall:
#                 filewb1.write(it.to_bytes(length=1,byteorder="little"))
#             title+=1
#
#
#             # break
#         # break
#         if len(ddb) < 34:
#             break
#
#
# print(time.thread_time())
# print(time.asctime())


# filename=r"E:\xinyuan\zuiku\zuiku.zip - 副本.037.txtmajiangjiami.date"
# 解密数据
# with open(filename,mode="rb") as filerd,open(filename+"jiemi.txt",mode="wb") as filewb1:
#     while True:
#         title = 0
#         for fi in range(8):
#             dataall=[]
#             dd1list=[]#9
#             dd2list=[]#9
#             dd3list=[]#9
#             d2list=[]#4
#             d3list=[]#3
#             jiamidd1list=[0,0,0,0,0,0,0,0,0]
#             jiamidd2list=[0,0,0,0,0,0,0,0,0]
#             jiamidd3list=[0,0,0,0,0,0,0,0,0]
#             jiamid2list=[0,0,0,0]
#             jiamid3list=[0,0,0]
#             ddb = filerd.read(34)
#             if len(ddb) < 34:
#                 filewb1.write(ddb)
#                 break
#             for qq in range(27):
#                 if qq<9:
#                     dd1list.append(ddb[qq])
#                 elif qq>17:
#                     dd3list.append(ddb[qq])
#                 else:
#                     dd2list.append(ddb[qq])
#             for tt in range(27,34):
#                 if tt>30:
#                     d3list.append(ddb[tt])
#                 else:
#                     d2list.append(ddb[tt])
#             # print(dd1list,dd2list,dd3list,d2list,d3list)
#             for i in range(9):
#                 nand = adlist[title][i]
#                 jiamidd1list[nand]=dd1list[i]
#             for i in range(9):
#                 nand = adlist[title][i]
#                 jiamidd2list[nand]=dd2list[i]
#             for i in range(9):
#                 nand = adlist[title][i]
#                 jiamidd3list[nand]=dd3list[i]
#             for i in range(4):
#                 nand = bdlist[title][i]
#                 jiamid2list[nand]=d2list[i]
#             for i in range(3):
#                 nand = dlist[title%4][i]
#                 jiamid3list[nand]=d3list[i]
#
#             for i in range(9):
#                 dataall.append(jiamidd1list[i])
#             for i in range(9):
#                 dataall.append(jiamidd2list[i])
#             for i in range(9):
#                 dataall.append(jiamidd3list[i])
#             for i in range(4):
#                 dataall.append(jiamid2list[i])
#             for i in range(3):
#                 dataall.append(jiamid3list[i])
#
#             for it in dataall:
#                 filewb1.write(it.to_bytes(length=1,byteorder="little"))
#             title+=1
#
#
#             # break
#         # break
#         if len(ddb) < 34:
#             break
# print("wancheng")
#
#
# print(time.thread_time())
# print(time.asctime())





pathsr=r"E:/xinyuan/zuiku"

# filename=r"E:\xinyuan\zuiku\zuiku.zip - 副本.037.txt"

for file in os.listdir(pathsr):
    print(time.thread_time())
    print(time.asctime())
    filename=pathsr+"/"+file
    with open(filename, mode="rb") as filerd, open(filename + "2026111.date", mode="wb") as filewb1:
        while True:
            title = 0
            for fi in range(8):
                dataall = []
                dd1list = []  # 9
                dd2list = []  # 9
                dd3list = []  # 9
                d2list = []  # 4
                d3list = []  # 3
                ddb = filerd.read(34)
                if len(ddb) < 34:
                    filewb1.write(ddb)
                    break
                for qq in range(27):
                    if qq < 9:
                        dd1list.append(ddb[qq])
                    elif qq > 17:
                        dd3list.append(ddb[qq])
                    else:
                        dd2list.append(ddb[qq])
                for tt in range(27, 34):
                    if tt > 30:
                        d3list.append(ddb[tt])
                    else:
                        d2list.append(ddb[tt])
                # print(dd1list,dd2list,dd3list,d2list,d3list)

                for i in range(9):
                    dataall.append(dd1list[adlist[title][i]])
                for i in range(9):
                    dataall.append(dd2list[adlist[title][i]])
                for i in range(9):
                    dataall.append(dd3list[adlist[title][i]])
                for i in range(4):
                    dataall.append(d2list[bdlist[title][i]])
                for i in range(3):
                    dataall.append(d3list[dlist[title % 4][i]])

                for it in dataall:
                    filewb1.write(it.to_bytes(length=1, byteorder="little"))
                title += 1

                # break
            # break
            if len(ddb) < 34:
                break
    time.sleep(2.5)
    print(filename,"已经完成加密。")

# 加密数据


jiamiwen:E:\xinyuan\zuiku\zuiku.zip - 副本.037.txt-------2026111(*).date,2026/01/11上传成功。
