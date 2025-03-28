import time
from PIL import Image


def saveimg(klist=[],paiweidict={},width=256,height=256,savename=r"D:\360安全浏览器下载\nnn.jpg",maximgnum=65536):
    imglist = []
    paiweidict1=paiweidict
    for j in sorted(paiweidict1.keys()):
        imglist.append(j)
    max1=0
    if len(imglist)!=maximgnum:
        for d in range(maximgnum-len(imglist)):
            if d == 255:
                max1+=1
            imglist.append((0,max1,d))
    img = Image.new("RGB", (width, height))
    img.putdata(klist)
    img.save(savename)

# dictg={64:0,128:0,256:0}
def junshu(filename):
    dictl={}
    allnum=0
    fin = open(file=filename, mode="rb")
    while True:
        binary_data = fin.read(1024)
        if not binary_data:
            break
        for d in range(len(binary_data) // 3):
            i = binary_data[d * 3 + 0]
            j = binary_data[d * 3 + 1]
            k = binary_data[d * 3 + 2]
            # if i == " ":
            #     print("i")
            # if j == "":
            #     print("j")
            # if k == "":
            #     print("k")
            # if i-b'\0xFF'<=0 and i - b'\0x80'>0:
            if (i, j, k) in dictl.keys():
                dictl[(i, j, k)] += 1
            else:
                dictl[(i, j, k)] = 1
                allnum += 1

    print(allnum)
    fin.close()
    return dictl

def paiweidict(dictl):
    paiweidict1={}
    alnum = 1
    for j in sorted(dictl.keys()):
        paiweidict1[j]=alnum
        alnum+=1
        # print(j,dictl[j])

    return paiweidict1

def reverse_dict(paiweidict1):
    reverse_dict = {v: k for k, v in paiweidict1.items()}
    return reverse_dict

def yasuofile(filein,fileout,paiweidict={}):
    fout = open(file=fileout, mode="wb")
    fin = open(file=filein, mode="rb")
    alll=0
    paiweidict1=paiweidict
    while True:
        binary_data = fin.read(1024)
        if not binary_data:
            break
        # for i,j,k in binary_data:
        for d in range(len(binary_data) // 3):
            i = binary_data[d * 3 + 0]
            j = binary_data[d * 3 + 1]
            k = binary_data[d * 3 + 2]
            # print(i,1000000,j)
            data1=paiweidict1[(i,j,k)]
            fout.write(data1.to_bytes(2,byteorder='little'))
            alll+=1
    print("压缩完毕！共压缩以下次数",alll)
    fin.close()
    fout.close()

def jieyafile(filein,fileout,rereverse_dict={}):
    fout = open(file=fileout, mode="wb")
    fin = open(file=filein, mode="rb")
    alll = 0
    reverse_dict = rereverse_dict
    while True:
        binary_data = fin.read(1024)
        if not binary_data:
            break
        # for i,j,k in binary_data:
        for d in range(len(binary_data) // 2):
            i = binary_data[d * 2 + 0]
            j = binary_data[d * 2 + 1]

            # print(i,1000000,j)
            bk = i+ j*256
            # bk=str(i)+str(j)
            # print(bk)
            num1 = int(bk)
            data1 = reverse_dict[num1]
            # print(data1[0])
            fout.write(int(data1[0]).to_bytes(1, byteorder='little'))
            fout.write(int(data1[1]).to_bytes(1, byteorder='little'))
            fout.write(int(data1[2]).to_bytes(1, byteorder='little'))
            alll += 1
    print("解压完毕！共解压以下次数",alll)
    fin.close()
    fout.close()



# 目前压缩算法为：自定义的算法，目标文件为1.6M左右，由于压缩后，解压文件还有一些变化性质。不推荐直接使用，建议作为算法的案例使用。
file1=r"D:\360安全浏览器下载\fuben.txt"  #文件位置路径
file3=r"D:\360安全浏览器下载\fubenyasuo1.txt"
file5=r"D:\360安全浏览器下载\fubenjieya1.txt"
# 目前压缩算法为：自定义的算法，目标文件为1.6M左右，由于压缩后，解压文件还有一些变化性质。不推荐直接使用，建议作为算法的案例使用。
dictl=junshu(file1)
# print(dictl)
paiweidict1=paiweidict(dictl)
reverse_dict1=reverse_dict(paiweidict1)
yasuofile(filein=file1,fileout=file3,paiweidict=paiweidict1)
time.sleep(.5)
jieyafile(filein=file3,fileout=file5,rereverse_dict=reverse_dict1)
# 目前压缩算法为：自定义的算法，目标文件为1.6M左右，由于压缩后，解压文件还有一些变化性质。不推荐直接使用，建议作为算法的案例使用。
# 算法的根本是将数据按（255，255，255） 排列，将所有的数据排列（65536以下）进行组合成一个jpg文件18KB左右（PNG文件过大 65KB左右），
# 每三个数据变成2个数据，理论上直接减少三分之一的体积，后续还能进行再度进行压缩，目前算法的7z压缩算法后再次压缩度相似与主文件的zip压缩率接近。除非算法再度优化，否则，理论上很难超过7z压缩算法
# 但此算法开辟了算法的空白（内算法）


