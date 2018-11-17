import json
with open("preprocess.json",'r',encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

date = []
time = []
username = []
account = []
data = []

for my_load in load_dict:
    i = 0
    for key in my_load:
        # print(i)
        # print(my_load[key])
        # i += 1
        if i == 0:
            #print('date ' + str(my_load[key]))
            date.append(str(my_load[key]))
        if i == 1:
            #print('time ' + str(my_load[key]))
            time.append(str(my_load[key]))
        if i == 2:
            # print('username ' + str(my_load[key]))
            username.append(str(my_load[key]))
        if i == 3:
            # print('account ' + str(my_load[key]))
            account.append(str(my_load[key]))
        if i == 4:
            # print('data ' + str(my_load[key]))
            data.append(str(my_load[key]))
        i += 1
print(data)
val = []
for i in range(len(data)):
    if '#我要红包' in data[i]:
        val.append('1')
    else:
        val.append('0')

# print(val)
# print(len(val))
for i in range(len(data) - 1):
    mystr = username[i] + '|' + account[i] + '|' + date[i] + ' ' + time[i] + '|' + val[i] + '\n'
    with open('data.txt','a+',encoding='utf-8') as f:
        f.write(mystr)

mylen = len(data) - 1


with open('data.txt', 'a+', encoding='utf-8') as f:
    ystr = username[mylen] + '|' + account[mylen] + '|' + date[mylen] + ' ' + time[mylen] + '|' + val[mylen]
    f.write(ystr)
