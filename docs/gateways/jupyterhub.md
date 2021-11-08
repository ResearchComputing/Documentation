## JupyterHub _(Python and R notebooks on CURC)_

[Jupyter notebooks](https://jupyter.org/) are an excellent resource for interactive development and data analysis using _Python_, _R_, and other languages. Jupyter notebooks can contain live code, equations, visualizations, and explanatory text which provide an integrated enviornment to use, learn, and teach interactive data analysis.  

CU Research Computing (CURC) operates a [JupyterHub server](https://jupyterhub.readthedocs.org/en/latest/) that enables users to run Jupyter notebooks on Summit or Blanca for serial (single core) and shared-memory parallel (single node) workflows. The CURC JupyterHub uses the next-generation [JupyterLab](https://jupyterlab.readthedocs.io) user interface. The CURC JupyterHub runs atop of [Anaconda](http://anaconda.com).  Additional documentation on the [CURC Anaconda distribution](../software/python.md) is available and may be a good pre-requisite for the following documentation outlining use of the CURC JupyterHub.

### Step 1: Log  in to CURC JupyterHub

CURC JupyterHub is available at [https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). To log in use your RC credentials. If you do not have an RC account, please [request an account before continuing.](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization)

### Step 2: Start a notebook server

To start a notebook server, select one of the available options in the *Select job profile* menu under *Spawner Options* and click *Spawn*. Available options are:

* __Summit interactive (1 core, 12hr, instant access)__ (a 12-hour, 1 core job on a Summit "shas" node)
* __Summit Haswell (12 cores, 4 hours)__ (a 4-hour, 12 core job on a Summit "shas" node)
* __Blanca (1 core, 12hr)__ (A 12-hour, 1 core job on your default Blanca partition; only available to Blanca users)
* __Blanca (12 cores, 4 hr)__ (A 4-hour, 12 core job on your default Blanca partition; only available to Blanca users)
* __Blanca CSDMS (12hr)__ (A 12-hour, 1 core job on the Blanca CSDMS partition; only available to Blanca CSDMS users)
* __Summit interactive Rstudio (1 core, 12hr)__ (a 12-hour, 1 core _Rstudio_ job on a Summit "shas" node)
  
___Note__: The "Summit interactive (1 core, 12hr, instant access)" option spawns a 1-core job to a partition on Summit called "shas-interactive". This partition is intended to provide "instant" access to computing resources for JupyterHub users.  The caveat is that 1) users may only run one "shas-interactive" job at a time, and 2) "shas-interactive" jobs only have 1 core and 4 GB of memory allocated to them. Therefore, this option works well for light work such as interactive code development and small processing tasks, but jobs may crash if large files are ingested or memory-intensive computing is conducted.  If this is your case, please consider running your workflow via a batch job on Summit, or try the "Summit Haswell (12 cores, 4 hours)" option (queue waits will be longer for this option).  Dask users should either run their workflows via a batch job on Summit, or use the "Summit Haswell (12 cores, 4 hours)" option because this provides 12-cores to the Dask array. Using "shas-interactive" for Dask jobs would only provide one core to the Dask array, negating its utility)._

The server will take a few moments to start.  When it does, you will be taken to the Jupyter home screen, which will show the contents of your CURC `/home` directory in the left menu bar. In the main work area on the right hand side you will see the "Launcher" and any other tabs you may have open from previous sessions.

<p align="middle">
  <img src="https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/docs/gateways/jupyterhub/jupyterlab1.png"/>
</p>


### Step 3: Navigating the JupyterLab Interface

The following features are availabe in the [JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html):

* _Left sidebar:_ Click on a tab to change what you see in the left menu bar.  Options include the file browser, a list of running kernels and terminals, a command palette, a notebook cell tools inspector, and a tabs list.
* _Left menu bar:_ 
  * The _file browser_ will be active when you log in. 
    * You can navigate to your other CURC directories by clicking the folder next to `/home/<username>`. Your other CURC file systems are available too: `/projects/<username>`, `/pl/active` (for users with PetaLibrary allocations), `/scratch/summit/<username>` (Summit only), and `/rc_scratch/<username>` (Blanca only).
    * To open an existing notebook, just click on the notebook name in the file browser (e.g., _mynotebook.ipynb_).
    * Above your working directory contents are buttons to add a new Launcher, create a new folder, upload files from your local computer, and refresh the working directory. 
