# Jupyter Sessions

[Jupyter Notebooks](https://jupyter.org/) are an excellent resource for interactive development and data analysis using _Python_, _R_, and other languages. Jupyter notebooks can contain live code, equations, visualizations, and explanatory text, which provide an integrated environment to use, learn, and teach interactive data analysis. Users can obtain quick access to Jupyter sessions using [Open OnDemand](./OnDemand.md) and easily launch a JupyterLab interface. The JupyterLab interface is a fantastic tool that provides a highly customizable graphical user interface (GUI) that allows users to easily navigate multiple Jupyter Notebooks and the CURC filesystem. 

## Navigating the JupyterLab Interface

The following features are available in the [JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html):

* _Left sidebar:_ Click on a tab to change what you see in the left menu bar.  Options include the file browser, a list of running kernels and terminals, a command palette, a notebook cell tools inspector, an extension manager, and a tabs list.
* _Left menu bar:_ 
  * The _file browser_ will be active when you log in. 
    * You can navigate to your other CURC directories by clicking the folder next 
to `/` or going to "File" then "Open Path" and entering your path in the field. Your other CURC file systems are available too: 
`/projects/<username>`, `/pl/active` (for users with PetaLibrary allocations), 
`/scratch/alpine/<username>` (Alpine only), and `/rc_scratch/<username>` (Blanca 
only).
    * To open an existing notebook, just click on the notebook name in the file browser (e.g., _mynotebook.ipynb_).
    * Above your working directory contents are buttons to add a new Launcher, create a new folder, upload files from your local computer, and refresh the working directory. 
* _Main Work Area:_ Your workspaces will be in this large area on the right hand side. Under the "Launcher" tab you can: 
  * Open a new notebook with any of the kernels listed:
      * __Python 3 (idp)__: Python3 notebook (Intel Python distribution)
      * __Bash__: BASH notebook
      * __R__: R notebook 
      * ...and any other custom kernels you add on your own _(see the [section below](#creating-your-own-custom-jupyter-kernel) on creating your own custom kernels)._
   * Open a new console (command line) for any of the kernels.
   * Open other functions; the "Terminal" function is particularly useful as it enables you to access the command line on the Alpine or Blanca node your Jupyter Session
job is currently running on. 
* See Jupyter's [documentation on the JupyterLab Interface for additional information.](https://jupyterlab.readthedocs.io/en/stable/user/interface.html)

## Find packages available to you within a notebook

The ___Python 3 (idp)___ notebook kernels have many preinstalled packages. To query a list of available packages from a python notebook, you can use the following nomenclature:

```
from pip._internal import main as pipmain 
pipmain(['freeze'])
```

If the packages you need are not available, you can create your own custom environment and Jupyter kernel.

## Creating your own custom Jupyter kernel

[Anaconda](http://anaconda.com) is an open-source software that provides access to _python_ and _R_ distributions, and it includes the _conda_ package manager to easily install software and packages. Software and associated Jupyter [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) other than _python_ and _R_ can also be installed using _conda_. The following steps describe how to create your own custom Anaconda environments and associated Jupyter kernels for use within a Jupyter Session. 

Follow these steps from a terminal session. You can get a new terminal session directly from Jupyter using `New`-> `Terminal`.

### 1.  Configure your conda settings

Follow our Anaconda documentation for [steps on configuring your conda settings via ~.condarc](../software/python.md#configuring-conda-with-condarc).

### 2. Activate the CURC Anaconda environment

```
[johndoe@c3cpu-a5-u15-4 ~]$ module load anaconda
```

You will know that you have properly activated the environment because you should see `(base)` in front of your prompt. For example, 

```
(base) [johndoe@c3cpu-a5-u15-4 ~]$
```

### 3. Create a new custom environment 

Follow our Anaconda documentation for [steps on creating your own custom conda environment](../software/python.md#create-your-own-custom-environment).


### 4. Activate your new environment

```
(base) [johndoe@c3cpu-a5-u15-4 ~]$ conda activate mycustomenv
```

> Note: We assume here that you've named your environment _mycustomenv_; please replace _mycustomenv_ with whatever name you gave your environment!

### 5. Create your own custom kernel, which will enable you to use this environment in your Jupyter Session

__For a _python_ kernel__

```
(mycustomenv) [johndoe@c3cpu-a5-u15-4 ~]$ conda install -y ipykernel
(mycustomenv) [johndoe@c3cpu-a5-u15-4 ~]$ python -m ipykernel install --user --name mycustomenv --display-name mycustomenv
```

* The first command will install the _ipykernel_ package if not installed already. 
* The second command will create a _python_ kernel with the name _mycustomenv_ with the Jupyter display name _mycustomenv_ (note: the name and display-name are not required to match the environment name -- call them anything you want). By specifying the `--user` flag, the kernel will be installed in `/home/$USER/.local/share/jupyter/kernels` (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you launch a Jupyter Session.

__For an _R_ kernel__

```
(mycustomenv) [johndoe@c3cpu-a5-u15-4 ~]$ conda install -y r-irkernel
(mycustomenv) [johndoe@c3cpu-a5-u15-4 ~]$ R
> IRkernel::installspec(name = 'mycustomenv', displayname = 'mycustomenv')
```

* The first command will install the _irkernel_ package if not installed already. 
* The second command will start _R_. The third command, executed from within _R_, will create an _R_ kernel with the name _mycustomenv_ with the Jupyter display name _mycustomenv_ (note: that the name and display-name are not required to match the environment name -- call them anything you want). The kernel will be installed in `/home/$USER/.local/share/jupyter/kernels` (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you launch a Jupyter Session.

### Notes:
* If you have already installed your own version of Anaconda or Miniconda, it is possible to create Jupyter kernels for your preexisting environments by following _Step 4_ above from within the active environment.  
* If you need to use custom kernels that are in a location other than `/home/$USER/.local/share/jupyter` (for example, if your research team has a group installation of Anaconda environments located in `/pl/active/<some_env>`), you can create a file in your home directory named `~/.jupyterrc` containing the following line:
```
export JUPYTER_PATH=/pl/active/<some_env>/share/jupyter
```

If you need assistance creating or installing environments or Jupyter kernels, contact us at <rc-help@colorado.edu>. 

## Troubleshooting

* If you are a CSU or ACCESS user and are having trouble with packages that employ PERL (due to the `@` symbol), visit our documentation on setting up a user variable that links to alternate paths without the `@` symbol in [CSU and XSEDE/ACCESS usernames](../additional-resources/csu-xsede-usernames.md)


## See Also

* [CURC Anaconda distribution](../software/python.md)
* [JupyterLab homepage](https://jupyterlab.readthedocs.io)


