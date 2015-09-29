# Chromosome Territory Modeller and Viewer: User Manual

This document is a User Manual for Chromosome Territory Modeller (`ChroTeMo`) and Chromosome Territory Viewer (`ChroTeVi`).
The first one is intended to use when you want to create chromosome territory model for a specific species. It computes the parameters of modeled chromosomes, allows to preview the model and saves the results to a file. 

`ChroTeVi` is designed to be a viewer - it lets you to read files created by `ChroTeMo`, display,  zoom in and out, and rotate the created model. 

### Hardware and software requirements
Both scripts are written in Python. For visualization purposes we use VPython. 
Our scripts also use libraries: `Tkinter`, `tkFileDialog`, `time`, `random`, `gc`, `array` and `datetime`.

If you are using Linux, probably you have Python already installed.
See Python and libraries (`VPython`) documentation to learn how to install the necessary software. For links see the Appendix at the end of this manual.

Minimal hardware requirements are determined by requirements of Python and VPython. However, because of the visualisation probably it will be more comfortable if you have an additional graphics card - not only the one integrated with the mainboard.

### Testing software environment - loading and running scripts 
After downloading and installing necessary software and libraries you can test your environment.
For that purpose you should find icon for `VIDLE`
![vidle](http://i.imgur.com/6s7SjPy.jpg)
open testing script named `Test_Environment_Config.py` 

![open in vidle](http://i.imgur.com/hEU4N5b.jpg)
![testChoose](http://i.imgur.com/W10yKaD.jpg)

and run it

![Run test](http://i.imgur.com/kJwUrN8.jpg)

You should see a picture similiar to the one presented below.

![displayedTest](http://i.imgur.com/vCjkCf1.jpg)

When you press the right mouse button and move the mouse you should be able to rotate this picture. 

![Canvas Move ](http://i.imgur.com/BXam8bu.jpg)
With the use of the central mouse button you should be able to zoom the view in and out.

If you succeed, ChroTeMo and ChroTeVi should now run on your computer.

## Chromosome Territory Modeller
The purpose of ChroTeMo is to create a model of chromosome territories distribution.
Chromosome Territory Modeller (reffered later as ChroTeMo) is a file in repository with the name ChroTeMo_v.X.py, where where X denotes the number of version. 

When you have source code of script downloaded, you can either run or customize configuration of Chromosome Territory Modeller before run.


## Setting Up ChroTeMo parameters
In our model there are some parameters, which can help to tailor and tune up the code for the simulation of chromosome territories arrangement in different species. When adjusting the implementation for a given specie the following parameters can be set up.

To simulate the model of chromosome territories arrangement, you can set up the parameters  mentioned below to fit/tune the model to your needs. This can be done by direct editing of the script file. The parameters are listed at the beginning of the script file. 
***Be careful !!*** Some parameters may result in a long running time of `ChroTeMo` (when testing the parameter `multi` = 1000, the script ran for more than 3 weeks)!

If you are unsure about parameters, just change only species specific **(sp)** parameters. You can experiment with the rest of parameters (**(mv)** - model specific) later.

After changing the parameters you should save the modified file.

To change the parameters you should open file ChroTeMo source file. It can be done with any text editor, but it is more comfortable to use any supporting syntax colouring.

Basic parameters of the model are defined in lines from 22 to 36 in block:
```
  #************************* PROGRAM PARAMETERS - can be modified *******************************
    l_arm_c=[7,7,6,6,6,6,4,4,3,3] #length of chromosome's arm before decondensation, seperate by coma
    l_arm_d=[37,29,25,20,8,38,30,35,29,20] #length of chromosome's arm after decondensation, separeta by coma
    chr_pair=5 #number of chromosome pairs
    n_arm=2 #how many arms should be colored (1 or 2)
    n_chr=1 #which pair of chromosome sholud be colored - 0 if none
    n_chr_2=0 #second pair of chromosome which can be colored - 0 if none
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
  
 ```

Some parameters are used as "species specific" **(sp)**, some for model and visualisation **(mv)** purposes. The meaning of parameters is as follows:

* `chr_pair` - number (integer) of chromosome pairs **(sp)**. List in form `l_arm_c` = [1,2,3,4] means that 1st arm of 1st chromsome has length 1, 2nd arm of 1st chromosome has length 2, 1st arm of 2nd chromosome has length 3, 2nd arm of 2nd chromosome has length 4 **(sp)**; 
* `l_arm_c` - is a vector containing numbers (integers) representing length of chromome arms in condensed form. Length is counted in micrometers (the units are in micrometers: 1 domain = 0.5 micrometer). Quantity of entries should equals 2\*`chr_pairs` **(sp)**;
* `l_arm_d` - is a vector containing numbers (integer) representing length of chromome arms after decondensation. Here, length is counted in Mbps (mega basepairs). Quantity of entries should equals 2\*`chr_pairs` **(sp)**;
* `min_rad_nu` - this parameter represents minimal radius of nucleus, usually taken from experiments and/or from literature **(sp)**; ***Jaka jednostka?***
* `max_rad_nu` - this parameter represents maximal radius of nucleus, usually taken from experiments and/or from literature **(sp)**; ***Jaka jednostka?***
* `min_vol_no` - this parameter is to determine the maximum percentage of volume in nucleus occupied by nucleolus. Entry should be in range (0-1), where 0.05 means 5% and 0.15 means 15%. These values are taken from experimental results and/or from literature **(sp)**;
* `max_vol_no` - this parameter is to determine the minimal percentage of volume in nucleus occupied by nucleolus. Entry should be in range (0-1), where 0.05 means 5% and 0.15 means 15%. These values are taken from experimental results and/or from literature **(sp)**;
* `n_arm` - how many arms is to be coloured, you can choose either one (1) or two (2) **(mv)**;
* `n_chr` - which pair of chromosomes you want to colour. The number (integer) should be from range zero (0) and `chr_pair`. When you choose zero it means that you do not want to color any chromosome. **Note:** This does not have influence on model saved in file. This apply only to visualisation during model creation **(mv)**;
* `n_chr_2` - by setting up this parmeter you can choose second pair of chromosome you want to paint. See description of `n_chr` above **(mv)**;
* `rad_bed` - this parameters determines radius of beads representing domains. Teoretically there is no limitation of the number, but it is recommended to be reasonable in comparison of radius of nucleus for succesfull model creation **(mv)**;
* `eps_1` - this parameter determines minimal distance that have to be kept between beads in the same chromosome **(mv)**;
* `eps_2` - this parameter determines minimal distance that have to be kept between beads of different chromosomes. It is also used to determine minimal distance to be kept between beads and walls of nucleus and nucleolus. It is recommended that eps_1<eps_2 **(mv)**;
* `trsp` - this parameter determines transparency ranges (0,1). Value 0 for total transparency - object is not visible, 1 when there is no transparency **(mv)**;
* `multi` - When you want to achieve more precise and detailed model of chromosome territory through more accurate impletion you can us this parameter. By default `multi`=1 what means that one bead is one domain. When you want fulfill space faithfully and with better accuracy (this can lead to more complicated shapes) you can increase this value. For example `multi`=4 means that one domain will be represented by 4 spheres, `multi`=10 means that one domain will be represented as 10 spheres. ***Warning! Increasing this parameter leads to significant growth of computational time necessary for model creation.*** **(mv)**; 




### ChroTeMo functions

•	`nucleus()` The purpose of this function is to create the nucleus. The nucleus is represented by a sphere , with the coordinates of the center `(x_nu, y_nu, z_nu)` = (0, 0, 0), and with the radius *R* generated in a random way from the interval < `min_rad_nu`, `max_rad_nu` >;

•	`nucleolus()` This function is used to generate the nucleolus. In the first step the radius of nucleolus *r* is determined using parameters `min_vol_no` and `max_vol_no`;

•	`centromere()` This function is responsible for generating the coordinates of the centromere bead centres (for all chromosomes);

•	`bead()` This function is used to draw all new domains of all chromosomes. The input parameters for this function are domain coordinates, colour (RGB colour defined as a separate degree of saturation for each component), and transparency. At the initial stage of the modelling process  this function is also responsible for drawing centromeres as spheres;

•	`new_domain()` This function generates the coordinates of the new domain. 
For domains that are drawn during building the condensed chromosomes, the new coordinates are generated based on previously, last generated coordinates (within the domain of the same arm). 
For the domains that are drawn in the phase of chromatin decondensation, the coordinates of the next domain are determined on the basis of a randomly selected domain (referred to as a precursory domain) from all previously generated domains that constitute chromosome arms;

•	`dist_bead()` This function is used to check whether the newly created domain does not collide with another domain within the same chromosome. The same function is also used to check whether there is not a collision with another domain within another chromosome. The only difference is in ε parameter – here ε2 (which is greater than ε1) is used;

•	`dist_precurs()` The last step in each iteration is to verify that the newly generated domain is located at a suitable distance from the precursory domain.

If this condition is true, the program return to the function `new_domain()`;





## Running ChroTeMo

Open file `ChroTeMo` with VIDLE in similiar way as described in "Testing Software Environment".
ChroTeMo can work in a half-batch mode: you can generate a few to a dozen models with one run.

In the beginning the first (and last) question appears: "How many results do you want?" You should write any reasonable (in the meaning of computational time) number denoted the number of models to be created.  
All you have to do is to run script. It can be done in the same way as described above, when testing software environment.
Wait a while and ... enjoy your model!

When you close ChroTeMo, windows with visualisation will close, but the file with elements describing model remains in working directory. Files have names with convention: `workfile + data + time.txt`. 
They can be used as input files for ChroTeVi

## Using ChroTeVi
Load ChroTeVi script with VIDLE as mentioned above. Run it in the same way as previously. 
Then you will be asked to point to file generated by ChroTeMo.
 
Then, you will be asked some questions:

1. Which pair of chromosomes you want to paint. You should write digits denoting pairs to be painted. If you  want to paint only one pair - your second answer should be 0 (zero).
2. The degree of transparency for the rest of beads in range from 0 to 1, when 0 means full transparency (beads will be invisible), 1 meand no transparency.
3. If you want to color only one pair of chromosome (answer to second question is zero), then here you can choose whether you want to paint entire chomosome or each arm of chromosome.

Now you should be able to view generated model. 
With the use of mouse buttons and scroll you should be able to zoom in, zoom out and rotate model.

  
That's all.
Enjoy!


# Appendix A
1. Python download and installation: https://wiki.python.org/moin/BeginnersGuide/Download
2. VPython download and documentation: http://vpython.org/

