import matplotlib as mpl
mpl.rcParams['font.family'] = 'MS Gothic'

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick   
import os


DATA = np.loadtxt("./InitialState.dat",skiprows=1)
tm = DATA[:,0]
ryua = DATA[:,1]
ryub = DATA[:,2]
ryuc = DATA[:,3]
ryud = DATA[:,4]
ryue = DATA[:,5]
ryuf = DATA[:,6]
ryug = DATA[:,7]



fpath= './InitialState_v01.png'

fig, ax = plt.subplots(dpi=500, figsize=(5,4))   


data = {" 0～ 5m":[ryua[0],ryua[1],ryua[2],ryua[3]],
        " 5～10m":[ryub[0],ryub[1],ryub[2],ryub[3]],
        "10～15m":[ryuc[0],ryuc[1],ryuc[2],ryuc[3]],
        "15～20m":[ryud[0],ryud[1],ryud[2],ryud[3]],
        "20～25m":[ryue[0],ryue[1],ryue[2],ryue[3]],
        "25～30m":[ryuf[0],ryuf[1],ryuf[2],ryuf[3]],
        "30～35m":[ryug[0],ryug[1],ryug[2],ryug[3]]}


df = pd.DataFrame(data, pd.Index(["5s", "10s", "15s", "20s"], name="danmen"))

bottom = np.zeros_like(df.index)
i=0
j=0

k=7
width=0.35
ind = np.arange(4)
ind_p = ind + width/2
ind_m = ind - width/2
ind_line = np.sort(np.concatenate([ind_p,ind_m]))
A_line=[0,0,0,0,0,0,0,0]
h=0
for name in df.columns:
   
    if i == 0:
        cr=255/255
        cg=0/255
        cb=0/255
    elif i == 1:
        cr=0/255
        cg=0/255
        cb=255/255
    elif i == 2:
        cr=0/255
        cg=255/255
        cb=0/255
    elif i == 3:
        cr=250/255
        cg=0/255
        cb=150/255
    elif i == 4:
        cr=250/255
        cg=150/255
        cb=50/255
    elif i == 5:
        cr=100/255
        cg=100/255
        cb=250/255
    elif i == 6:
        cr=250/255
        cg=100/255
        cb=250/255
    elif i == 7:
        cr=0/255
        cg=200/255
        cb=0/255
    
    plt.bar(df.index, df[name], width, bottom=bottom, label=name,color=(cr,cg,cb))
    
    h += 1
    
    B_line = (np.insert(DATA[:,h], np.arange(4), DATA[:,h])) + A_line
    
    plt.plot(ind_line,B_line,'--k',zorder=1,linewidth=0.2)
    
    bottom += df[name]
    i=i+1
    
    k=k-1
    
    if j % 2 == 0:
        j=200/255
    else:
        
        j=60/255
    
    A_line=B_line
 

# #black
cr=0/255
cg=0/255
cb=0/255



plt.ylim(0,25000)
plt.savefig(fpath)

plt.clf()
plt.close()

