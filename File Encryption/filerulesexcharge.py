
import time

liebiaolist=[] #按规律来进行交换
zidiandict={} # 自定义交换规则
nums=0 #按个数进行交换 一般推荐

filename1=""
filename2=""
filename3=""

# 矩阵效应 影响下，dictmod 出现形变bug，  为固定bug，无法修理。请注意自行规避
nums=128
liebiaolist=[2048,1024,512,256,128,64,32]
zidianzongdict={"1600":[7,11,17,19,23,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127],"32":[2,3,5,7,11,13,17,19,23,29,31],"64":[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61],"128":[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127],"256":[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257]}

def numrdmod(filerdname1,filewdname2,nums):
    with open(file=filerdname1,mode="rb") as frd1,open(file=filewdname2,mode="wb") as fwd1:
        while True:
            fwstr = frd1.read(nums * 2)
            if len(fwstr) == nums * 2:
                fwd1.write(fwstr[nums:])
                fwd1.write(fwstr[:nums])
            else:
                fwd1.write(fwstr)
                break
def listmod(filerdname1,filewdname2,typelist):
    listnum=0
    with open(file=filerdname1,mode="rb") as frd1,open(file=filewdname2,mode="wb") as fwd1:
        while True:
            fwstr = frd1.read(typelist[listnum%len(typelist)] * 2)
            if len(fwstr) == typelist[listnum%len(typelist)] * 2:
                fwd1.write(fwstr[nums:])
                fwd1.write(fwstr[:nums])
                listnum+=1
            else:
                fwd1.write(fwstr)
                break

# dictmod 存在过量数据溢出异常现象，会导致某些特定数据会直接改写，暂时无法修复
def dictmod(filerdname1, filewdname2, zidiandict, ztnum="1600"):
    linshilist = zidiandict[ztnum]
    with open(file=filerdname1, mode="rb") as frd1, open(file=filewdname2, mode="wb") as fwd1:
        while True:
            lastedchar=b''
            postion=0
            for i in linshilist:
                fwstr=frd1.read(i * 2)+lastedchar
                postion+=i*2
                lastedchar=fwstr
                if fwstr[0] == fwstr[len(fwstr) // 2]:
                    break
            if len(fwstr) ==postion:
                half = len(fwstr) // 2
                fwd1.write(fwstr[half:])
                fwd1.write(fwstr[:half])
            else:
                fwd1.write(fwstr)
                break

# 测试案例

# numrdmod(filerdname1=filename1,filewdname2=filename2,nums=nums)
# time.sleep(.6)
# numrdmod(filerdname1=filename2,filewdname2=filename3,nums=nums)

# 测试案例

# listmod(filerdname1=filename1,filewdname2=filename2,typelist=liebiaolist)
# time.sleep(.6)
# listmod(filerdname1=filename2,filewdname2=filename3,typelist=liebiaolist)


# # 测试案例
# 文件存在不可修复（修复时间无限长bug）
# dictmod(filerdname1=filename1,filewdname2=filename2,zidiandict=zidianzongdict,ztnum="1600")
# time.sleep(.5)
# dictmod(filerdname1=filename2,filewdname2=filename3,zidiandict=zidianzongdict,ztnum="1600")




# 错误代码：
# # def dictmod(filerdname1,filewdname2,zidiandict,ztnum="1600"): linshilist=zidiandict[ztnum] with open(file=filerdname1,mode="rb") as frd1,open(file=filewdname2,mode="wb") as fwd1: while True: lasted=0 fwstr=[] for i in linshilist: fwstr = frd1.read((lasted+i) * 2) lasted=len(fwstr)//2 try: if fwstr[0]==fwstr[len(fwstr)//2]: break except IndexError: print(fwstr) if len(fwstr) == lasted* 2: fwd1.write(fwstr[lasted:]) fwd1.write(fwstr[:lasted]) else: fwd1.write(fwstr) break dictmod(filerdname1=filename1,filewdname2=filename2,zidiandict=zidianzongdict,ztnum="1600") 查询代码的错误部分。
