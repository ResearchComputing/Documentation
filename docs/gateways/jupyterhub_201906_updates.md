# JupyterHub

[JupyterHub](https://jupyterhub.readthedocs.org/en/latest/) is a multi-user server for [Jupyter](https://jupyter.org/) (formerly known as IPython) notebooks. It provides a web service that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. CU Research Computing (CURC) operates a JupyterHub server includes support for serial and parallel computation on local HPC resources. The following documentation outlines how to use the CURC JupyterHub.

### Step 1: Log  in to CURC JupyterHub

CURC JupyterHub is available at [https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). To log in use your RC credentials. If you do not have an RC account, please [request an account](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization) before continuing.

### Step 2: Start a notebook server

To start a notebook server, select one of the available options in the _`Select job profile`_ menu under _`Spawner Options`_ and click _`Spawn`_. Available options are:

* ___Summit Haswell - 2hr___ (a 2-hour, 1 core job on a Summit "shas" node)
* ___Summit Haswell - 12hr___ (a 12-hour, 1 core job on a Summit "shas" node)
* ___Summit Knight's Landing - 2hr___ (a 2-hour, full node job on a Summit "sknl" node)
* ___Blanca - 12hr___ (A 12-hour, 1 core job on your default Blanca partition; only available to Blanca users)

The server will take a few moments to start.  When it does, you will be taken to the Jupyter home screen, which will show the contents of your CURC _`/home`_ directory under the _`Files`_ tab.  You will also see the following buttons in the upper right of the screen:

* _`Quit`_: Will terminate your notebook server (i.e., terminates the job you just started).  
* _`Logout`_: Will log you out of CURC Jupyterhub and terminate your notebook server.
* _`Control Panel`_: Will enable you to manually terminate and (if desired) restart your server.
* _`Upload`_: Enables you to upload files from your local computer to your CURC _`/home`_ directory.
* _`New`_: Enables you to open a new notebook via a chosen kernel (e.g., Python2, Python3, bash, R)
  * _documentation on opening new notebooks is provided in "Step 3" below_

#### Default Notebook Features

* Access to standard RC file systems: 
  * _`/home`_
  * _`/projects/`_
  * _`/pl/active`_ (for users with PetaLibrary allocations)
  * _`/scratch/summit`_ (Summit only)
  * _`/rc_scratch`_ (Blanca only)
* Access to the following default kernels in the CURC Anaconda distribution 
  (_Note: documentation on creating and importing your own custom kernels is provided in the "Additinoal Documentation" below_):
  * Python2 notebooks
  * Python3 notebooks
  * BASH notebooks
  * R notebooks 
* IPyParallel/IPython clusters

### Step 3: Open a notebook

There are two ways to open a notebook:
* _To open a new notebook_: click on the _`New`_ button on the right hand side of the Jupyter home screen, and select one of the available options (kernels) under "Notebook", depending on the programming language you wish to use in the notebook (e.g., python, R, bash). Once you are in the notebook, you can save it to _myfilename_.ipynb using the _File -> Save as.._ option.
* To open an existing notebook: Click on the _myfilename_.ipynb notebook that you want to work in.  This will open the notebook in the appropriate kernel (assuming that kernel is available on CURC Jupyterhub).

### Step 4: Shut down a Notebook Server

Use the _`Stop My Server`_ button in the _`Control Panel`_ to shut down the Jupyter notebook server when finished (this cancels the job you are running on Summit or Blanca). You also have the option to restart a server if desired (for example, if you want to change from a "shas" to a "sknl" server).

Alternately, you can use the _`Quit`_ button from the Jupyter home page to shut down the Jupyter notebook server.

Using the _`Logout`_ button will log you out of CURC JupyterHub.  It will not shut down your notebook server if one happens to be running.  

-----------------------------

### Additional Documentation

#### Creating your own custom Jupyter kernels

The CURC JupyterHub runs on top of [Anaconda](http://anaconda.com), an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. Software and associated Jupyter [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) other than _python_ and _R_ can also be installed using _conda_. The following steps describe how to create your own custom Anaconda environments and associated Jupyter kernels for use on RC JupyterHub. 

To follow these steps, you must first login to a terminal session on Blanca or Summit (i.e., you can't do this from within CURC JupyterHub).  

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

#### IPython Clusters

Notebook servers started on Summit can also launch IPython clusters for parallel processing. See [IPython Parallel](http://ipyparallel.readthedocs.org/en/latest/) and [MPI for Python](https://mpi4py.readthedocs.io/en/stable/) for general information on parallel processing with IPython clusters.

The RC environment provisions two IPython profiles automatically which can be used as a reference point for starting IPython clusters. These profiles are available in the _IPython Clusters_ tab.

##### `default`

The `default` profile is generated automatically by IPython. Engines
are dispatched in the same resources as the notebook server, and
provide no MPI support or cluster performance.

##### `example-shas`

Each `example-shas` engine provides access to a Summit Haswell CPU
thread. Multiple engines are aggregated into a single MPI session.

**Note:** IPython engines on RC cluster resources are provisioned as
batch jobs using Slurm, but Jupyter does not yet report queue
progress. The exception "NoEnginesRegistered: Can't build targets
without any engines" indicates that the cluster job is still in the
queue and not ready to accept work.

#### See Also

* [Parallel Programming with Jupyter Notebooks](./parallel-programming-jupyter.md)
* [RC JupyterHub CHANGELOG](jupyterhub/CHANGELOG.md)
