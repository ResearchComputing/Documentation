[JupyterHub](https://jupyterhub.readthedocs.org/en/latest/) is a multi-user server for [Jupyter](https://jupyter.org/) (formerly known as IPython) notebooks. It provides a web service that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. The CURC environment includes support for parallel computation on local HPC resources.

JupyterHub is available at https://jupyter.rc.colorado.edu. To log in use your RC credentials. If you do not have an RC account, please [request an account](https://portals.rc.colorado.edu/accounts/account-request/create/general) before continuing.

## Start a notebook server
To start a notebook server, select one of the available options in the _Select job profile_ menu and click _Spawn_. Available options are explained below.

### Virtual Notebook Server
Virtual notebook servers are started on the JupyterHub host, and are **not intended for computational work**. The following features are supported by virtual notebooks:
* Access to standard RC file systems
* Python 3 notebooks
* BASH notebooks

### Summit Haswell
These notebook servers start on the `shas` partition using the `normal` QOS. The following features are supported by Summit Haswell notebooks:
* Access to standard RC file systems
* Access to [RC environment modules](https://www.rc.colorado.edu/support/user-guide/modules.html)
* Python 3 notebooks
* Python 2.7 notebooks
* BASH notebooks
* IPyParallel/IPython clusters

### Summit Knight's Landing
These notebook servers start on the `sknl` partition using the `normal` QOS. The following features are supported by Summit KNL notebooks:
* Access to standard RC file systems
* Access to [RC environment modules](https://www.rc.colorado.edu/support/user-guide/modules.html)
* Python 3 notebooks
* Python 2.7 notebooks
* BASH notebooks
* IPyParallel/IPython clusters

## Stopping a Notebook Server
Use the _Stop My Server_ button in the _Control Panel_ to shut down the Jupyter notebook server when finished.

## Troubleshooting
Jupyter notebook servers spawned on RC compute resources log to `~/.jupyterhub-spawner.log`. Watching the contents of this file provides useful information regarding any problems encountered during notebook startup or execution.

## IPython Clusters
Notebook servers started on RC compute resources can also launch IPython clusters for parallel processing. See [IPython Parallel](http://ipyparallel.readthedocs.org/en/latest/) and [MPI for Python](http://pythonhosted.org/mpi4py/) for general information on parallel processing with IPython clusters.

The RC environment provisions two IPython profiles automatically which can be used as a reference point for starting IPython clusters. These profiles are available in the _IPython Clusters_ tab.

#### `default`
The `default` profile is generated automatically by IPython. Engines are dispatched in the same resources as the notebook server, and provide no MPI support or cluster performance.

#### `example-shas`
Each `example-shas` engine provides access to a [Summit Haswell](https://www.rc.colorado.edu/support/user-guide/compute-resources.html#Summit) CPU thread. Multiple engines are aggregated into a single MPI session.

**Note:** IPython engines on RC cluster resources are provisioned as batch jobs using Slurm, but Jupyter does not yet report queue progress. The exception "NoEnginesRegistered: Can't build targets without any engines" indicates that the cluster job is still in the queue and not ready to accept work.

## Updating Your JupyterHub Config
_This only applies if you used JupyterHub at RC prior to September 2017._

The September 2017 update of our JupyterHub deployment deprecates some of the Jupyter and IPython configuration in your home directory. Updating to the new configuration _(which is required for documented features to work properly)_ is a manual process.

Start by removing the stale Jupyter config from your home directory:
```bash
rm -rf $HOME/.jupyter
```

Remove all IPython profiles for Crestone and Janus:
```bash
cd $HOME/.ipython
rm -rf profile_crestone-*
rm -rf profile_janus-*
```

The new configurations will be automatically applied the next time you start a notebook server.

## See Also
* [ JupyterHub Service Changelog ](JupyterHub-CHANGELOG)
* [[ Parallel Programming with Jupyter Notebooks ]]
