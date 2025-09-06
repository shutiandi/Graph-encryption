
def process_file(input_file_path, output_file_path,numsize=128):
    # 打开输入文件以二进制模式读取
    with open(input_file_path, 'rb') as input_file:
        # 打开输出文件以二进制模式写入
        with open(output_file_path, 'wb') as output_file:
            while True:
                # 每次读取1024字节的数据
                data_chunk = input_file.read(numsize)

                # 如果没有更多的数据可读，则退出循环
                if len(data_chunk)<numsize:
                    output_file.write(data_chunk)
                    break

                # 将数据分成两部分
                mid_index = len(data_chunk) // 2
                var1 = data_chunk[:mid_index]
                var2 = data_chunk[mid_index:]

                # 将var1和var2_modified的数据写入输出文件
                output_file.write(var2)
                output_file.write(var1)


def reprocess_file(oldfile,newfile,numsize=128):
    with open(oldfile, 'rb') as input_file:
        # 打开输出文件以二进制模式写入
        with open(newfile, 'wb') as output_file:
            while True:
                # 每次读取1024字节的数据
                data_chunk = input_file.read(numsize)

                # 如果没有更多的数据可读，则退出循环
                if len(data_chunk)<numsize:
                    output_file.write(data_chunk)
                    break

                # 将数据分成两部分
                mid_index = len(data_chunk) // 2
                var1 = data_chunk[:mid_index]
                var2 = data_chunk[mid_index:]

                # # 将var1和var2_modified的数据写入输出文件
                output_file.write(var2)
                output_file.write(var1)

file1="ximo1.txt"
file2="ximo2.txt"
file3="ximo3.txt"

process_file(input_file_path=file1,output_file_path=file2,numsize=1024)

reprocess_file(oldfile=file2,newfile=file3,numsize=1024)
