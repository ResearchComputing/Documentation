# Using Python with Anaconda

To support the diverse python workflows and high levels of customization Research Computing users require, [Anaconda](http://anaconda.com) is installed on the CURC system. Anaconda is an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. The following documentation describes how to activate the CURC Anaconda distribution and our default environments, as well as how to create and activate your own custom Anaconda environments. Additional documentation on the [CURC JupyterHub](../gateways/jupyterhub.md) is available for users desiring to interact with their custom environments via [Jupyter notebooks](https://jupyter.org). 

_Note: CURC also hosts several python modules for those users who prefer modules over Anaconda. Type ```module spider python``` for a list of available python versions. Each module employs the Intel python distribution and has numerous pre-installed packages which can be queried by typing ```pip freeze```._ 

## Using the CURC Anaconda environment

Follow these steps from a Research Computing terminal session. 

#### Before you use conda for the first time:

##### Modify your ~/.condarc file so that packages are downloaded to your _/projects_ directory

Your _/home/$USER_ directory (also denoted with "_~_") is small -- only 2 GB. By default, conda downloads packages to your home directory when creating a new environment, and it will quickly become full. The steps here modify the conda configration file, called _~/.condarc_, to change the default location of _pkgs_dirs_ so that the packages are downloaed to your (much bigger) _/projects_ directory.

Open your _~/.condarc_ file in your favorite text editor (e.g., nano):
_(note: this file may not exist yet -- if not, just create a new file with this name)_
```
[johndoe@shas0137]$ nano ~/.condarc
```

...and add the following two lines:
```
pkgs_dirs:
  - /projects/$USER/.conda_pkgss
```

...then save and exit the file. You won't need to perform this step again -- it's permanent unless you change _pkgs_dirs_ by editing _~/.condarc_ again.

Note that there are lots of other things you can customize using the [~/.condarc file](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html).

### Activate the CURC Anaconda environment

#### ___For python2___:
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda2/2019.03/bin/activate
(base) [johndoe@shas0137 ~]$ conda activate idp
```

#### ___For python3___:
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/2019.03/bin/activate
(base) [johndoe@shas0137 ~]$ conda activate idp
```

The first command activates the "base" python2 or python3 environment, which uses the Anaconda python distribution.  You will know that you have properly activated the environment because you should see _`(base)`_ in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$
```

The second command (_conda activate idp_) activates the Intel python distribution (idp), which is optimized for many mathematics functions and will run more efficiently on the Intel architecture of Summit and Blanca. You will know that you have properly activated the environment because you should see _`(idp)`_ in front of your prompt. E.g.: 

```
(idp) [johndoe@shas0137 ~]$
```

_*We strongly recommend using the Intel python distribution on Summit_.

### Using python in Anaconda

#### To list the packages currently installed in the environment:

```
(idp) [johndoe@shas0137 ~]$ conda list
```

#### To add a new package named "foo" to the environment:

```
(idp) [johndoe@shas0137 ~]$ conda add foo 
```

#### To list the conda environments currently available:

```
(idp) [johndoe@shas0137 ~]$ conda env list
```

#### To deactivate an environment:

```
(idp) [johndoe@shas0137 ~]$ conda deactivate
```

#### To create a new environment in a predetermined location in your /projects directory.  

*Note: In the examples below the environment is created in /projects/$USER/software/anaconda/envs. This assumes that the software, anaconda, and envs directories already exist in /projects/$USER. Environments can be installed in any writable location the user chooses.

 ##### 1a Activate the conda environment if you haven't already done so.
 
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/2019.03/bin/activate
(base) [johndoe@shas0137 ~]$ conda activate idp
```

 ##### 2a. _Ceate a custom environment "from scratch"_: Here we create a new environment called _mycustomenv_:

```
(idp) [johndoe@shas0137 ~]$ conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv
```

 or if you want a specific version of python other than the default installed in the CURC Anaconda base environment:

```
(idp) [johndoe@shas0137 ~]$ conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv python==2.7.16
```

 ##### 2b. _Ceate a custom environment by cloning a preexisting environment_: Here we clone the preexisting Intel Python3 distribution in the CURC Anaconda environment, creating a new environment called _mycustomenv_:

```
(idp) [johndoe@shas0137 ~]$ conda create --clone idp --prefix /projects/$USER/software/anaconda/envs/mycustomenv
```

##### 3. Activate your new environment

```
(idp) [johndoe@shas0137 ~]$ conda activate /projects/$USER/software/anaconda/envs/mycustomenv
```

##### Notes on creating environments:
* You can create an environment in any directory location you prefer (as long as you have access to that directory).  We recommend using your _`/projects`_ directory because it is much larger than your _`/home`_ directory).

* Although we don't show it here, it is expected that you will be installing whatever software and packages you need in this environment, as you normally would with conda).

* We [strongly recommend] cloning the [Intel Python distribution](https://software.intel.com/en-us/distribution-for-python) if you will be doing any computationally-intensive work, or work that requires parallelization. The Intel Python distribution will run more efficiently on our Intel architecture than other python distributions.

#### Troubleshooting

If you are having trouble loading a package, you can use `conda list` or `pip freeze` to list the available packages and their verion numbers in your current conda environment. Use `conda install <packagname>` to add a new package or `conda install <packagename==version>` for a specific verison; e.g., `conda install numpy=1.16.2`.

Sometimes conda environments can "break" if two packages in the environment require different versions of the same shared library.  In these cases you try a couple of things.
* Reinstall the packages all within the same _install_ command (e.g., `conda install <package1> <package2>`).  This forces conda to attempt to resolve shared library conflicts. 
* Create a new environment and reinstall the packages you need (preferably installing all with the same `conda install` command, rather than one-at-a-time, in order to resolve the conflicts).

#### See Also

* [CURC JupyterHub](../gateways/jupyterhub.md)
