#sel 1 net v
#sel 0 net w
from random import randint
from math import *
import time
from JST_data import get

import matplotlib.pyplot as plt
import numpy as np

def akt(x):
    fx = (1/(1+exp(-x)))
    return fx
########################################## FORWARD ##########################################
def net(vnet,vin,sel):
    jum = 0
    out_net = 0
    out_net_val = []
    if sel == 1:
        a = jum_hid_layer
        b = jum_input
    elif sel == 0:
        a = jum_output
        b = jum_hid_layer
    for i in range (a):
        out_sum_net = 0
        for k in range (b):
            out_sum_net = out_sum_net + vin[k]*vnet[i][k+1]
        
        out_net = vnet[i][0] + out_sum_net
        out_net_val.append(out_net)
    return out_net_val

def bobot(x,sel):
    hasil = []
    if sel == 1:
        a = jum_hid_layer
    elif sel == 0:
        a = jum_output
    for i in range (a):
        hasil.append(akt(x[i]))
    return hasil
########################################## FORWARD ##########################################
######################################## BACKRWARD ########################################
def new_w(a,t,y,z,w):
    d = []
    nnw = []
    loss = []
    for i in range (jum_output):
        n_w = []
        loss.append((t[i] - y[i])**2)
        d.append((t[i] - y[i])*y[i]*(1- y[i]))
        n_w.append(a*d[i])
        for j in range (jum_hid_layer):
            n_w.append(a*d[i]*z[j])
        nnw.append(n_w)
    ms = sum(loss)/len(loss)
    rms = sqrt(ms)
    return nnw,d,rms

def new_v(a,dk,w,x,z):
    d_net = 0
    
    n_v = []
    for j in range (jum_hid_layer):
        nnv=[]
        for k in range (jum_output):
            d_net = ((dk[k]*w[k][j+1])*z[j]*(1-z[j]))
            nnv.append(d_net*a)
            for i in range(jum_input):
                nnv.append(d_net*a*x[i])
        n_v.append(nnv)
    return n_v
        
def up_w(w,dw):
    hasil = []
    for i in range (jum_output):
        ha = []
        ha.append(w[i][0]+dw[i][0])
        for j in range(jum_hid_layer):
            ha.append(w[i][j+1]+dw[i][j+1])
        hasil.append(ha)
    return hasil

def up_v(v,dv):
    hasil = []
    for i in range (jum_hid_layer):
        ha = []
        ha.append(v[i][0]+dv[i][0])
        for j in range(jum_input):
            ha.append(v[i][j+1]+dv[i][j+1])
        hasil.append(ha)
    return hasil
        
            

######################################## BACKRWARD ########################################
millis = lambda : time.time() * 1000

def proses():
    global jum_input,jum_hid_layer,jum_output
##    global val_w,val_v,val_x
    dk = []
    target  = []
    val_x = []
    val_x,target = get()
##    print(val_x,target)
    val_z = []
    val_y = []
    val_v = []
    val_w = []
    d_w = [[]]
    d_v = [[]]

    rms = []
    xrms = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000]

    jum_input = 63;
    jum_hid_layer =45;
    jum_output = 3;
    jum_data = 15

    for i in range (jum_hid_layer):
        v = []
        for j in range(jum_input+1):
            v.append((randint(-100,100)/100))
        val_v.append(v)

    for i in range (jum_output):
        w = []
        for j in range(jum_hid_layer+1):
            w.append((randint(-100,100)/100))
        val_w.append(w)

    lr = 0.1
    t1 = millis()
    t3 = millis()
    interval = 1000
##    hasil = 1
##    epoh = 0
##    while (hasil>0.0003):
    for epoh in range(1000):
##        print(epoh)
##        epoh +=1 
        if((epoh+1)%10 == 0):
            print(f'epoch {epoh+1} dengan loss {loss}') 
            rms.append(loss)
        for jx in range (jum_data):
            t4 = millis()
            
            if (t4-t3 > interval):
                # print(epoh)
                # print(f'epoch {epoh} dengan loss {loss}')
                t3 = t4
            val_z = bobot(net(val_v,val_x[jx],1),1)
            val_y =bobot(net(val_w,val_z,0),0)
            
            d_w,dk,loss=new_w(lr,target[jx],val_y,val_z,val_w)
            # print(f'epoch {epoh} dengan loss {loss}')
            d_v = new_v(lr,dk,val_w,val_x[jx],val_z)
            
            val_w = up_w(val_w,d_w)
            val_v = up_v(val_v,d_v)
##            z = []
##            z = bobot(net(val_v,val_x[jx],1),1)s
##            a_list = (bobot(net(val_w,z,0),0))
##            hasil = 0
##            for i in range (jum_output):
##                hasil = hasil + (target[jx][i]-a_list[i])**2
##            print(hasil)
##            time.sleep(0.5)
##    print('v= ',val_v)
##    print('w= ',val_w)
    t2 = millis()
    waktu = ((t2-t1)/1000)
    print(waktu)
    nprms = np.array(rms)
    npxrms = np.array(xrms)
    plt.plot(npxrms, nprms)
    plt.show()
    return(val_v,val_w,waktu)
            
   
    

