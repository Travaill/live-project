import sys
i = 0
res = []
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
dict={}
kk=0
ab=[1,3,5,17,25,43,49]
with open('record.txt', mode='r', encoding='utf-8', errors='ignore') as file:
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
                if user[0] in dict:
                    dict[user[0]]=str(dict[user[0]])+str(line)
                else:    
                    filename = 'num_name.txt'
                    with open(filename,'a',encoding='utf-8') as f:
                        f.write(str(kk))
                        f.write("  :")
                        f.write(user[0])
                        f.write("\n")
                        kk=kk+1
                    dict[user[0]]=str(line)
                res[-1]['data'] += line
        else:
            i = 0
#print(dict)



dict2 = {}  
ls = list(dict.keys())        #ls存储用户账号
ll=len(dict)
list_2d = [[0 for col in range(ll)] for row in range(ll)]
listname=[0 for col in range(ll)]
for i in range(ll):
    data = str(dict[ls[i]])    #同学i的消息
    for j in range(ll):
        if j!=i:
            list_2d[i][j]=list_2d[i][j]+data.count(ls[j])    #出现同学j名字一次，关联度加一
            if (not i in ab)and(not j in ab):
                listname[j]=listname[j]+data.count(ls[j])



try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
#print(list_2d)
G=nx.DiGraph()
#添加带权边
for m in range(ll):
    for n in range(ll):
        if(list_2d[m][n]>0and(not m in ab)and(not n in ab)):
            G.add_edge(str(m),str(n),weight=list_2d[m][n]/10)
#按权重划分为重权值得边和轻权值的边
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.2]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.2]
#节点位置
pos=nx.spring_layout(G) # positions for all nodes
#首先画出节点位置
# nodes
nx.draw_networkx_nodes(G,pos,node_size=70)
#根据权重，实线为权值大的边，虚线为权值小的边
# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=2)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=2,alpha=0.5,edge_color='b',style='dashed')
 
# labels标签定义
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
 
plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display





dict_name={}
for w in range(ll):
    dict_name[str(w)]=listname[w]
#print(dict_name)
#dict_n= sorted(dict_name.iteritems(), key=lambda d:d[1]['val'], reverse = True)
#print(dict_n)


#dict_name存放用户名和被que次数



import matplotlib.pyplot as plt
 
name_list = [col for col in range(ll)]
num_list = listname
rects=plt.bar(range(len(num_list)), num_list, color='rgby')
# X轴标题
index=[col for col in range(ll)]
index=[float(c)+0.4 for c in index]
plt.ylim(ymax=80, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("arrucay(%)") #X轴标签
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')
plt.show()
