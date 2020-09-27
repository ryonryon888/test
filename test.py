"""
このファイルに解答コードを書いてください
"""

fin = open('input.txt','r')
#fin = open('sample1.txt','r')
lines = fin.readlines()
fin.close()
data = list()

#データの読み込み
for line in lines:
    if ':' in line:
        i, s = line.split(':')
        data.append((int(i),s))
    else:
        m = int(line)
        break

#iについて昇順ソート
data.sort(key=lambda x: x[0])

#条件を満たす文字列を保存
res = ""
for d in data:
    i, s = d
    if m % i == 0:
        res += s[:-1]

#出力(空の時 m　を出力)
if res != "":
    print(res)
else:
    print(m)