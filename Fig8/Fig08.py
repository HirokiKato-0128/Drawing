import matplotlib as mpl
mpl.rcParams['font.family'] = 'MS Gothic'


import numpy as np
import matplotlib.pyplot as plt
import os

input_folder="ParticleSizeDistribution_Front"
fig, ax = plt.subplots(dpi=500, figsize=(4,3))   
ihk=-1
for file_name in os.listdir(input_folder):

    DATA = np.loadtxt(os.path.join(input_folder, file_name),skiprows=1)
    d = DATA[:,0]
    mpar = DATA[:,1]
    lw=1.5
    ihk=ihk+1
    if ihk==1:
        s="05s"
        cr=0/255
        cg=0/255
        cb=0/255
        plt.plot(d,mpar,label=s,color=(cr,cg,cb),linewidth=lw)
    elif ihk==2:
        s="10s"
        cr=0/255
        cg=200/255
        cb=0/255
        plt.plot(d,mpar,label=s,color=(cr,cg,cb),linewidth=lw)
    elif ihk==3:
        s="15s"
        cr=0/255
        cg=0/255
        cb=250/255
        plt.plot(d,mpar,label=s,color=(cr,cg,cb),linewidth=lw)
    elif ihk==4:
        s="20s"
        cr=250/255
        cg=0/255
        cb=0/255
        plt.plot(d,mpar,label=s,color=(cr,cg,cb),linewidth=lw)

    plt.legend(fontsize=9)

    plt.xlim(0.1,1.0)

    plt.ylim(0,100)

    plt.minorticks_on()

    ax.set_xscale('log')
    
sname= 'Fig08.png'
plt.savefig(sname)