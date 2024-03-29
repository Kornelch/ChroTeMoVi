#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
#    2016  M. Tkacz, K. Chromiński, D. Idziak, E. Robaszkiewicz, R. Hasterok
#    if you find this useful, please cite:  
#    Tkacz MA, Chromiński K, Idziak-Helmcke D, Robaszkiewicz E, Hasterok R (2016) 
#    Chromosome Territory Modeller and Viewer. PLoS ONE 11(8): e0160303. doi:10.1371/journal.pone.0160303
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#print("===================================================================")
#print (""" This code is licensed under GPLv3 license          """)
#print("===================================================================")

print("Please select file with generated model (ChroTeMo output): ")

# reading libraries
import Tkinter, tkFileDialog
from visual import *
import time
import random
import gc
from array import *

l=0

# GUI elements
root = Tkinter.Tk()
root.withdraw()
self = tkFileDialog.askopenfilename()

# opeing and parsing file generated by Modeller (ChroTeMo)
f = open(self,"r")
r_k=float(f.readline())
l=l+1
ite=int(f.readline())
l=l+1
k_kol=[[0 for col in range(4)] for row in range(4*ite+1)]
for po in range (0,4*(ite/2)):
    for po2 in range (0,4):
        k_kol[po][po2]=float(f.readline())
        l=l+1
r_s=float(f.readline())
l=l+1
x_j=float(f.readline())
l=l+1
y_j=float(f.readline())
l=l+1
z_j=float(f.readline())
l=l+1
r_j=float(f.readline())
l=l+1

ind=int(f.readline())
tab = [[0 for col in range(ind+2)] for row in range(10)]

l=l+1
licz=0
odcz=1
i=0
while odcz==1:
    
    licz=licz+1
    tym=str(f.readline())
    if tym=='': break
    tab[0][i]=int(tym)
    l=l+1
    tab[1][i]=float(f.readline())
    l=l+1
    tab[2][i]=float(f.readline())
    l=l+1
    tab[3][i]=float(f.readline())
    
    l=l+1
    i=i+1

for re in range(0, 4*ite):
            for re_2 in range (0,4):
                k_kol[re][re_2]=1

print("-----------------------------------------------------------------")

print("Set pairs of chromosomes to be painted"+"\n")
a=input("Enter number of first pair to be painted \n")
b=input("Enter number of second pair to be painted (0 if none) \n")


print("Set transparency for remaining beads (from not painted pairs), range 0 - 1 \n")
prz=input("0 - beads invisible, 1 - no transparency \n")

#pb=3
# Setting transparency for beads
for p in range(0,4*ite):
    k_kol[p][3]=prz

# Displaying information about colors of chromosomes or arms, and setting colors
if (a>0 and b==0):
    # chromosom a, jeden z pary, rami? krotsze ma kolor
    print("If only one pair is to be painted, certain chromosome in pair is denoted with digit_A and digit_B"+"\n")
    print(" shorter arm in "+str(a)+"_A "+"will be painted as dark green ")
    print(" longer arm in "+str(a)+"_A"+" will be painted as dark red ")
    print(" shorter arm in "+str(a)+"_B"+ " will be painted as light green ")
    print(" longer arm in "+str(a)+"_B"+ " will be painted as light orange ")
    if (a==1):
        a=0
    if (a==2):
        a=2
    if (a==3):
        a=4
    else:
        if (a==4):
            a=6

    if (a==5):
        a=8
    c=a+1
    d=a+ite
    e=d+1
# color settings
    k_kol[a][0]=0.0
    k_kol[a][1]=0.1
    k_kol[a][2]=0
    k_kol[a][3]=1
    k_kol[c][0]=0.12
    k_kol[c][1]=0.55
    k_kol[c][2]=0.1
    k_kol[c][3]=1
    k_kol[d][0]=0.56
    k_kol[d][1]=0.14
    k_kol[d][2]=0.14
    k_kol[d][3]=1
    k_kol[e][0]=1
    k_kol[e][1]=0.54
    k_kol[e][2]=0
    k_kol[e][3]=1

if (b>0):
    print(" 1st chromosome from "+ str(a) + " pair will be in dark green")
    print(" 2nd chromosome from "+ str(a) +" pair will be in light green")
    print(" 1st chromosome from "+ str(b) +" pair will be in dark red")
    print(" 2nd chromosome from "+ str(b) +" pair will be in light orange")
    if (a==1):
        a=0
    if (a==2):
        a=2
    if (a==3):
        a=4
    else:
        if (a==4):
            a=6
    if (a==5):
        a=8
    c=a+1
    d=a+ite
    e=d+1
# color settings
    k_kol[a][0]=k_kol[d][0]=0.0
    k_kol[a][1]=k_kol[d][1]=0.1
    k_kol[a][2]=k_kol[d][2]=0
    k_kol[a][3]=k_kol[d][3]=1
    k_kol[c][0]=k_kol[e][0]=0.12
    k_kol[c][1]=k_kol[e][1]=0.55
    k_kol[c][2]=k_kol[e][2]=0.1
    k_kol[c][3]=k_kol[e][3]=1

    if (b==1):
        b=0
    if (b==2):
        b=2
    if (b==3):
        b=4
    else:
        if (b==4):
            b=6
        if (b==5):
            b=8
    b_1=b+1
    b_2=b+ite
    b_3=b_2+1

# colors settings
    k_kol[b_2][0]=k_kol[b][0]=0.56
    k_kol[b_2][1]=k_kol[b][1]=0.14
    k_kol[b_2][2]=k_kol[b][2]=0.14
    k_kol[b_2][3]=k_kol[b][3]=1
    k_kol[b_3][0]=k_kol[b_1][0]=1
    k_kol[b_3][1]=k_kol[b_1][1]=0.54
    k_kol[b_3][2]=k_kol[b_1][2]=0
    k_kol[b_3][3]=k_kol[b_1][3]=1

# Model drawing
ball = sphere(pos=(0,0,0), radius=r_s, material=materials.emissive, opacity=0.2)
ball_2 = sphere(pos=(x_j,y_j,z_j), radius=r_j, color=(0.9,0.81,0.6), opacity=1)
for z in range (0, licz):
    kul=sphere(pos=(tab[1][z],tab[2][z], tab[3][z]), radius=r_k, color=(k_kol[tab[0][z]][0],k_kol[tab[0][z]][1],k_kol[tab[0][z]][2]), opacity=k_kol[tab[0][z]][3])

# Closing the file
f.close()

