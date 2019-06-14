# Using Python with Anaconda

To support the diverse python workflows high levels of customization Research Computing users require, [Anaconda](http://anaconda.com) is installed on the CURC system. Anaconda is an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. The following documentation describes how to activate the CURC Anaconda distribution and our default environments, as well as how to create and activate your own custom Anaconda environments. Additional documentation on the [CURC JupyterHub](../gateways/jupyterhub.md) is available for users desiring to interact with their custom environments via [Jupyter notebooks](https://jupyter.org). 

## Using the CURC Anaconda environment

Follow these steps from a Research Computing terminal session. 

##### 1. Activate the CURC Anaconda environment

```source /curc/sw/anaconda3/2019.03/bin/activate```

You will know that you have properly activated the environment because you should see _`(base)`_ in front of your prompt. E.g.: `(base) [johndoe@shas0137 ~]$`

NOTES: 
CHANGE idp to idp3 (unfortunately there is no easy way to rename in conda, so:
`conda create --name idp3 --clone idp`
`conda remove --name idp --all`

Install idp2: `conda create -n idp2 intelpython2_core python=2`
```conda info envs```
```conda activate <env_I_want>```
```conda deactivate```

"rstudio" may not be an optimal name. Perhaps just call it "Renv"
You can now use 

##### 2. Create a new environment in a predetermined location in your /projects directory.  

 ###### 2a. [Ceate a custom environment "from scratch"]: Here we create a new environment called _mycustomenv_ in the preexisting location _`/projects/$USER/software/anaconda/envs`_:

 ```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

 or if you want a specific version of python other than the default installed in the CURC Anaconda base environment:

 ```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv python==2.7.16```

 ###### 2b. [Ceate a custom environment by cloning a preexisting environment]: Here we clone the preexisting Intel Python3 distribution in the CURC Anaconda environment, creating a new environment called _mycustomenv_ in the preexisting location _`/projects/$USER/software/anaconda/envs`_:

 ```conda create --clone idp --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

##### 3. Activate your new environment

```conda activate /projects/$USER/software/anaconda/envs/mycustomenv```








## Creating your own custom Anaconda environment

Follow these steps from a Research Computing terminal session. 

##### 1. Activate the CURC Anaconda environment

```source /curc/sw/anaconda3/2019.03/bin/activate```

##### 2. Create a new environment in a predetermined location in your /projects directory.  

 ###### 2a. [Ceate a custom environment "from scratch"]: Here we create a new environment called _mycustomenv_ in the preexisting location _`/projects/$USER/software/anaconda/envs`_:

 ```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

 or if you want a specific version of python other than the default installed in the CURC Anaconda base environment:

 ```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv python==2.7.16```

 ###### 2b. [Ceate a custom environment by cloning a preexisting environment]: Here we clone the preexisting Intel Python3 distribution in the CURC Anaconda environment, creating a new environment called _mycustomenv_ in the preexisting location _`/projects/$USER/software/anaconda/envs`_:

 ```conda create --clone idp --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

##### 3. Activate your new environment

```conda activate /projects/$USER/software/anaconda/envs/mycustomenv```

##### 4. Create your own custom kernel, which will enable you to use this environment in CURC Jupyterhub:

```python -m ipykernel install --user --name mycustomenv --display-name mycustomenv```

This command will create a kernel with the name _mycustomenv_ and the Jupyter display name _mycustomenv_ (note that the name and display-name are not required to match the environment name). By specifying the _`--user`_ flag, the kernel will be in _`/home/$USER/.local/share/jupyter/kernels`_ (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you use CURC JupyterHub.

##### Notes on creating environments:
* You can create an environment in any directory location you prefer (as long as you have access to that directory).  We recommend using your _`/projects`_ directory because it is much larger than your _`/home`_ directory).
* Although we don't show it here, it is expected that you will be installing whatever software and packages you need in this environment, as you normally would with conda).
* We [strongly recommend] cloning the [Intel Python distribution](https://software.intel.com/en-us/distribution-for-python) if you will be doing any computationally-intensive work, or work that requires parallelization. The Intel Python distribution will run more efficiently on our Intel architecture than other python distributions.
* If you have already installed your own version of Anaconda or Miniconda, it is possible to create Jupyter kernels for your preexisting environments by following _Step 4_ above from within the active environment.  
* If you need to use custom kernels that are in a location other than _`/home/$USER/.local/share/jupyter`_ (for example, if your research team has a group installation of Anaconda environments located in _`/pl/active/<some_env>`_), you can create a file in your home directory named _`~/.jupyterrc`_ containing the following line:

   ```export JUPYTER_PATH=/pl/active/<some_env>/share/jupyter```
* If you need assistance creating or installing environments or Jupyter kernels, contact us at rc-help@colorado.edu. 

#### Troubleshooting

Jupyter notebook servers spawned on RC compute resources log to _`~/.jupyterhub-spawner.log`_. Watching the contents of this file provides useful information regarding any problems encountered during notebook startup or execution.

#### See Also

* [RC JupyterHub CHANGELOG](jupyterhub/CHANGELOG.md)
