import time

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
        # 打开文件并读取二进制数据
    with open(file_path, 'rb') as fin:
        binary_data = fin.read()
    for j in range(numda):
        with open(jiamifile, 'rb') as fins:
            binaryarray_data2.append(fins.read())
        fins.close()
    binary_data2=b''.join(binaryarray_data2)
        # 对每个字节应用修改函数
    modified_data = bytes(modify_func(byte,byte2) for byte,byte2 in zip(binary_data,binary_data2))

    # 将修改后的数据写回文件
    with open(output_path, 'wb') as fout:
        fout.write(modified_data)

modify_binary_file(r'E:xiugai0.PNG'', byte_plus_one, r'E:xiugai1.PNG',numda=1)
# 增加了numda，参数意思是需要多少个相同的加密规则文件才能比加密文件大，目前直接设定了数值，如有需要请自行写代码进行计算
modify_binary_file(r'E:xiugai1.PNG', byte_dec_one, r'E:xiugai2.PNG',numda=1)
# 修改版本用于大型文件的加密解密
