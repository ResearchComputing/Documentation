## JupyterHub

[JupyterHub](https://jupyterhub.readthedocs.org/en/latest/) is a multi-user server for [Jupyter](https://jupyter.org/) (formerly known as IPython) notebooks. It provides a web service that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. The CU Research Computing environment includes support for parallel computation on local HPC resources.

### Step 1: Log  in to CURC JupyterHub

JupyterHub is available at [https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). To log in use your RC credentials. If you do not have an RC account, please [request an account](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization) before continuing.

### Step 2: Start a notebook server

To start a notebook server, select one of the available options in the _Select job profile_ menu under _Spawner Options_ and click _Spawn_. Available options are:

* Summit Haswell - 2hr (a 2-hour, 1 core job on a Summit "shas" node)
* Summit Haswell - 12hr (a 12-hour, 1 core job on a Summit "shas" node)
* Summit Knight's Landing - 2hr (a 2-hour, full node job on a Summit "sknl" node)
* Blanca - 12hr (A 12-hour, 1 core job on your default Blanca partition; only available to Blanca users)

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
* Access to three default kernels in the CURC Anaconda distribution:
  * Python2 notebooks
  * Python3 notebooks
  * BASH notebooks
    * _documentation on creating and importing your own custom kernels is provided below_ 
* IPyParallel/IPython clusters

### Step 3: Open a notebook


### Step 4: Shut down a Notebook Server

Use the _Stop My Server_ button in the _Control Panel_ to shut down the Jupyter notebook server when finished (this cancels the job you are running on Summit or Blanca). You also have the option to restart a server if desired (for example, if you want to change from a "shas" to a "sknl" server).

Alternately, you can use the _Quit_ button from the Jupyter home page to shut down the Jupyter notebook server.

Using the _Logout_ button will both shut down the Jupyter notebook server and log you out of CURC JupyterHub

### Additional Documentation

#### Creating your own custom Jupyter kernels

TEXT HERE.

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
