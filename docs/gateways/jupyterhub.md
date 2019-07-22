## JupyterHub

[Jupyter notebooks](https://jupyter.org/) are an excellent resource for interactive development and data analysis using Python, R, and other languages. Jupyter notebooks can contain live code, equations, visualizations, and explanatory text which provide an excellent enviornment to use, learn, and teach interactive data analysis.  

CU Research Computing (CURC) operates a [JupyterHub server](https://jupyterhub.readthedocs.org/en/latest/) that enables users to run Jupyter notebooks on Summit or Blanca for serial (single core) and shared-memory parallel (single node) workflows. The CURC JupyterHub runs atop of [Anaconda](http://anaconda.com).  Additional documentation on the [CURC Anaconda distribution](../software/python.md) is available and may be a good pre-requisite for the following documentation outlining use of the CURC JupyterHub.

### Step 1: Log  in to CURC JupyterHub

CURC JupyterHub is available at [https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). To log in use your RC credentials. If you do not have an RC account, please [request an account before continuing.](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization)

### Step 2: Start a notebook server

To start a notebook server, select one of the available options in the *Select job profile* menu under *Spawner Options* and click *Spawn*. Available options are:

* __Anaconda-based servers (recommended)__
   * __Summit interactive (12hr)__ (a 12-hour, 1 core job on a Summit "shas" node)
   * __Summit Haswell (1 node, 12hr)__ (a 12-hour, 24 core job on a Summit "shas" node)
   * __Blanca (12hr)__ (A 12-hour, 1 core job on your default Blanca partition; only available to Blanca users)
   * __Blanca CSDMS (12hr)__ (A 12-hour, 1 core job on the Blanca CSDMS partition; only available to Blanca CSDMS users)
* __Module-based servers (legacy; no longer supported)__
   * __Legacy - Summit Haswell - 2hr__ (a 2-hour, 1 core job on a Summit "shas" node)
   * __Legacy - Summit Haswell - 12hr__ (a 12-hour, 1 core job on a Summit "shas" node)
   * __Legacy - Summit Knight's Landing__ (a 2-hour, full node job on a Summit "sknl" node)
   * __Legacy - Blanca CSDMS__ (A 12-hour, 1 core job on the Blanca CSDMS partition; only available to Blanca CSDMS users)
   * __Legacy - Blanca Sol__ (A 12-hour, 1 core job on the Blanca Sol partition; only available to Blanca Sol users)
   * __Legacy - Blanca APPM__ (A 12-hour, 1 core job on the Blanca APPM partition; only available to Blanca APPM users)

The server will take a few moments to start.  When it does, you will be taken to the Jupyter home screen, which will show the contents of your CURC `/home` directory under the `Files` tab.  You will also see the following buttons in the upper right of the screen:

* _Quit_: Will terminate your notebook server (i.e., terminates the job you just started).  
* _Logout_: Will log you out of CURC Jupyterhub and terminate your notebook server.
* _Control Panel_: Will enable you to manually terminate and (if desired) restart your server.
* _Upload_: Enables you to upload files from your local computer to your CURC _`/home`_ directory.
* _New_: Enables you to open a new notebook via a chosen kernel (e.g., Python2, Python3, bash, R) 
    * _documentation on opening new notebooks is provided in "Step 3" below_

#### Default Notebook Features

* Access to standard RC file systems: 
  * `/home`
  * `/projects/`
  * `/pl/active` (for users with PetaLibrary allocations)
  * `/scratch/summit` (Summit only)
  * `/rc_scratch` (Blanca only)
* Access to the following default kernels in the CURC Anaconda distribution 
  (_Note: documentation on creating and importing your own custom kernels is provided in the "Additional Documentation" below_):
  * __Python 2 (idp)__: Python2 notebook (Intel Python distribution)
  * __Python 3 (idp)__: Python3 notebook (Intel Python distribution)
  * __Bash__: BASH notebook
  * __R__: R notebook 
* IPyParallel/IPython clusters

### Step 3: Open a notebook

There are two ways to open a notebook:
* _To open a new notebook_: click on the _`New`_ button on the right hand side of the Jupyter home screen, and select one of the available options (kernels) under "Notebook", depending on the programming language you wish to use in the notebook (e.g., python, R, bash). Once you are in the notebook, you can save it to _myfilename_.ipynb using the _File -> Save as.._ option.
* To open an existing notebook: Click on the _myfilename_.ipynb notebook that you want to work in.  This will open the notebook in the appropriate kernel (assuming that kernel is available on CURC Jupyterhub).

_Tip_: The ___Python 2 (idp)___ and ___Python 3 (idp)___ notebook environments have many preinstalled packages. To query a list of available packages from a python notebook, you can use the following nomenclature:

```
from pip._internal import main as pipmain 
pipmain(['freeze'])
```

If the packages you need are not available, [you can create your own custom environment and Jupyter kernel](#additional-documentation).

### Step 4: Shut down a Notebook Server

Use the _`Stop My Server`_ button in the _`Control Panel`_ to shut down the Jupyter notebook server when finished (this cancels the job you are running on Summit or Blanca). You also have the option to restart a server if desired (for example, if you want to change from a "shas" to a "sknl" server).

Alternately, you can use the _`Quit`_ button from the Jupyter home page to shut down the Jupyter notebook server.

Using the _`Logout`_ button will log you out of CURC JupyterHub.  It will not shut down your notebook server if one happens to be running.  

## Additional Documentation

### Creating your own custom Jupyter kernels

The CURC JupyterHub runs on top of the [CURC Anaconda distribution](../software/python.md). [Anaconda](http://anaconda.com) is an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. Software and associated Jupyter [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) other than _python_ and _R_ can also be installed using _conda_. The following steps describe how to create your own custom Anaconda environments and associated Jupyter kernels for use on RC JupyterHub. 

Follow these steps from a terminal session. You can get a new terminal session directly from Jupyter using `New`-> `Terminal`.

#### 1. Activate the CURC Anaconda environment

__For python2__:
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda2/2019.03/bin/activate
```

__For python3__:
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/2019.03/bin/activate
```

You will know that you have properly activated the environment because you should see `(base)` in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$
```

#### 2. Modify your `~/.condarc` file so that packages are downloaded to your `/projects` directory

By default, conda downloads packages to your `home/$USER` directory when creating a new environment. Your `/home/$USER` directory (also denoted with `~`) is small -- only 2 GB. The steps here modify the conda configration file, called `~/.condarc`, to change the default location of `pkgs_dirs` so that the packages are downloaed to your (much bigger) `/projects` directory.

Open your `~/.condarc` file in your favorite text editor (e.g., nano, vim):
_(note: this file may not exist yet -- if not, just create a new file with this name)_
```
(base) [johndoe@shas0137]$ nano ~/.condarc
```

...and add the following two lines:
```
pkgs_dirs:
  - /projects/$USER/.conda_pkgss
```

...then save and exit the file. You won't need to perform this step again -- it's permanent unless you change _pkgs_dirs_ by editing _~/.condarc_ again.

Note: You can customize [a variety of jupyter settings using the `~/.condarc` file](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html).

#### 3. Create a new environment in a predetermined location in your /projects directory.  

_*Note: In the examples below the environment is created in `/projects/$USER/software/anaconda/envs`. This assumes that the `software`, `anaconda`, and `envs` directories already exist in `/projects/$USER`. Environments can be installed in any writable location the user chooses._ 

##### a. _Create a custom environment "from scratch"_: Here we create a new environment called _mycustomenv_:

 ``` You will know that you have properly activated the environment because you should see _`(base)`_ in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$ conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv
```

 or if you want a specific version of python other than the default installed in the CURC Anaconda base environment:

 ```
 (base) [johndoe@shas0137 ~]$ conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv python==2.7.16
 ```

 or...

##### b. _Create a custom environment by cloning a preexisting environment_: Here we clone the preexisting Intel Python3 distribution in the CURC Anaconda environment, creating a new environment called _mycustomenv_:

 ```
 (base) [johndoe@shas0137 ~]$ conda create --clone idp --prefix /projects/$USER/software/anaconda/envs/mycustomenv
 ```

#### 4. Activate your new environment

```
(base) [johndoe@shas0137 ~]$ conda activate /projects/$USER/software/anaconda/envs/mycustomenv
```

#### 5. Create your own custom kernel, which will enable you to use this environment in CURC Jupyterhub:

```
(mycustomenv) [johndoe@shas0137 ~]$ python -m ipykernel install --user --name mycustomenv --display-name mycustomenv
```

This command will create a kernel with the name _mycustomenv_ and the Jupyter display name _mycustomenv_ (note that the name and display-name are not required to match the environment name -- call them anything you want). By specifying the _`--user`_ flag, the kernel will be in _`/home/$USER/.local/share/jupyter/kernels`_ (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you use CURC JupyterHub.

##### Notes on creating environments:
* You can create an environment in any directory location you prefer (as long as you have access to that directory).  We recommend using your _`/projects`_ directory because it is much larger than your _`/home`_ directory).
* Although we don't show it here, it is expected that you will be installing whatever software and packages you need in this environment, as you normally would with conda).
* We [strongly recommend] cloning the [Intel Python distribution](https://software.intel.com/en-us/distribution-for-python) (idp) if you will be doing any computationally-intensive work, or work that requires parallelization. The Intel Python distribution will run more efficiently on our Intel architecture than other python distributions.
* If you have already installed your own version of Anaconda or Miniconda, it is possible to create Jupyter kernels for your preexisting environments by following _Step 4_ above from within the active environment.  
* If you need to use custom kernels that are in a location other than _`/home/$USER/.local/share/jupyter`_ (for example, if your research team has a group installation of Anaconda environments located in _`/pl/active/<some_env>`_), you can create a file in your home directory named _`~/.jupyterrc`_ containing the following line:

   ```export JUPYTER_PATH=/pl/active/<some_env>/share/jupyter```
* If you need assistance creating or installing environments or Jupyter kernels, contact us at rc-help@colorado.edu. 

## Troubleshooting

Jupyter notebook servers spawned on RC compute resources log to _`~/.jupyterhub-spawner.log`_. Watching the contents of this file provides useful information regarding any problems encountered during notebook startup or execution.

## See Also

* [CURC Anaconda distribution](../software/python.md)
* [RC JupyterHub CHANGELOG](jupyterhub/CHANGELOG.md)
