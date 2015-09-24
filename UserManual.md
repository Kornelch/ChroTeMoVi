# Chromosome Territory Modeller and Viewer: User Manual

This document is a User Manual for Chromosome Territory Modeller (`ChroTeMo`) and Chromosome Territory Viewer (`ChroTeVi`).
The first one is intended to use when you want to create chromosome territory model for specific species. It computes parameters of modelled chromosomes, allows to preview model and save results to file. Bacause all computations are done by `ChroTeMo`, it works some time.

The second is designed to be a viewer - it let you to read file created by `ChroTeMo`, display, rotate, zoom in and out created model. Because it works on ready model it is also faster in use.

### Hardware and software requirements
Both scripts are written in Python. For visualisation purposes we use VPython. 
Our scripts also use libraries: `Tkinter`, `tkFileDialog`, `time`, `random`, `gc`, `array` and `datetime`.

If you are using Linux, probably you have Python itself already installed.
See Python and libraries (`VPython`) documentation  about how to install necessary software. For links see Appendix at the end of this manual.

Minimal hardware requirements are determined by requirements of Python and VPython. Anyway, because of visualisation probably it will be more comfortable if you will have own graphics card - not only those integrated with mainboard.

### Testing software environment - loading and running scripts 
After downloading and installing necessary software and libraries you can test your environment.
For that purpose you should find icon for `VIDLE`
![vidle](http://i.imgur.com/6s7SjPy.jpg)
open testing script named `Test_Environment_Config.py` 

![open in vidle](http://i.imgur.com/hEU4N5b.jpg)
![testChoose](http://i.imgur.com/W10yKaD.jpg)

and run it

![Run test](http://i.imgur.com/kJwUrN8.jpg)

You should see a picture similiar to presented below.

![displayedTest](http://i.imgur.com/vCjkCf1.jpg)

When you press right mouse button and move mouse you should be able to rotate this picture. 

![Canvas Move ](http://i.imgur.com/BXam8bu.jpg)
With the use of central mouse botton you should be able to zoom in and zoom out.

If you succeed, you can go on. 
ChroTeMo and ChroTeVi should now run on your computer.

## Chromosome Territory Modeller
The purpose of ChroTeMo is to create model of chromosome territory.
ChroTeMo model nucleus and nucleolus as spheres with given radius. Chromatine domains are also represented as spheres (one domain = one sphere. It is possible to change ratio by using multiplication parameter. For details see full text of article).

### Variables in ChroTeMo
In our model there are some parameters, which can help to tailor and tune up the code for the simulation of chromosome territory arrangement in different species. When fitting implementation for a given purpose the following parameters can be set up  :
•	`chr_pair` – number of chromosomes pairs to be generated;
•	`l_arm_c` – table of length of the arms of a condensed chromosome;
•	`l_arm_d` – table of length of the arms of a decondensed chromosome;
•	`min_rad_nu` – the minimal radius of the nucleus;
•	`max_rad_nu` – the maximum radius of the nucleus;
•	`min_vol_no` – minimum volume of the nucleolus (expressed as percentage of nucleus  volume);
•	`max_vol_no` – maximum volume of the nucleolus (expressed as percentage of nucleus  volume);
•	`rad_bead` – rb, radius of a chromatin domain;
•	`col_pair` – a parameter informing which pair of chromosomes has to be colored (0 for none);
•	`col_arm` – a parameter informing how to colour the arms of the chromosome (if equals 1,  entire chromosome in displayed one color, if it equals 2, each arm of the chromosome is in different color);
•	`eps_1` – ɛ1, a parameter used in collision detection procedure: minimal distance required to another domain of the same chromosome; 
•	`eps_2` – ε2, a parameter used in collision detection procedure: minimal distance required to another domain of a different chromosome, also minimal distance from the boundaries of the nucleus and nucleolus;
•	`trsp` – a transparency parameter for chromosomes that are not coloured during modelling (1 – transparency off, 0 – chromosomes are not visible);
•	`multi` – multiplication: allows to increase the number of beads constituting one domain representation (1 domain = multi · 1 bead = multi · 1 sphere) . In the presented version of ChroTeMo, one domain is represented by one bead (multi = 1) and these two terms are used interchangeably in the latter parts of the text.
•	`xyz[]` - is an array where coordinates of centromeres are stored.


### ChroTeMo functions

•	`nucleus()` The purpose of this function is to create the nucleus. The nucleus is represented by a sphere , with the coordinates of the center `(x_nu, y_nu, z_nu)` = (0, 0, 0), and with the radius *R* generated in a random way from the interval < `min_rad_nu`, `max_rad_nu` >
•	`nucleolus()` This function is used to generate the nucleolus. In the first step the radius of nucleolus *r* is determined using parameters `min_vol_no` and `max_vol_no`.
•	`centromere()` This function is responsible for generating the coordinates of the centromere bead centres (for all chromosomes).
•	`bead()` This function is used to draw all new domains of all chromosomes. The input parameters for this function are domain coordinates, colour (RGB colour defined as a separate degree of saturation for each component), and transparency. At the initial stage of the modelling process  this function is also responsible for drawing centromeres as spheres.
•	`new_domain()` This function generates the coordinates of the new domain. 
For domains that are drawn during building the condensed chromosomes, the new coordinates are generated based on previously, last generated coordinates (within the domain of the same arm). 
For the domains that are drawn in the phase of chromatin decondensation, the coordinates of the next domain are determined on the basis of a randomly selected domain (referred to as a precursory domain) from all previously generated domains that constitute chromosome arms. 
•	`dist_bead()` This function is used to check whether the newly created domain does not collide with another domain within the same chromosome. The same function is also used to check whether there is not a collision with another domain within another chromosome. The only difference is in ε parameter – here ε2 (which is greater than ε1) is used. 
•	`dist_precurs()` The last step in each iteration is to verify that the newly generated domain is located at a suitable distance from the precursory domain. 
If this condition is true, the program return to the function `new_domain()`;


## Using ChroTeMo
To generate models of chromosome territory, you should set up mentioned above parameters to fit/tune model for your needs (species you examine). This can be done by direct editing script file. Parameters are listed at the beginning of the script file. 
***Be careful !!*** Some parameters may cause script - Modeler a long running time (with parameter `multi`= 1000 script runs when testing more than 3 weeks)!

If you are unsure about parameters, just change only species-specified parameters. You can experiment with the rest of parameters later.

After changing parameters you should save file (of course you can save file with different name).
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

