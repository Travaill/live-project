import sys
import json
import codecs
i = 0
res = []
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
with open('test.txt', mode='r', encoding='utf-8', errors='ignore') as file:
    for line in file.readlines():
        line = line.translate(non_bmp_map)
        line = line.encode('utf-8').decode('utf-8-sig').strip()
        if (len(line) > 1):
            i += 1
            if (i == 1):
                word = line.split()
                try:
                    user = word[2].split('(')
                    temp = {'date': word[0], 'time': word[1], 'username': user[0],'account':user[1][0:(len(user[1])-1)], 'data': ''}
                    res.append(temp)
                except:
                    continue

            else:
                res[-1]['data'] += line

        else:
            i = 0

#with codecs.open('preprocess.json', 'w','utf-8') as f:
    #json.dump(res,f,ensure_ascii=False)
print(res)
