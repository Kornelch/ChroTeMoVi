#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2015  K. Chromiński, M. Tkacz, D. Idziak, E. Bread, R. Hasterok
#    when you used it please cite:    
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

itera=input("How many results do you want? \n")
for iteracje in range(0,itera):
    #**************************************************************************************************
    #Program description                                                                              *
    #Simulation of chromosome teritory                                                                *
    #licence: GPLv3                                                                       *
    #when you used it please cite: Plos ....                                                          *
    #**************************************************************************************************


    # -*- coding: cp1250 -*-
    from visual import *
    import time
    import random
    import gc
    from array import *
    
    import datetime

    ###############################################################################
    #************************* PROGRAM PARAMETERS - can be modified *******************************
    l_arm_c=[7,7,6,6,6,6,4,4,3,3] #length of chromosome's arm before decondensation, seperate by coma
    l_arm_d=[37,38,29,30,25,35,20,29,8,20] #length of chromosome's arm after decondensation, separeta by coma 
    chr_pair=5 #number of chromosome pairs
    min_rad_nu=6.8 #minimal radius of nucleus
    max_rad_nu=7 #maksimal radius of nucleus
    min_vol_no=0.05 #minimum occupancy of nucleus by nucleolus
    max_vol_no=0.15 #maksimum occupancy of nucleus by nucleolus
    rad_bead=0.5 #radius of beads
    eps_1=0.004 #admissible distance from the beads with the same chromosome
    eps_2=0.05 #admissible distance from the beads with diffrent chromosome
    trsp=1 #transparency of non-colore beads
    multi=1 #chromosome size multiplier

    #****************** END PROGRAM PARAMETERS *********************************

    #****************** variables in the program - DO NOT MODIFY WITHOUT UNDERSTANDING THE CODE *****************************
    licznik=0
    par_12=0.95
    lb_ram=2
    x_nu=0
    y_nu=0
    z_nu=0
    multi=int(multi)
    if multi>1:
        l_arm_c = [x * multi for x in l_arm_c]
        l_arm_d = [x * multi for x in l_arm_d]
        if multi<4:
            rad_bead = rad_bead/multi
        else:
            rad_bead = rad_bead/(multi/4)
    if multi<1:
        print("Warning: multi must be greater than 1 ")
    tab = [[0 for col in range(90000)] for row in range(10)] #the array to save the coordinate of centers of Domains
    ind=(chr_pair*4)-1
    #the array for storing coordinates of the points
    xyz = [[0 for col in range(chr_pair*4)] for row in range(4)]
    #the array to write the length of chromosomes before dekondensation
    l_ch=[0 for col in range(chr_pair*4)]
    #program parameter
    fk=0
    for ft in range(0,2*chr_pair,2):
        fh=ft+(chr_pair*2)
        l_ch[ft]=l_ch[ft+1]=l_arm_c[fk]
        fk=fk+1
        l_ch[fh]=l_ch[fh+1]=l_arm_c[fk]
        fk=fk+1
    
    
    #the array of arms length
    l_ram=[0 for col in range (chr_pair*4)]
    
    fk=0
    for ft in range(0,2*chr_pair,2):
        fx=ft+(chr_pair*2)
        l_ram[ft]=l_ram[ft+1]=l_arm_d[fk]
        fk=fk+1
        l_ram[fx]=l_ram[fx+1]=l_arm_d[fk]
        fk=fk+1
    #print(l_ram)
  


    
    kr = [0 for col in range(chr_pair*4)] #the array of chromosomes length - a counter for length



    
    ty=[0 for col in range(chr_pair*4)]


    #the array of colors and transparency of domains
    k_kol=[[0 for col in range(4)] for row in range(chr_pair*4)]
    for re in range(0, chr_pair*4):
            for re_2 in range (0,3):
                k_kol[re][re_2]=1
            k_kol[re][3]=trsp

                
            
    
    #****************** END variables in the program **********************************

    #Writing parameters to the file
    date_time_str = datetime.datetime.now().strftime('%d-%m-%Y_%H^%M^%S')
    plik="workfile "+date_time_str+".txt"
    f = open(plik, 'w')
    f.write(str(rad_bead))
    f.write("\n")
    f.write(str(2*chr_pair))
    f.write("\n")

    for po in range(0,chr_pair*4):
        for po2 in range(0, 4):
            f.write(str(k_kol[po][po2]))
            f.write("\n")

    gc.collect()


    #generating nucleus
    def nucleus():
        global x_nu, y_nu, z_nu, r_nu, R
        R=round(random.uniform(min_rad_nu,max_rad_nu),5) 
        f.write(str(R))
        f.write("\n")
        x_s=0
        y_s=0
        z_s=0
        ball = sphere(pos=(x_nu,y_nu,z_nu), radius=R, material=materials.emissive, opacity=0.2)
    nucleus()

    #generating nucleolus
    def nucleolus():
        global x_j, y_j, z_j, r_j, R
        r_s5=(max_vol_no*(R**(3)))**(1/3.0)
        r_s30=(max_vol_no*(R**(3)))**(1/3.0)
    
        r_j=round(random.uniform(r_s5, r_s30),3) #generate the size of the nucleolus
    
        #generate the position of the nucleolus
        t=True
        while (t==True):
            x_j=round(random.uniform((x_nu-(R-r_j-1)),(x_nu+(R-r_j-2))),5)
            y_j=round(random.uniform((y_nu-(R-r_j-1)),(y_nu+(R-r_j-2))),5)
            z_j=round(random.uniform((z_nu-(R-r_j-1)),(z_nu+(R-r_j-2))),5)
            if (sqrt((x_j-0)**2+(y_j)**2+z_j**2)<(R-r_j-eps_2)):
                t=False

    nucleolus()
    f.write(str(x_j))
    f.write("\n")
    f.write(str(y_j))
    f.write("\n")
    f.write(str(z_j))
    f.write("\n")
    f.write(str(r_j))
    f.write("\n")
    ball_2 = sphere(pos=(x_j,y_j,z_j), radius=r_j, color=color.orange, opacity=1)
    
    gc.collect()

    

    
    kol_1=1
    kol_2=0.5
    dfg=0
    #function responsible for generating domains
    def bead(x_1, y_1, z_1, k1, k2, k3, k4):
        global dfg
        dfg=dfg+1
        kul = sphere(pos=(x_1,y_1,z_1), radius=rad_bead, color=(k1, k2, k3), opacity=k4)
         
        

    gc.collect()


    #***************************** Function in program ***************************************


    #function to check the output of the nucleus
    def is_in_nu(nr_k):
        global ind
        global L
        global H
        global W
        global tab
        global k
        global xyz
        global r_s, rad_bead
        
        if (((R-rad_bead-eps_2)>sqrt((xyz[0][nr_k])**2+(xyz[1][nr_k])**2+(xyz[2][nr_k])**2))):
            ind=ind+1
            tab[0][ind]=nr_k #save number of domain
            tab[1][ind]=xyz[0][nr_k]
            tab[2][ind]=xyz[1][nr_k]
            tab[3][ind]=xyz[2][nr_k]
            k=1
        else:
            xyz[0][nr_k]=x
            xyz[1][nr_k]=y
            xyz[2][nr_k]=z
            k=0
    #function to generate starting points - centromeres
    def centromere():
        
        global xyz, R, rad_bead, x_j, y_j, z_j
        for i in range (0,chr_pair*2):
            ij=i+(chr_pair*2)
            #print("i: ",i)
            spr=0
            while(spr==0):
                
                #generate x
                xyz[0][i]=round(random.uniform((-R+4*rad_bead),(R-4*rad_bead)),5)
                xyz[0][ij]=xyz[0][i]
                tab[0][i]=i
                tab[0][ij]=ij
                tab[1][i]=xyz[0][i]
                tab[1][ij]=xyz[0][i]
                #generate y
                xyz[1][i]=round(random.uniform((-R+4*rad_bead),(R-4*rad_bead)),5)
                xyz[1][ij]=xyz[1][i]
                tab[2][i]=xyz[1][i]
                tab[2][ij]=xyz[1][i]
                #generate z
                xyz[2][i]=round(random.uniform((-R+4*rad_bead),(R-4*rad_bead)),5)
                xyz[2][ij]=xyz[2][i]
                tab[3][i]=xyz[2][i]
                tab[3][ij]=xyz[2][i]
                
            
                if (i>0):
                    if (sqrt((xyz[0][i]-x_j)**2+(xyz[1][i]-y_j)**2+(xyz[2][i]-z_j)**2)>(r_j+rad_bead+2*eps_2)):
                        if (sqrt((xyz[0][i])**2+(xyz[1][i])**2+(xyz[2][i])**2)<(R-(rad_bead+5*eps_2))):
                            for j in range (0,i):
                                if (sqrt((xyz[0][i]-xyz[0][j])**2+(xyz[1][i]-xyz[1][j])**2+(xyz[2][i]-xyz[2][j])**2)>(2*rad_bead+2*eps_2)):
                                    spr=spr+1
                            if (spr>(i-2)):
                                spr=1
                                break
                                spr=1
                else:
                    if (sqrt((xyz[0][i]-x_nu)**2+(xyz[1][i]-y_nu)**2+(xyz[2][i]-z_nu)**2)<(R-(rad_bead+4*eps_2))):
                        if (sqrt((xyz[0][i]-x_j)**2+(xyz[1][i]-y_j)**2+(xyz[2][i]-z_j)**2)>(r_j+rad_bead+2*eps_2)):
                            spr=1
                            break
            


                        
    #function to generate the direction of moving for the new domain
    def new_domain(nr_k_2):
        
        global xyz
        for i in range (0,3):
            
            znak=bool(random.getrandbits(1))
            if znak==True:
                xyz[i][nr_k_2]=xyz[i][nr_k_2]+round(random.uniform(0, 2*rad_bead+2*eps_1),5)
            else:
                xyz[i][nr_k_2]=xyz[i][nr_k_2]-round(random.uniform(0, 2*rad_bead+2*eps_1),5)

    def is_out_no():
        global xyz, nr_k, x_j, pot, k_1, r_j, r_k, k, eps_2
        
        if (sqrt((xyz[0][nr_k]-x_j)**2+(xyz[1][nr_k]-y_j)**2+(xyz[2][nr_k]-z_j)**2)<(r_j+rad_bead+eps_2)):
            pot=1
            xyz[0][nr_k]=x
            xyz[1][nr_k]=y
            xyz[2][nr_k]=z
            k=0
            
    def dist_bead(): 
        global xyz, nr_k, ind, tab, eps_1, eps_2, x, y ,z,k, k_3
        for df in range (0, ind+1):
            if (df != k_3):
                if (tab[0][df]==nr_k or (tab[0][df]==nr_k+(chr_pair*2) and nr_k< (chr_pair*2)) or (tab[0][df]==nr_k-(chr_pair*2) and nr_k>(chr_pair*2-1))):
                    
                    if (sqrt((xyz[0][nr_k]-tab[1][df])**2+(xyz[1][nr_k]-tab[2][df])**2+(xyz[2][nr_k]-tab[3][df])**2)<(2*rad_bead-2*eps_1)):
                        
                        pot=1
                        xyz[0][nr_k]=x
                        xyz[1][nr_k]=y
                        xyz[2][nr_k]=z
                        k=0
                        
                        break
                else:
                    if (sqrt((xyz[0][nr_k]-tab[1][df])**2+(xyz[1][nr_k]-tab[2][df])**2+(xyz[2][nr_k]-tab[3][df])**2)<(2*rad_bead+eps_2)):
                        
                        pot=1
                        xyz[0][nr_k]=x
                        xyz[1][nr_k]=y
                        xyz[2][nr_k]=z
                        k=0
                        
                        break 
    def dist_precurs():
        global xyz, nr_k, k_1, z, y, z, epx_1, eps_2, k
        if (((2*rad_bead-eps_1) >  sqrt((xyz[0][nr_k]-x)**2+(xyz[1][nr_k]-y)**2+(xyz[2][nr_k]-z)**2)) or ((2*rad_bead+eps_1) <  sqrt((xyz[0][nr_k]-x)**2+(xyz[1][nr_k]-y)**2+(xyz[2][nr_k]-z)**2))):
            
            xyz[0][nr_k]=x
            xyz[1][nr_k]=y
            xyz[2][nr_k]=z
            k=0
            
        
    def bead_generate(nr_k_1, ty, dl_ch):
        global licznik
        global nr_k
        global y
        global x
        global z
        global xyz
        global k
        global k_1
        global k_2
        global k_3
        global tab
        global rad_bead
        global eps_1
        global eps_2
        global ind
        global k_3
        
        
        nr_k=nr_k_1
        k=0
        k_1=0
        k_2=0
        k_3=ind+1
        while (k==0):
            k=1
            k_1=k_1+1
            k_2=0
            
            if (ty>dl_ch or k_1>1000):
                
                while (k_2==0):
                    k_3=random.randrange(ind)
                    if (tab[0][k_3]==nr_k):
                        xyz[0][nr_k]=tab[1][k_3]
                        xyz[1][nr_k]=tab[2][k_3]
                        xyz[2][nr_k]=tab[3][k_3]
                        k_2=1
                
            x=xyz[0][nr_k]
            y=xyz[1][nr_k]
            z=xyz[2][nr_k]
            
            global pot
            pot=0
            new_domain(nr_k)
            
            licznik=licznik+1
            dist_bead()    
            is_out_no()
                
            dist_precurs()
            if (k==1):
                is_in_nu(nr_k)
           
    # ********************************* END Function *****************************************************

    # ********************************* Program Begin **************************************************
    print("RUN...")
    centromere() 

    for i in range (0,max(l_arm_d)+1):
        print('checking '+str(i))
        rate(5)
        for n_i in range (0, (4*chr_pair)): #generate all chromosome
            if (kr[n_i]<l_ram[n_i]): #until kr =  length of chromose
                
                bead(xyz[0][n_i],xyz[1][n_i],xyz[2][n_i],k_kol[n_i][0],k_kol[n_i][1], k_kol[n_i][2], k_kol[n_i][3]) 
                kr[n_i]=kr[n_i]+1 
                bead_generate(n_i,ty[n_i],l_ch[n_i]) 
                ty[n_i]=ty[n_i]+1 
    f.write(str(ind+1))
    f.write("\n")
    for i in range(0, ind+1):
        for iu in range(0,4):
            f.write(str(tab[iu][i]))
            f.write("\n")

    f.close()  
    print("FINISH")
