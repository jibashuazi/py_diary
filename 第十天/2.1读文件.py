"""
过程：
1、打开文件
2、读文件内容
3、关闭文件
"""
"""
1、打开文件
open(path,flag[,encoding][,errors])
path:要打开文件的路径
flag:打开方式
r   以只读的方式打开文件夹，文件的描述符放在文件的开头
rb 以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r+ 打开一个文件用于读写，文件的描述符放在文件的开头
w  打开一个文件值用于写入，如果该文件已经存在会覆盖，如果不存在则创建新文件
wb 打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，如果不存在则创建新文件
w+ 打开一个文件用于读写
a  打开一个文件用于追加，如果文件存在，文件描述符将会方到文件末尾
a+ 打开一个文件用于追加读写

encoding:编码方式
errors：错误处理
"""

path = r"C:\Users\Administrator\Desktop\课件\第十天\file1.txt"
#ignore 忽略错误
f = open(path,"r",encoding="utf-8",errors="ignore")

"""
2、读文件内容
"""
#1、读取文件全部内容
# str1 = f.read()
# print(str1)

#2、读取指定字符数
# str2 = f.read(10)
# print("*"+str2+"*")

#3、读取整行，包括 “\n” 字符
# str3 = f.readline()
# print("*"+str3+"*")

#4、读取指定字符数
# str4 = f.readline(10)
# print("*"+str4+"*")

#5、读取所以行返回列表
# str5 = f.readlines()
# print(str5)

#6、若给定数字大于0，返回实际size字节的行数
# str6 = f.readlines(1)
# print(str6)

#7、修改描述符的位置
# f.seek(10)
# str7 = f.read()
# print(str7)

"""
关闭文件
"""
f.close()

with open(path,"r",encoding="utf-8") as f2:
    print(f2.read())

try:
    f3 = open(path,"r",encoding="utf-8")
    print(f3.read())
finally:
    if f3:
        f3.close()



