This page tracks changes to the CURC JupyterHub service, as well as changes planned for the future.

## Changelog

### 2018-14-05
* Deprecated _Virtual Notebooks_. Only cluster notebooks are supported via JupyterHub.
* Added 2 and 12 hour notebook profiles.
* Added profiles for select Blanca groups.

### 2017-09-25
* `/work/` mounts are now supported for Virtual Notebooks.
* Notebooks can now be spawned on Summit, and the Crestone spawn option has been deprecated.
* Ipyparallel profiles have been updated for Summit. To remove stale Janus/Crestone profiles, please follow the procedure described in the [JupyterHub User Guide](https://github.com/ResearchComputing/jupyter-at-rc/wiki/JupyterHub-User-Guide#updating-your-jupyterhub-config)
* Cluster notebooks now use lmod instead of virtualenv for software dependencies.

Couldn't find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/1WoP_KtLp9lnTEsgW7Os-we45_JbEt3aUgS6j61jARnk/edit)
