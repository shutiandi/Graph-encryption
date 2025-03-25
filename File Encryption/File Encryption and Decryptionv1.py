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
def modify_binary_file(file_path, modify_func, output_path=None):
    # 默认输出路径为输入文件路径（覆盖原文件）
    if output_path is None:
        output_path = file_path
    file2 =r"r0-255-255-255.png"
        # 打开文件并读取二进制数据
    with open(file_path, 'rb') as fin:
        binary_data = fin.read()
    with open(file2, 'rb') as fins:
        binary_data2 = fins.read()
        # 对每个字节应用修改函数
    modified_data = bytes(modify_func(byte,byte2) for byte,byte2 in zip(binary_data,binary_data2))

    # 将修改后的数据写回文件
    with open(output_path, 'wb') as fout:
        fout.write(modified_data)

modify_binary_file(r'E:xiugai0.PNG', byte_plus_one, r'xiugai1.PNG')
modify_binary_file(r'xiugai1.PNG', byte_dec_one, r'xiugai2.PNG')
