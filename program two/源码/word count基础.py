
import os
path=input('请输入查询文件的路径：')
f=open(path,'r',encoding="utf-8")
L=0                                    #定义行数为L
C=0                                 #定义字符数
W=0                                      #定义单词数
for line in f.readlines():
    L+=1                              #每读取一行，L+1
    for i in line:
        if i==' ' or i=='\n':
            W+=1                    #若读到空格或换行符则单词数W+1
        else:
            C+=1
W=W+1                               #最后一行没有换行符，所以上面少算了1个单词
print("行数：%d"%L)
print("字符数：%d"%C)
print("单词数：%d"%W)
os.system("pause")
