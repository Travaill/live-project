
# coding: utf-8

# In[34]:


import re
import subprocess
import time
from time import strftime,localtime
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from qqbot import _bot as bot


def spider_stop():#用于结束爬取进程
    order ='qq stop'
    pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
    print("倒计时时间已到！\n")
    
def mess_spider(time_min):#爬取聊天内容
    order ='qqbot'
    flag = 0#用于判断用户是否已登录成功
    pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
    for i in iter(pi.stdout.readline,'b'):
        login_sig = r'\[INFO\] 登录成功。登录账号：'
        result = re.compile(login_sig).findall(i.decode("gbk"))
        if len(result) != 0:
            print("用户登录成功开始计时\n")
            curr_time = time.time()
            flag = 1
        if flag == 1:
            files = open("C:\\Users\\Administrator\\Desktop\\input.txt",'a')
            files.write(i.decode("gbk")+'\n')
            files.close()
            if time.time() >= float(curr_time) + (float(time_min) * 60):
                spider_stop()
                break
    #print (i.decode("gbk"))

def mess_parser(str):#分析并将指定群聊的聊天内容写入文件
    file = open("C:\\Users\\Administrator\\Desktop\\input.txt",'r')
    string = file.read()
    file.close()
    target = r'\[(.*?)\] \[INFO\] 来自 群“(.*?)”\[成员“(.*?)”\] 的消息: "(.*?)"'
    result = re.compile(target).findall(string)
    output = open("C:\\Users\\Administrator\\Desktop\\output.txt",'w')
    mess_content = open("C:\\Users\\Administrator\\Desktop\\mess_content.txt",'w',encoding = 'gbk')
    for data in result:
        if data[1]==str:
            print(data[0]+" "+data[2]+"()\n"+data[3]+"\n\n")
            output.write(data[0]+" "+data[2]+"()\n"+data[3]+"\n\n")  
            mess_content.write(data[3]+"\n")  
    output.close()
    mess_content.close()
#print(result)

def hot_words(num):
    f = open('C:\\Users\\Administrator\\Desktop\\mess_content.txt','r').read()
    wordcloud = WordCloud(
            background_color="white", #设置背景为白色，默认为黑色
            width=1500,              #设置图片的宽度
            height=960,              #设置图片的高度
            max_words=num,            #设置显示的热词数
            margin=10               #设置图片的边缘
            ).generate(f)
    # 绘制图片
    plt.imshow(wordcloud)
    # 消除坐标轴
    plt.axis("off")
    # 展示图片
    plt.show()
    # 保存图片
    wordcloud.to_file('C:\\Users\\Administrator\\Desktop\\hot words2.png')


# In[35]:


if __name__=="__main__":
    print("输入群名：")
    group_name = input()
    print("请输入倒计时长，以分钟为单位：")
    time_min = input()
    #print("请输入要统计的热词数")
    #num = input()
    mess_spider(time_min)
    mess_parser(group_name)
    #hot_words(num)
    

