**Authors:** Magdalena Tkacz, Kornel Chrominski, Dominika Idziak - Helmcke, Ewa Robaszkiewicz, Robert Hasterok

***If you find our script useful please support us and cite:  
Tkacz MA, Chromiński K, Idziak-Helmcke D, Robaszkiewicz E, Hasterok R (2016) 
Chromosome Territory Modeller and Viewer. PLoS ONE 11(8): e0160303. doi:10.1371/journal.pone.0160303***

**This document is licensed under CC BY-NC-SA 4.0**


*The most recent version of User Manual is located in [github repository](https://github.com/Kornelch/ChroTeMoVi/blob/master/UserManual.md)*


# Chromosome Territory Modeller and Viewer: User Manual

This document is a User Manual for Chromosome Territory Modeller (`ChroTeMo`) and Chromosome Territory Viewer (`ChroTeVi`).
The first one is intended to use when you want to create chromosome territory model for a specific species. It computes the parameters of modeled chromosomes, allows to preview the model and saves the results to a file. 

`ChroTeVi` is designed to be a viewer - it lets you to read files created by `ChroTeMo`, display,  zoom in and out, and rotate the created model. 

### Hardware and software requirements
Both scripts are written in Python. For visualization purposes we use VPython. 
Our scripts also use libraries: `Tkinter`, `tkFileDialog`, `time`, `random`, `gc`, `array` and `datetime`.

Scripts has been tested to run on:
* Windows 7, Windows 8, Windows 8.1 64 bit with Python 2.7.9 and VPython 2.7-6.11
* MacOS 10.11.3, Python 2.7.11 and Vpython 2.7-6.11
* Debian-based distribution (Debian 8.3 and LMDE2) with default Python interpreter (Python 2.7.9 [GCC4.9.2] and `python-visual` package, accessible directly via `apt-get` from debian repository mirrors.

If you are using Linux, probably you have Python already installed.
See [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and libraries [VPython](http://vpython.org/) documentation to learn how to install the necessary software or to section "Notes for Linux users" below.
Installation for Mac OS users are described in "Notes for Mac users" section.

Minimal hardware requirements are determined by requirements of Python and VPython. However, because of the visualisation, probably it will be more comfortable if you have an additional graphics card - not only the one integrated with the mainboard.

## Downloading ChroTe Suite

Source code and other files (ReadMe, UserManual, SatelliteArticles) are located in Github repository.

To download files from Github, clone repository, or navigate to the address https://github.com/Kornelch/ChroTeMoVi and download archive - see picture below.
![](http://i.imgur.com/LH2b8RH.jpg)

In fact, if you want only use scripts, you only need scripts located in ***_ChroTeMoVi_suite_latest*** folder.

If you do not know Git and/or want to learn more about Git you can take a [15 minutes course from Code School](https://try.github.io/levels/1/challenges/1 "CodeSchoolGit"), take a look at this short [tutorial](http://rogerdudler.github.io/git-guide/ "gitguide") or read more at [TutorialsPoint](http://www.tutorialspoint.com/git/git_basic_concepts.htm "tutorialspointGit").
If you rather prefer to watch than read, you can watch [this](https://www.youtube.com/watch?v=Fwdg8-thBAc "git webinar") webinar about Git and version control.

##Python and Visual Python Library Installation
Installation slightly differs in different operating systems, so below you can find information concerning particular systems.

### Notes for Windows Users
First, download and install Python and VPython. Steps are described [here](http://vpython.org/contents/download_windows.html "installationWin").

Pay attention to use `VIDLE`, not usual `IDLE`.

After downloading and installing necessary software and libraries you can test your environment.
To do that, you should find icon for `VIDLE`,
![](http://i.imgur.com/WieQreC.jpg)

open testing script named `Test_Environment_Config.py`:

![](http://i.imgur.com/aKdCs6e.jpg)

![](http://i.imgur.com/yMgptMg.jpg)

and run it

![](http://i.imgur.com/Jv9V2e7.jpg)

You should see a picture similar to the one presented below.

![](http://i.imgur.com/Of6tYBA.jpg)

When you press the right mouse button and move the mouse you should be able to rotate this picture. 

![](http://i.imgur.com/4PIurD6.jpg)

With the use of the central mouse button you should be able to zoom the view in and out.

If you succeed, ChroTeMo and ChroTeVi should now run on your computer.

### Notes for Linux Users
If you are an advanced Linux user, see "In short" section at the end of this section.


Our application does not use any sophisticated parameters from VPython, so it should work on the old library, accessible in default Linux package systems and default repositories. According to [Vpython webpage](http://vpython.org/contents/download_linux.html) it is recommended to use the newest version, but it requires more effort: either run through Wine or build from the source. This should change in the [near future](http://vpython.org/contents/announcements/evolution.html  "future") when VPython will use WebGL or [Jupyter notebooks](http://jupyter.org/ "Jupyter project").

We tested whether visual itself runs on Jupyter Notebook, and the result is shown below. However, we did not test ChroTe Suite in Jupyter notebooks yet.

![visual in Jupyter notebook](http://i.imgur.com/ZFJ4Llc.jpg)

In this manual we show how to run our scripts under Debian 8.3, default Python installation, and basic version of VPython.

![Debian and Python version](http://i.imgur.com/phDtv4Q.png)

You can check if you do not have python-visual library installed (as dependency of some other application). First, open the Terminal and call Python console (just type `python` and press Enter in Terminal). Then type `from visual import *` and press Enter. If you see error message, you need to install library, so follow further steps.

Before you start, make sure that your network connection is up and running. We  also assume that you have working Linux, capable for updating (`apt-get update`, `apt-get install`) and you are able to use ***Terminal***.


#### Installing Additional packages
Packages that are necessary to run scripts are: `python-visual` and `python-tk`.
Package `python-visual` is responsible for visualizing, package `python-tk` is responsible for displaying window in Viewer to allow choosing file with simulation results.
Installation is made using `apt-get`. When terminal type:
`sudo apt-get install python-visual` is opened, appropriate package is to be installed.

![python-visual install](http://i.imgur.com/e2I4TkB.png)

Accept installation. Then some packages are to be downloaded and configured.

When the installation is finished, run Python console and try to load `visual` module as presented below, typing in the Python console `from visual import *`

![TestingVisual](http://i.imgur.com/lOhcr7y.png)

Now, there should be no error message (notice the difference with previous visual import screendump). Then, try to draw a sphere: type `sphere(pos=(1,1,1), radius=1)` and press Enter (or use Test_Environment_Config.py if you have cloned the repository from git). You should see a picture of a sphere (or line of spheres - see testing environment section) in separate window. 

![](http://i.imgur.com/lTjeeNS.png)

If you have not used `tk` till now, there is only one step remaining to do - install `python-tk` for Viewer. You can do so by typing in terminal `sudo apt-get install python-tk` and install as `python-visual` previously.

If you succeed - that's it - your environment is ready to use our script!

#### Using ChroTe Suite Scripts

First, place the scripts in a place where you have appropriate rights for reading and writing. You can clone github repo typing `git clone https://github.com/Kornelch/ChroTeMoVi.git` in chosen directory. Usually home directory is a good choice (here, we placed directory 'ChroTe' in home directory of user named 'user'). Go to your catalog with the scripts (either in terminal or in Windows manager).

To run the scripts you have to grant permission for executing them. You can do this using `chmod`: type `chmod +x ChroTe*.py` for Modeller and `chmod +x Viewer*.py` for Viewer (or `chmod 755 script_name.py` if you prefer numbers for granting rights). 

![rights](http://i.imgur.com/AMu85iN.png)

Then, to run the script you should type `python script_name.py`.
That's all!

This is the Modeller in action:
![modeler](http://i.imgur.com/MIJr6xt.png)

And this is the Viewer:
![Viewer_in_action](http://i.imgur.com/4kI9AkH.png)

For detailed instruction for using ChroTe script suite see Sections for ChroTeMo and ChroTeVi.

Graphical windows can be closed by clicking cross mark in a top-right corner, console (if not closed) try press Ctrl+x.

***Note***: You can install both packages in one turn typing `sudo apt-get install python-visual python-tk`.


#### In Short

* Install packages `python-visual` and, if you do not have it yet, also `python-tk`,
* Test if you can import `visual` in Python console, then quit console,
* Download the script file(s) from Github webpage or clone [git repo](https://github.com/Kornelch/ChroTeMoVi.git "repository"),
* Set appropriate rights,
* Run script(s).

Enjoy!

### Notes for Mac OS Users
*Acknowledgement: We want to thank Damian Skipioł for checking installation and running of our scripts on MacOS.*

Testing environment was MacOS in version 10.11.3.

![MacOsVersion](http://i.imgur.com/0XBqlu8.png)

Installation has been made according instructions on [Visual Python webpage](https://www.python.org/downloads/release/python-2711/ "Vpython webpage") concerning MacOS.

On [this page](https://www.python.org/download/mac/tcltk/ "Mac-TclTk") you can find appropriate installers for your OS X version.

![choice for mac](http://i.imgur.com/M4ctddJ.jpg)

In our case Python 2.7.11 has been chosen. After downloading, install Python:

![MacPyInstall](http://i.imgur.com/Rgj9jTM.jpg)

After installation Python, the console should looks like in the following image

![pytest1](http://i.imgur.com/QNUO6Fg.png)

As you can see, there was a warning displayed, informing us that the current version of Tcl/Tk may be unstable. (If you do not see this warning, you can skip next few steps regarding Tcl/Tk installation).

Clicking on appropriate link seen on first screendump in this section (or in this sentence) you should be redirected to [Activestate  download page](http://www.activestate.com/activetcl/downloads "activetclDownload"), wher you can download Active Tcl package for your OS X. Download appropriate package and install it.

![ActiveTCL installation](http://i.imgur.com/uEKZLEE.png)

When succeed, you should see information similar to the following

![TCLSucceed](http://i.imgur.com/QdGPoPs.jpg)

Run again Python console, and check if there is still warning. If all is OK, you should see just clear console.
![python with tcl](http://i.imgur.com/2dD7K5l.png)

Notice that there is no warning.
You can try to use visual library .
Type in the Python console `from visual import *` and press Enter. Probably you do not have it, and you will see error message:

![MacVisualCheck](http://i.imgur.com/wV1Qr1o.jpg)

Close Python console.

So, we need to download and install Visual library (VPython-Mac-Py2.7-6.11 package) from [this](http://www.vpython.org/contents/download_mac.html "visual downloadMac") link.

Install downloaded package.

![installVisualMac](http://i.imgur.com/6OO6H20.png)

After installation open VIDLE-Py2.7 and type again `from visual import *` and press Enter.
You should see no error message this time. So type `sphere()` and press Enter. 
You should see window with sphere drawn as shown below.

![VisualMacSphere test](http://i.imgur.com/T0rUqnD.jpg)

Congratulations, it seems that you have Python with Visual up and running!.

Then you need files of ChroTe Suite. You can either download copy of repository in zip file via web browser or clone git repository.
Save files at location of your own choice. Then open VIDLE-Py2.7 and run `Test_Environment_Config.py` file from your location. you should see a line of beads:

![chroteTest](http://i.imgur.com/k8i0VTm.jpg)

If this succeeds, you should be able to run and use ChroTeMo or ChroTeVi (see next section).

![ChroTemoRun](http://i.imgur.com/ugWHmHT.jpg) 

and see steps of building a model

![ChrotemoRunGraph](http://i.imgur.com/sHoYD8A.jpg)

That's all. Enjoy!


## Chromosome Territory Modeller
The purpose of ChroTeMo is to create a model of chromosome territories distribution.
Chromosome Territory Modeller (reffered later as ChroTeMo) is a file in repository with the name ChroTeMo_v.X.py, where where X denotes the number of version. 

When you have source code of script downloaded, you can either run or customize configuration of Chromosome Territory Modeller before run.


### Setting Up ChroTeMo parameters
In our model there are some parameters, which can help to tailor and tune up the code for the simulation of chromosome territories arrangement in different species. When adjusting the implementation for a given specie the following parameters can be set up.

To simulate the model of chromosome territories arrangement, you can set up the parameters  mentioned below to fit/tune the model to your needs. This can be done by direct editing of the script file. The parameters are listed at the beginning of the script file. 
***Be careful !!*** Some parameters may result in a long running time of `ChroTeMo` (when testing the parameter `multi` = 1000, the script ran for more than 3 weeks)!

If you are unsure about parameters, just change only species specific **(sp)** parameters. You can experiment with the rest of parameters (**(mv)** - model specific) later.


To change the parameters you should open file ChroTeMo source file. It can be done with any text editor, but it is more comfortable to use any supporting syntax colouring. After changing the parameters you should save the modified file.

Basic parameters of the model are defined in lines from 45 to 57 in block:

    ```
    #************************* PROGRAM PARAMETERS - can be modified *******************************
    l_arm_c=[7,7,6,6,6,6,4,4,3,3] #length of chromosome's arm before decondensation, seperate by comma
    l_arm_d=[37,38,29,30,25,35,20,29,8,20] #length of chromosome's arm after decondensation, separeta by comma
    chr_pair=5 #number of chromosome pairs
    min_rad_nu=3.5 #minimal radius of nucleus
    max_rad_nu=3.7 #maksimal radius of nucleus
    min_vol_no=0.05 #minimum occupancy of nucleus by nucleolus
    max_vol_no=0.13 #maksimum occupancy of nucleus by nucleolus
    rad_bead=0.25 #radius of beads
    eps_1=0.004 #admissible distance from the beads with the same chromosome
    eps_2=0.05 #admissible distance from the beads with diffrent chromosome
    trsp=1 #transparency of non-colore beads
    multi=1 #chromosome size multiplier
    restart_after = 500000 #number of iterations made before restarting modeler
    #****************** END PROGRAM PARAMETERS *********************************
      
     ```

Some parameters are used as "species specific" **(sp)**, some for model and visualization **(mv)** purposes. The meaning of parameters is as follows:

* `chr_pair` - number (integer) of chromosome pairs **(sp)**. 
* `l_arm_c` - is a vector containing numbers (integers) representing length of chromome arms in condensed form. Length is counted in micrometers (the units are in micrometers: 1 domain = 0.5 micrometer). Quantity of entries should equals 2\*`chr_pairs`. List in form `l_arm_c` = [1,2,3,4] means that 1st arm of 1st chromosome has length 1, 2nd arm of 1st chromosome has length 2, 1st arm of 2nd chromosome has length 3, 2nd arm of 2nd chromosome has length 4 **(sp)**;
* `l_arm_d` - is a vector containing numbers (integer) representing length of chromosome arms after decondensation. Here, length is counted in Mbp (mega basepairs). Number of entries should equal 2\*`chr_pairs` **(sp)**;
* `min_rad_nu` - this parameter represents minimum radius of nucleus (calculated in micrometers), usually taken from experiments and/or from literature **(sp)**; 
* `max_rad_nu` - this parameter represents maximum radius of nucleus (calculated in micrometers), usually taken from experiments and/or from literature **(sp)**; 
* `min_vol_no` - this parameter is to determine the maximum percentage of nucleus volume occupied by nucleolus. Entry should be in range (0-1), where 0.05 means 5% and 0.15 means 15%. These values are taken from experimental results and/or from literature **(sp)**;
* `max_vol_no` - this parameter is to determine the minimum percentage of nucleus volume occupied by nucleolus. Entry should be in range (0-1), where 0.05 means 5% and 0.15 means 15%. These values are taken from experimental results and/or from literature **(sp)**;
* `rad_bead` - this parameters determines the radius of beads representing domains. Theoretically there is no limitation of the number, but it is recommended to be reasonable and take into account the radius of the nucleus for succesful model creation **(mv)**;
* `eps_1` - this parameter determines the minimum distance that have to be kept between the beads in the same chromosome **(mv)**;
* `eps_2` - this parameter determines the minimum distance that have to be kept between the beads of different chromosomes. It is also used to determine minimum distance to be kept between the beads and the boundaries of the nucleus and nucleolus. It is recommended that eps_1<eps_2 **(mv)**;
* `trsp` - this parameter determines transparency in a range (0,1). Choose 1 if you wish the transparency off, if you choose 0 the chromosomes will not be visible **(mv)**;
* `multi` - When you want to achieve more precise and detailed model of chromosome territories through more accurate impletion you can use this parameter. By default `multi`= 1 which means that one bead corresponds to one domain. When you want to fill space faithfully and with better accuracy you can increase this value ( keep in mind that this can lead to more complicated shapes of the simualted territories). For example, `multi`= 4 means that one domain will be represented by 4 spheres, `multi`=10 means that one domain will be represented as 10 spheres. ***Warning! Increasing this parameter leads to significant increase of the computational time necessary for model creation.*** **(mv)**; 
* `restert_after` - parameter defining after how many iterations model should restart (in case that model still did not converge)




### ChroTeMo functions

•	`nucleus()` The purpose of this function is to create the nucleus. The nucleus is represented by a sphere , with the coordinates of the center `(x_nu, y_nu, z_nu)` = (0, 0, 0), and with the radius *R* generated in a random way from the interval < `min_rad_nu`, `max_rad_nu` >;

•	`nucleolus()` This function is used to generate the nucleolus. In the first step the radius of the nucleolus *r* is determined using parameters `min_vol_no` and `max_vol_no`;

•	`centromere()` This function is responsible for generating the coordinates of the centromere bead centers (for all chromosomes);

•	`bead()` This function is used to draw all new domains of all chromosomes. The input parameters for this function are domain coordinates, color (RGB color defined as a separate degree of saturation for each component), and transparency. At the initial stage of the modelling process this function is also responsible for drawing centromeres as spheres;

•	`new_domain()` This function generates the coordinates of the new domain. 
For domains that are drawn during building the condensed chromosomes, the new coordinates are generated based on previously, last generated coordinates (within the domain of the same arm). 
For the domains that are drawn in the phase of chromatin decondensation, the coordinates of the next domain are determined on the basis of a randomly selected domain (referred to as a precursory domain) from all previously generated domains that constitute chromosome arms;

•	`dist_bead()` This function is used to check whether the newly created domain does not collide with another domain within the same chromosome. The same function is also used to check whether there is not a collision with another domain within another chromosome. The only difference is in ε parameter – here ε2 (which is greater than ε1) is used;

•	`dist_precurs()` The last step in each iteration is to verify that the newly generated domain is located at a suitable distance from the precursory domain. If this condition is true, the program returns to the function `new_domain()`;

•	`bead_generate_wrap()` This function is used to restart the program when it cannot find the solution (when it is impossible to add a new domain to the previously created model components). The function counts the number of failures in the process of generation of a new domain. When the count reaches the value declared by `restart_after` variable, the process of model creation is restarted. In the case of restart, the previously generated part of the model is not saved, and the process of generating chromosomes starts from the beginning. The number of restarts does not affect the declared number of models to generate. 



### Running ChroTeMo

Open file `ChroTeMo` with VIDLE in the same way as described in "Testing Software Environment".
ChroTeMo allows to generate more than one model in one run.
All you have to do is to run the script. It can be done in the same way as described above, when testing software environment.

In the beginning the first (and last) question appears: "How many results do you want?" You should write any reasonable (in terms of computational time) number denoting the number of models to be created.  

If you write 1 (one) - one model will be created and you can also see  visualisation. For number greater than one, Modeler works in "batch" mode and will write model parameters into files to be later viewed in Viewer.

When you close ChroTeMo, the windows with visualization will close, but the file containing the model description is automatically saved into the working directory. Files are named according to the pattern: `workfile + data + time.txt`. 
They can be used as the input files for ChroTeVi

## Using ChroTeVi
Load ChroTeVi script with VIDLE as mentioned above and run it in the same way as previously. 
Then you will be asked to point to a file generated by ChroTeMo.
 
Then, you will be asked some questions:

1. Which pair of chromosomes you want to paint. You should write digits denoting the pairs to be painted. If you want to paint only one pair, the answer to the second question should be 0 (zero).
2. The degree of transparency for the rest of the beads in a range from 0 to 1, where 0 means full transparency (beads will be invisible), 1 means no transparency.
3. If you want to color only one pair of chromosomes,  here you can choose whether you want to paint the entire chomosome in one color or use different colors for each arm ofthe chromosome.

Now you should be able to view the generated model. 
With the use of the mouse buttons and scroll you should be able to zoom in, zoom out and rotate the model.

  
That's all.
Enjoy!


# Appendix A
Algorithm pseudocode:
```
Input data: Model's parameters
Result: Model of chromosome territory arrangement

generate nucleus;
generate nucleolus;
generate centromeres;
draw centromeres;
for each arm do
    while number of domains in arm do
        repeat
            generate new coordinates of domain;
            check whether inside nucleus;
            check collision with nucleolus;
            check collision with beads in different chromosome;
            check collision with other beads in own chromosome;
        until not collision;
        draw domain;
     end
end
save bead coordinates (tab[]) to file;
```


