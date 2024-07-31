# Terminal application

The _Clusters_ menu provides shell access to login nodes on CURC clusters. The shell terminal is similar to many other tools that provide terminal access.

<br>

![](OnDemand/shell_access.png)

* __Alpine:__ The Alpine tab will launch a terminal that RC users can use to manually access an RC Login node. After the tab opens, type your CURC password and accept the Duo push to your phone, which will complete the login to the terminal.

> **NOTE:** Currently, Alpine shells log you into a basic login node. You can 
load in either Alpine or Blanca slurm instances from here: `module load 
slurm/<cluster>` with either Alpine or Blanca.