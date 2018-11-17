# _*_ coding:utf-8 _*_
import os
import numpy as np
import random
import datetime
import operator



def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.strip(' ')
    return text
def str_date(str):
    date = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
    return date

def common_fileter(time_id, val_id):
    for key in time_id:
        my_time = time_id[key]
        for i in range(len(my_time)):
            diff = str_date(my_time[len(my_time) - 1]) - str_date(my_time[i])
            if diff.days <= 14 and diff.days > 1:
                val_id.add(key)
    return val_id

def complex_fileter(time_id, val_id):
    for key in time_id:
        my_time = time_id[key]
        for i in range(len(my_time)):
            diff = str_date(my_time[len(my_time) - 1]) - str_date(my_time[i])
            if diff.days <= 3 and diff.days > 1:
                val_id.add(key)
    return val_id

def search():
    with open('search.txt','r',encoding = 'utf-8-sig') as f:
        a = f.readline()
        b = f.readline()
        return int(a),b

if __name__ == '__main__':
    #os.system("")
    dict_name = {}
    dict_time = {}
    dict_date = {}
    val_id = set()
    with open('preprocess.txt', 'r', encoding='utf-8-sig') as f:
        i = 0
        for line in f.readlines():
            text = line.split('|')
            dict_name[str(text[i+1])] = text[i]
            if text[i+1] in dict_time.keys():
                dict_time[str(text[i+1])] += 1
            else:
                dict_time[text[i+1]] = int(text[i+3])
            if text[i+1] in dict_date.keys():
                # print(dict_date[str(text[i+1])])
                dict_date[str(text[i+1])].append(text[i+2])
            else:
                list1 = []
                list1.append(text[i+2])
                dict_date[str(text[i+1])] = list1

    #print(dict_date)
    m,n = search()

    if m==1:
        val_id = common_fileter(dict_date, val_id)
    elif m==2:
        val_id = complex_fileter(dict_date, val_id)
    else:
        val_id = dict_name.keys()
    #print(val_id)
    dict_loss = {}
    for i in dict_time.keys():
        a = random.random()
        dict_loss[i] = np.square(a+0.5*dict_time[i])/np.sqrt(1+0.5*dict_time[i])
    fp = open('result.txt','w',encoding='utf-8-sig')
    sorted(dict_loss.items(), key=operator.itemgetter(1))
    for id in val_id:
        # print(dict_loss[id])
        print(id, dict_loss[str(id)])
        fp.write(id+'\n')


    #print(dict_loss)
