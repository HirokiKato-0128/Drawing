import matplotlib as mpl
mpl.rcParams['font.family'] = 'MS Gothic'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick   
import os

input_folder="Q-Qs-Qw-v02"
#input_folder="EQ-A"
#input_folder="t01"

for file_name in os.listdir(input_folder):

    DATA = np.loadtxt(os.path.join(input_folder, file_name),skiprows=1)
    tim = DATA[:,0]
    Qs05= DATA[:,1]
    Qs10= DATA[:,2]
    Qs11= DATA[:,3] 
    Qs12= DATA[:,4]
    Qs13= DATA[:,5] 
    Qs14= DATA[:,6] 
    Qs15= DATA[:,7]
    Qs16= DATA[:,8] 
    Qs17= DATA[:,9]
    Qs18= DATA[:,10] 
    Qs19= DATA[:,11] 
    Qs20= DATA[:,12]
    Qw05= DATA[:,13]
    Qw10= DATA[:,14]
    Qw11= DATA[:,15] 
    Qw12= DATA[:,16]
    Qw13= DATA[:,17] 
    Qw14= DATA[:,18] 
    Qw15= DATA[:,19]
    Qw16= DATA[:,20] 
    Qw17= DATA[:,21]
    Qw18= DATA[:,22] 
    Qw19= DATA[:,23] 
    Qw20= DATA[:,24]
    Qall05= DATA[:,25]
    Qall10= DATA[:,26]
    Qall11= DATA[:,27] 
    Qall12= DATA[:,28]
    Qall13= DATA[:,29] 
    Qall14= DATA[:,30] 
    Qall15= DATA[:,31]
    Qall16= DATA[:,32] 
    Qall17= DATA[:,33]
    Qall18= DATA[:,34] 
    Qall19= DATA[:,35] 
    Qall20= DATA[:,36]
    As05= DATA[:,37]
    As10= DATA[:,38]
    As11= DATA[:,39] 
    As12= DATA[:,40]
    As13= DATA[:,41] 
    As14= DATA[:,42] 
    As15= DATA[:,43]
    As16= DATA[:,44] 
    As17= DATA[:,45]
    As18= DATA[:,46] 
    As19= DATA[:,47] 
    As20= DATA[:,48]
    Aw05= DATA[:,49]
    Aw10= DATA[:,50]
    Aw11= DATA[:,51] 
    Aw12= DATA[:,52]
    Aw13= DATA[:,53] 
    Aw14= DATA[:,54] 
    Aw15= DATA[:,55]
    Aw16= DATA[:,56] 
    Aw17= DATA[:,57]
    Aw18= DATA[:,58] 
    Aw19= DATA[:,59] 
    Aw20= DATA[:,60]
    Aall05= DATA[:,61]
    Aall10= DATA[:,62]
    Aall11= DATA[:,63] 
    Aall12= DATA[:,64]
    Aall13= DATA[:,65] 
    Aall14= DATA[:,66] 
    Aall15= DATA[:,67]
    Aall16= DATA[:,68] 
    Aall17= DATA[:,69]
    Aall18= DATA[:,70] 
    Aall19= DATA[:,71] 
    Aall20= DATA[:,72]
    
    fname = os.path.basename(file_name)
    bname, ext =  os.path.splitext( fname )
    
    fpath=  "Fig5.png"
   
    fig, ax = plt.subplots(dpi=500, figsize=(4,3))   
    

    # blue
    cr=0/255
    cg=0/255
    cb=255/255
    s="05m"  
    plt.plot(tim,Qall05,label=s,color=(cr,cg,cb))
    
     # Red
    cr=255/255
    cg=0/255
    cb=0/255
    s="10m" 
    plt.plot(tim,Qall10,label=s,color=(cr,cg,cb))

    # Lime
    cr=0/255
    cg=255/255
    cb=0/255
    s="15m"  
    plt.plot(tim,Qall15,label=s,color=(cr,cg,cb))

    # Salmon
    cr=250/255
    cg=128/255
    cb=114/255
    # cr=80/255
    # cg=80/255
    # cb=200/255
    s="20m"  #"In"
    plt.plot(tim,Qall20,label=s,color=(cr,cg,cb))



    plt.xlim(5,20)
    
    # plt.ylim(0,2.5)

    plt.minorticks_on()

    plt.savefig(fpath)

    plt.clf()
    plt.close()
