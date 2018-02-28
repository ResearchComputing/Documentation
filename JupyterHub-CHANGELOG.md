This page tracks changes to the CURC JupyterHub service, as well as changes planned for the future.

## Changelog

### 2017-09-25
* `/work/` mounts are now supported for Virtual Notebooks.
* Notebooks can now be spawned on Summit, and the Crestone spawn option has been deprecated.
* Ipyparallel profiles have been updated for Summit. To remove stale Janus/Crestone profiles, please follow the procedure described in the [JupyterHub User Guide](https://github.com/ResearchComputing/jupyter-at-rc/wiki/JupyterHub-User-Guide#updating-your-jupyterhub-config)
* Cluster notebooks now use lmod instead of virtualenv for software dependencies.