* _Main Work Area:_ Your workspaces will be in this large area on the right hand side. Under the "Launcher" tab you can: 
  * Open a new notebook with any of the kernels listed:
      * __Python 3 (idp)__: Python3 notebook (Intel Python distribution)
      * __Bash__: BASH notebook
      * __R__: R notebook 
      * ...and any other custom kernels you add on your own _(see the [section below](#creating-your-own-custom-jupyter-kernels) on creating your own custom kernels)._
   * Open a new console (command line) for any of the kernels.
   * Open other functions; the "Terminal" function is particularly useful, as it enables you to access the command line on the Summit or Blanca node your Jupyterhub job is currently running on. 
* See Jupyter's [documentation on the JupyterLab Interface for additional information.](https://jupyterlab.readthedocs.io/en/stable/user/interface.html)

#### Tip for finding the packages available to you within a notebook

The ___Python 3 (idp)___ notebook kernels have many preinstalled packages. To query a list of available packages from a python notebook, you can use the following nomenclature:

```
from pip._internal import main as pipmain 
pipmain(['freeze'])
```

If the packages you need are not available, [you can create your own custom environment and Jupyter kernel](#additional-documentation).

    
#### For users who prefer the "old school" classic Jupyter interface in favor of JupyterLab

You can access the Jupyter classic view by going to the address bar at the top of your broswer and changing "lab" to "tree" in the URL.  For, example, if your session URL is https://jupyter.rc.colorado.edu/user/janedoe/lab, you can change this to https://jupyter.rc.colorado.edu/user/janedoe/tree . 

### Step 4: Shut down a Notebook Server

Go to the "File" menu at the top and choose "Hub Control Panel". Use the `Stop My Server` button in the `Control Panel` to shut down the Jupyter notebook server when finished (this cancels the job you are running on Summit or Blanca). You also have the option to restart a server if desired (for example, if you want to change from a "Summit Interactive" to a "Summit Haswell" server).

Alternately, you can use the `Quit` button from the Jupyter home page to shut down the Jupyter notebook server.

Using the `Logout` button will log you out of CURC JupyterHub.  It will not shut down your notebook server if one happens to be running.  

### Additional Documentation

#### Creating your own custom Jupyter kernels

The CURC JupyterHub runs on top of the [CURC Anaconda distribution](../software/python.html). [Anaconda](http://anaconda.com) is an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. Software and associated Jupyter [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) other than _python_ and _R_ can also be installed using _conda_. The following steps describe how to create your own custom Anaconda environments and associated Jupyter kernels for use on RC JupyterHub. 

Follow these steps from a terminal session. You can get a new terminal session directly from Jupyter using `New`-> `Terminal`.

##### 1.  Configure your conda settings

Follow our Anaconda documentation for [steps on configuring your conda settings via ~.condarc](../software/python.html#configure-your-conda-settings).

##### 2. Activate the CURC Anaconda environment

```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/latest
```

You will know that you have properly activated the environment because you should see `(base)` in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$
```

##### 3. Create a new custom environment. 

Follow our Anaconda documentation for [steps on creating your own custom conda environment](../software/python.html#create-your-own-custom-environment).


##### 4. Activate your new environment

```
(base) [johndoe@shas0137 ~]$ conda activate mycustomenv
```

(Note: we assume here that you've named your environment _mycustomenv_; please replace _mycustomenv_ with whatever name you gave your environment!)

##### 5. Create your own custom kernel, which will enable you to use this environment in CURC Jupyterhub:

__For a _python_ kernel__

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install -y ipykernel
(mycustomenv) [johndoe@shas0137 ~]$ python -m ipykernel install --user --name mycustomenv --display-name mycustomenv
```

The first command will install the _ipykernel_ package if not installed already. The second command will create a _python_ kernel with the name _mycustomenv_ with the Jupyter display name _mycustomenv_ (note that the name and display-name are not required to match the environment name -- call them anything you want). By specifying the `--user` flag, the kernel will be installed in `/home/$USER/.local/share/jupyter/kernels` (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you use CURC JupyterHub.

__For an _R_ kernel__

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install -y r-irkernel
(mycustomenv) [johndoe@shas0137 ~]$ R
> IRkernel::installspec(name = 'mycustomenv', displayname = 'mycustomenv')
```

The first command will install the _irkernel_ package if not installed already. The second command will start _R_. The third command, executed from within _R_, will create an _R_ kernel with the name _mycustomenv_ with the Jupyter display name _mycustomenv_ (note that the name and display-name are not required to match the environment name -- call them anything you want). The kernel will be installed in `/home/$USER/.local/share/jupyter/kernels` (a directory that is in the default __JUPYTER_PATH__) and will ensure your new kernel is available to you the next time you use CURC JupyterHub.

##### Notes:
* If you have already installed your own version of Anaconda or Miniconda, it is possible to create Jupyter kernels for your preexisting environments by following _Step 4_ above from within the active environment.  
* If you need to use custom kernels that are in a location other than `/home/$USER/.local/share/jupyter` (for example, if your research team has a group installation of Anaconda environments located in `/pl/active/<some_env>`), you can create a file in your home directory named `~/.jupyterrc` containing the following line:
* If you are a CSU or XSEDE user and are having trouble with packages that employ PERL (due to the `@` symbol) visit our documentation on setting up a user variables that links to alternate paths without the `@` symbol [CSU and XSEDE usernames](../additional-resources/csu-xsede-usernames.md)

```
export JUPYTER_PATH=/pl/active/<some_env>/share/jupyter
```

If you need assistance creating or installing environments or Jupyter kernels, contact us at rc-help@colorado.edu. 

#### Using Dask to spawn multi-core jobs from CURC JupyterHub

_Dask is a flexible library for parallel computing in Python. Documentation for using Dask on RC JupyterHub is forthcoming. In the meantime, if you need help integrating Dask with Slurm so that you can run multicore jobs on the CURC JupyterHub, please contact us at rc-help@colorado.edu._

### Troubleshooting

Jupyter notebook servers spawned on RC compute resources log to `~/.jupyterhub-spawner.log`. Watching the contents of this file provides useful information regarding any problems encountered during notebook startup or execution.

### See Also

* [CURC Anaconda distribution](../software/python.html)
* [RC JupyterHub CHANGELOG](jupyterhub/CHANGELOG.html)
* [JupyterLab homepage](https://jupyterlab.readthedocs.io)
