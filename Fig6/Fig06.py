import matplotlib as mpl
mpl.rcParams['font.family'] = 'MS Gothic'


import numpy as np
import matplotlib.pyplot as plt
import os


input_folder="XZ2D_SfZbH_20230427"
# input_folder="XZ2D_SfZbH_20230426"

fig = plt.figure(dpi=500, figsize=(8,3))
ihk=0
for file_name in os.listdir(input_folder):

    DATA = np.loadtxt(os.path.join(input_folder, file_name),skiprows=1)
    xp = DATA[:,0]
    aveU = DATA[:,1]
    eneU= DATA[:,2]      
    eneP= DATA[:,3]
    eneZ= DATA[:,4] 
    q= DATA[:,5] 
    Area = DATA[:,6]
    H = DATA[:,7]
    eee= DATA[:,8]      
    specificene= DATA[:,9]
    As= DATA[:,10] 
    Aw= DATA[:,11] 
    ezb= DATA[:,12] 
    sf= DATA[:,13] 
    zb= DATA[:,14]
    dzb= DATA[:,15] 
   
    fname = os.path.basename(file_name)
    bname, ext =  os.path.splitext( fname )
    fpath= './png/' + bname + '.' + 'png'
    t,u=bname.split('=')
    v=float(u)
    w=v/10000
    ss=str(w) + 's'
    fpath= './png_H/' + bname + '.' + 'png'

    if ss == '5.0s':
        # blue
        cr=0/255
        cg=0/255
        cb=255/255
        plt.plot(xp,sf,color=(cr,cg,cb),linewidth=1)
    elif ss == '10.0s':
         # Red
        cr=255/255
        cg=0/255
        cb=0/255
        plt.plot(xp,sf,color=(cr,cg,cb),linewidth=1)
    elif ss == '15.0s':
        # Lime
        cr=0/255
        cg=255/255
        cb=0/255
        plt.plot(xp,sf,color=(cr,cg,cb),linewidth=1)
    elif ss == '20.0s':
        # Salmon
        cr=250/255
        cg=128/255
        cb=114/255
        plt.plot(xp,sf,color=(cr,cg,cb),linewidth=1)

    # plt.legend(fontsize=8,ncol=2)
    plt.xlim(5,35)
    # plt.ylim(10,23)

    plt.minorticks_on()

sname='Fig06b.png'
plt.savefig(sname)