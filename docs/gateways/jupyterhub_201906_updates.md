# JupyterHub

[JupyterHub](https://jupyterhub.readthedocs.org/en/latest/) is a multi-user server for [Jupyter](https://jupyter.org/) (formerly known as IPython) notebooks. It provides a web service that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. CU Research Computing (CURC) operates a JupyterHub server includes support for serial and parallel computation on local HPC resources. The following documentation outlines how to use the CURC JupyterHub.

### Step 1: Log  in to CURC JupyterHub

CURC JupyterHub is available at [https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). To log in use your RC credentials. If you do not have an RC account, please [request an account](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization) before continuing.

### Step 2: Start a notebook server

To start a notebook server, select one of the available options in the _Select job profile_ menu under _Spawner Options_ and click _Spawn_. Available options are:

* _Summit Haswell - 2hr_ (a 2-hour, 1 core job on a Summit "shas" node)
* _Summit Haswell - 12hr_ (a 12-hour, 1 core job on a Summit "shas" node)
* _Summit Knight's Landing - 2hr_ (a 2-hour, full node job on a Summit "sknl" node)
* _Blanca - 12hr_ (A 12-hour, 1 core job on your default Blanca partition; only available to Blanca users)

The server will take a few moments to start.  When it does, you will be taken to the Jupyter home screen, which will show the contents of your CURC _/home_ directory under the _Files_ tab.  You will also see the following buttons in the upper right of the screen:

* _Quit_: Will terminate your notebook server (i.e., terminates the job you just started).  
* _Logout_: Will log you out of CURC Jupyterhub and terminate your notebook server.
* _Control Panel_: Will enable you to manually terminate and (if desired) restart your server.
* _Upload_: Enables you to upload files from your local computer to your CURC _/home_ directory.
* _New_: Enables you to open a new notebook via a chosen kernel (e.g., Python2, Python3, bash, R)
  * _documentation on opening new notebooks is provided below_

#### Default Notebook Features

* Access to standard RC file systems: 
  * /home
  * /projects/
  * /pl/active (for users with PetaLibrary allocations)
  * /scratch/summit (Summit only)
  * /rc_scratch (Blanca only)
* Access to the following default kernels in the CURC Anaconda distribution 
  (_Note: documentation on creating and importing your own custom kernels is provided below_):
  * Python2 notebooks
  * Python3 notebooks
  * BASH notebooks
  * R notebooks 
* IPyParallel/IPython clusters

### Step 3: Open a notebook

There are two ways to open a notebook:
* [To open a new notebook]: click on the _New_ button on the right hand side of the Jupyter home screen, and select one of the available options (kernels) under "Notebook", depending on the programming language (python, R, etc.) you wish to use in the notebook. Once you are in the notebook, you can save it to <myfilename>.ipynb using the _File -> Save as.._ option.
* [To open an existing notebook]: Click on the <myfilename>.ipynb notebook that you want to work in.  This will open the notebook in the appropriate kernel (assuming that kernel is available on CURC Jupyterhub).

### Step 4: Shut down a Notebook Server

Use the _Stop My Server_ button in the _Control Panel_ to shut down the Jupyter notebook server when finished (this cancels the job you are running on Summit or Blanca). You also have the option to restart a server if desired (for example, if you want to change from a "shas" to a "sknl" server).

Alternately, you can use the _Quit_ button from the Jupyter home page to shut down the Jupyter notebook server.

Using the _Logout_ button will both shut down the Jupyter notebook server and log you out of CURC JupyterHub

### Additional Documentation

#### Creating your own custom Jupyter kernels

The CURC JupyterHub runs on top of Anaconda, an open-source _python_ and _R_ distribution that uses the _conda_ package manager to easily install software and packages. Software and [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) other than _python_ and _R_ can also be installed using conda. The following steps describe how to create your own custom Anaconda environments and associated Jupyter kernels for use on RC JupyterHub. 

To follow these steps, you must first login to a terminal session on Blanca or Summit (i.e., you can't do this from within CURC JupyterHub).  

##### 1. Activate the CURC Anaconda environment

```source /curc/sw/anaconda3/2019.03/bin/activate```

##### 2. Create an environment in a predetermined location in your /projects directory.  

###### 2a. [Ceate a custom environment "from scratch"]: Here we create a new environment called _mycustomenv_ in the preexisting location _/projects/$USER/software/anaconda/envs_:

```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

or if you want a specific version of python other than the default installed in the CURC Anaconda base environment:

```conda create --prefix /projects/$USER/software/anaconda/envs/mycustomenv python==2.7.16```

###### 2b. [Ceate a custom environment by cloning a preexisting environment]: Here we clone the preexisting Intel Python3 distribution in the CURC Anaconda environment, creating a new environment called _mycustomenv_ in the preexisting location _/projects/$USER/software/anaconda/envs_:

```conda create --clone idp --prefix /projects/$USER/software/anaconda/envs/mycustomenv```

##### 3. Activate your new environment

```conda activate /projects/$USER/software/anaconda/envs/mycustomenv```

##### 4. Create your own custom kernel, which will enable you to use this environment in CURC Jupyterhub:

```python -m ipykernel install --user --name mycustomenv --display-name mycustomenv```

This command will create a kernel with the name _mycustomenv_ and the Jupyter display name _mycustomenv_.  By specifying the `--user` flag, the kernel will be in _/home/$USER/.local/share/jupyter/kernels_, a directory that is in the default JUPYTER_PATH that will ensure your new kernel is available to you the next time you use CURC JupyterHub.

[Notes on creating environments:]
* You can create an environment in any directory location you prefer (as long as you have access to that directory).  We recommend using your /projects directory because it is much larger than your /home directory).
* Although we don't show it here, it is expected that you will be installing whatever software and packages you need in this environment, as you normally would with conda).
* We [strongly recommend] cloning the [Intel Python distribution](https://software.intel.com/en-us/distribution-for-python) if you will be doing any computationally-intensive work, or work that requires parallelization. The Intel Python distribution will run more efficiently on our Intel architecture than other python distributions.
* If you have already installed your own version of Anaconda or Miniconda, it is possible to create kernels for your preexisting environments by following _Step 4_ above from within the active environment.  
* If you need to use custom kernels that are in a location other than _/home/$USER/.local/share/jupyter_ (for example, if your research team has a group installation of Anaconda environments located in _/pl/active/<some_env>_, you can create a file in your home directory named _~/.jupyterrc_ containing the following line:

   ```export JUPYTER_PATH=/pl/active/<some_env>/share/jupyter```
* If you need assistance creating or installing environments or kernels, contact us at rc-help@colorado.edu. 

#### Troubleshooting

Jupyter notebook servers spawned on RC compute resources log to `~/.jupyterhub-spawner.log`. Watching the contents of this file provides useful information regarding any problems encountered during notebook startup or execution.

#### IPython Clusters

Notebook servers started on RC compute resources can also launch IPython clusters for parallel processing. See [IPython Parallel](http://ipyparallel.readthedocs.org/en/latest/) and [MPI for Python](https://mpi4py.readthedocs.io/en/stable/) for general information on parallel processing with IPython clusters.

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

* [Parallel Programming with Jupyter Notebooks](../additional-resources/parallel-programming-jupyter.html)
* [RC JupyterHub CHANGELOG](jupyterhub/CHANGELOG.html)
