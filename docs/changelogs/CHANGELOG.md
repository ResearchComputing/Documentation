## CHANGELOG

### Thursday, 13 January 2022

* 2022 Q1 Documentation Review
> Major Changes:
> - Add Alpine resources/documentation
> - Source Anaconda: `source /curc/sw/anaconda3/latest` -> `module load anaconda`
> - FAQ page added to PetaLibrary

### Tuesday, 2 November 2021

* Adding CUmulus documents for CUmulus beta release

### Wednesday, 27 October 2021

* Stable version of documents set: 1.0.0

### Wednesday, 17 October 2018

* Configured Slurm to reject invalid jobs during queueing, rather than accept and pend forever

### Wednesday, 16 May 2018

* [Shut down legacy login nodes](https://www.colorado.edu/rc/news/rcloginnodemigration)

### Wednesday, 9 May 2018

* [Moved login.rc.colorado.edu to a new set of login nodes](https://www.colorado.edu/rc/news/rcloginnodemigration)

### Tuesday, 27 February 2018

* [Reduced memory limits on Summit](https://www.rc.colorado.edu/node/1094)

### Tuesday, 20 February 2018

* Installed version control clients on Summit in response to a request for Mercurial

### Monday, 19 February 2018

* [Reduced default per-core memory requests on Summit](https://www.rc.colorado.edu/node/1094)

### 25 September 2017

* `/work/` mounts are now supported for JupyterHub Virtual Notebooks.

* JupyterHub Notebooks can now be spawned on Summit, and the Crestone
  spawn option has been deprecated.

* JupyterHub Ipyparallel profiles have been updated for Summit. To
  remove stale Janus/Crestone profiles, please follow the procedure
  described in the
  [JupyterHub User Guide](https://github.com/ResearchComputing/jupyter-at-rc/wiki/JupyterHub-User-Guide#updating-your-jupyterhub-config)

* JupyterHub Cluster notebooks now use lmod instead of virtualenv for
  software dependencies.

Couldn't find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/1WoP_KtLp9lnTEsgW7Os-we45_JbEt3aUgS6j61jARnk/edit)
