# Chromosome Territory Modeller and Viewer: User Manual

This document is a User Manual for Chromosome Territory Modeller (`ChroTeMo`) and Chromosome Territory Viewer (`ChroTeVi`).
The first one is intended to use when you want to create chromosome territory model for specific species. It computes parameters of modelled chromosomes, allows to preview model and save results to file. Bacause all computations are done by ChroTeMo, it works some time.
The Second is designed to be a viewer - it let you to read file created by ChroTeMo, display, rotate, zoom in and out created model. Because it works on ready model it is also fast in use.

### Hardware and software requirements
Both scripts are written in Python. For visualisation purposes we use VPython. In our script we also use libraries: time, random, gc, array, datetime.
See Python and libraries (VPython) documentation about how to install necessary software. For links see Appendix A.

If you are using Linux, probably you have Python itself already installed.
Also, if you are using Anaconda, Python(x,y) or Enthough Python distribution you have environment necessary for running those scripts.

Mininal hardware requirements are determined by requirements of Python and VPython. Anyway, because of visualisation probably it will be more comfortable if you will have own graphics card - not only those integrated with mainboard.

### Testing software environment - loading and running scripts 
After downloading and installing necessary software and libraries you can test your environment.
For that purpose you should find icon for VIDLE (rys vidle), open testing script named .... and run it.

You should see a picture similiar to presented below.

rysunek

If you succeed, you can go on. ChroTeMo and ChroTeVi should run on your computer.

## Chromosome Territory Modeller
The purpose of ChroTeMo is to create model of chromosome territory.
ChroTeMo model nucleus and nucleolus as spheres with given radius. Chromatine domains are also represented as spheres (one domain = one sphere. It is possible to change ratio by using multiplication parameter. For details see full text of article).

### ChroTeMo parameters




### Using ChroTeMo
To generate models of chromosome territory, you should set up mentioned above parameters to fit/tune model for your needs (species you examine). This can be done by direct editing script file. Parameters are listed at the beginning of the script file. 
Be careful, because some parameters may cause script - Modeler  a long running time (with parameter ... equal .... script runs when testing more than 3 weeks)!

If you are unsure about parameters, just change only species-specified parameters. You can experiment with the rest of parameters later.

After changing parameters you should save file (of course you can save file with different name).
All you have to do is to run script. It can be done in the same way as described above, when testing software environment.
Wait a while and ... enjoy your model!
When you close ChroTeMo, windows with visualisation will close, but the file with elements describing model remains in working directory. Files have names with convention: workfile + data+time.txt. 
They can be used as input files for ChroTeVi

### Using ChroTeVi
Load ChroTeVi script with VIDLE as mentioned above. Run it. 

***plik wpisywany w skrypcie, czy skrypt pyta o plik***
You will be asked some questions:
1. what should be painted
2. 

  
That's all.
Enjoy!


# Appendix A
1. Python download and installation: https://wiki.python.org/moin/BeginnersGuide/Download
2. VPython download and documentation: http://vpython.org/




```
code block
```
Żeby mieć wcięcie potrzebuję 4 spacje

```python
for i in :
    do sth
```

**pogrubienie**, *pochylenie* i ***połączone***

~~przekreślenie~~

hiperlink: http://example.com

```
codeblock
```

