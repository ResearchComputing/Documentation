This repo contains the source code for building the CU Research Computing user guide as found at https://curc.readthedocs.io. All user guide builds are available at https://readthedocs.org/projects/curc/.

This is the new documentation for the NMT computer cluster system.

## Research Computing User Tutorials

This repository houses general user tutorials created by CU Boulder Research Computing.  
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

## Generating Documentation Locally

The full documentation can be generated locally using the provided `Makefile`. Note that Windows users may need to install `make` before proceeding with the below steps. For convenience a yaml file is also included, which allows one to easily construct a conda environment. To create the conda environment using the yaml file and a terminal, first [download Anaconda](https://www.anaconda.com/). Once Anaconda has been installed the conda environment `rc-docs` can be created using
```
conda env create -f conda_dev_env.yml
```
This new environment can then be activated as follows
```
conda activate rc-docs
```

Using the `rc-docs` environment we can now easily generate the documentation locally using the following make command:
```
make html
```
this command builds the documentation and stores it in the directory `build`. 

One can then view the documentation using:
```
make view 
```
which will open the index page of the documentation. 

Although not necessary, one can then remove the build folder using:
```
make clean
```
