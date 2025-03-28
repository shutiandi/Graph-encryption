def filetablenum(file1,file2):
    if os.path.exists(file2):
        return os.path.getsize(file2)//os.path.getsize(file1)+1
    else:
        raise "FileNotFoundError"


def byte_dec_one(byte,byte2):
    int1=int(byte)
    int2=int(byte2)
    if int1< int2:
        return byte+256-byte2  #输出结果分成多部分进行修改
    else:
        return byte-byte2

def byte_plus_one(byte,byte2):
    return (byte + byte2) % 256  # 确保结果在 0-255 范围内
# 修改文件

def modify_binary_file(file_path, modify_func, output_path=None,jiamifile=r"r0-255-255-255.png",numda=8):
    # 默认输出路径为输入文件路径（覆盖原文件）
    if output_path is None:
        output_path = file_path
    # file2 =jiamifile
    binaryarray_data2=[]
    for j in range(numda):
        with open(jiamifile, 'rb') as fins:
            binaryarray_data2.append(fins.read())
        fins.close()
    binary_data2 = b''.join(binaryarray_data2)
    linshifile="ddt.bin"
    with open(linshifile, 'wb') as fbin:
        fbin.write(binary_data2)
    fbin.close()
    # 保存数据，可以自行指定规则文件组合，重复等等手段
    # 因文件过大，每次读取1024字节文件


    filebin=open(file=linshifile,mode="rb")

        # 打开文件并读取二进制数据

    fin=open(file=file_path,mode="rb")
    while True:
        binary_data = fin.read(1024)
        if not binary_data:
            break
        binary_data2=filebin.read(1024)
        # 对每个字节应用修改函数
        modified_data = bytes(modify_func(byte,byte2) for byte,byte2 in zip(binary_data,binary_data2))
        with open(output_path, 'ab') as fout:
            fout.write(modified_data)
    filebin.close()    # 后续需要删除filebin包括的文件，这里需要一直使用，暂时没有删去
    # 将修改后的数据写回文件
  # 后续为调用程序，
  # 目前版本将filetablenum 组合编写加密的规则文件，为最基础的程序之一。
# 有一定风险，请开发时，注意文件数据的安全性验证。
# 加密后，数据的丰度逐渐趋近，即每种数据的可靠性都临近，因此，文件压缩的压缩率会下降%30-%60之间，请确认是否需要使用该算法进行加密。
