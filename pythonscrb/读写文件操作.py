# 写文件
# encoding=utf8
with open('test.txt','wt',encoding='utf-8') as out_file:
    out_file.write('我会写进文本中\n你呢')

with open('test.txt','rt',encoding='utf-8') as in_file:
    text = in_file.read()

print(text)
