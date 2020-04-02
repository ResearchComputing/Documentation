# Using Python and R with Anaconda

To support the diverse _python_ and _R_ workflows and high levels of customization Research Computing users require, [Anaconda](http://anaconda.com) is installed on the CURC system. Anaconda uses the _conda_ package manager to easily install software and associated packages, and supports _python_, _R_, and many other applications. The following documentation describes how to activate the CURC Anaconda distribution and our default environments, as well as how to create and activate your own custom Anaconda environments. Additional documentation on the [CURC JupyterHub](../gateways/jupyterhub.md) is available for users desiring to interact with their custom environments via [Jupyter notebooks](https://jupyter.org). 

_Note: CURC also hosts several legacy python and R modules for those users who prefer modules over Anaconda. Type ```module spider python``` or ```module spider R``` for a list of available versions. We recommend using Anaconda.

## Using the CURC Anaconda environment

Follow these steps from a Research Computing terminal session on a Summit `scompile` node or from an interactive session on a Blanca compute node. 

### Modify your ~/.condarc file so that packages are downloaded to your _/projects_ directory 

Your _/home/$USER_ directory (also denoted with "_~_") is small -- only 2 GB. By default, conda downloads packages to your home directory when creating a new environment, and it will quickly become full. The steps here modify the conda configration file, called _~/.condarc_, to change the default location of _pkgs_dirs_ so that the packages are downloaed to your (much bigger) _/projects_ directory.

Open your _~/.condarc_ file in your favorite text editor (e.g., nano):
_(note: this file may not exist yet -- if not, just create a new file with this name)_
```
[johndoe@shas0137]$ nano ~/.condarc
```

...and paste the following four lines:
```
pkgs_dirs:
  - /projects/$USER/.conda_pkgs
envs_dirs:
  - /projects/$USER/software/anaconda/envs
```

...then save and exit the file. You won't need to perform this step again -- it's permanent unless you modify _~/.condarc_ later.

Note that there are lots of other things you can customize using the [~/.condarc file](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html).

### Activate the CURC Anaconda environment:

```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/latest
```

___note__: The command above activates the base envioronment for python3, which as of 2020 is the only supported python standard. For users requiring legacy python2, you can still use conda to create a custom environment with the python2.X version of your choice (we provide an example of how to do this below)_. 

You will know that you have properly activated the environment because you should see _`(base)`_ in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$
```

### Using Conda:

Now that you have activated the _base_ conda environment, you can use conda for _python_ and _R_!  There are two ways forward, depending on your needs.  You can:

_1. Use one of CURC's pre-installed environments._ 
* Pros: You can begin using one of these immediately, and they contain mainy of the most widely used python and R packages. 
* Cons: These are root-owned environments, so you can't add additional packages. 

or

_2. Create your own custom environment(s)._
* Pros: You own these, so you can add packages as needed, control package versions, etc.
* Cons: There really aren't any cons, other than the time needed to create a custom environment (usually 5-30 minutes depending on the number of packages you install).     

Both options are discussed next.

#### Using one of CURC's pre-installed enviroments:

To use the CURC Intel Python distribution (python v3.6.8):

```
(base) [johndoe@shas0137 ~]$ conda activate idp
```

You will know that you have properly activated the environment because you should see _`(idp)`_ in front of your prompt. To see the python packages available in the _idp_ environment, you can type `conda list`. Now, you can use _python_ as you normally would.  

To use the CURC R distribution (R v3.6.0):

```
(base) [johndoe@shas0137 ~]$ conda activate rstudio
```

You will know that you have properly activated the environment because you should see _`(rstudio)`_ in front of your prompt. To see the _R_ packages available in the _rstudio_ environment, you can type `conda list`. Now, you can use _R_ as you normally would.  Most users use _R_ on our system within batch jobs, rather than interactively (they find that doing interactive development of _R_ code is more convenient on their laptop).  However, should you need to use _rstudio_ on top of _R_ for interactive development on Summit, you can login to our system with X11-forwarding (`ssh -X`) and initiate an rstudio session from within an `sinteractive` job.  


#### Create your own custom environment:

*Note: In the examples below the environment is created in `/projects/$USER/software/anaconda/envs`, which is specified under `envs_dirs` in your ~/.condarc file. Environments can be installed in any user-writable location the user chooses; just add the path to ~/.condarc.

##### 1. Activate the _base_ conda environment if you haven't already done so:
 
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/latest
(base) [johndoe@shas0137 ~]$ 
```

##### 2. Create a custom environment:
 
_Here we create a new environment called _mycustomenv_ (you can call it anything you want!)_

```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv
```

 ...if you want a specific version of _python_ or _R_, you can modify the above commmand as follows (e.g.): 

...for _python_ v2.7.16:
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv python==2.7.16
```

...for _python_ v3.6.8
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv python==3.6.8
```
...for the latest version of _R_:

```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv r-base
```

##### 3. Activate your new environment:

```
(base) [johndoe@shas0137 ~]$ conda activate mycustomenv
```

If successful, your prompt will now be preceded with _(mycustomenv))_.

##### 4. Install needed packages in your new environment:

The best way to do this for _python_ packages is to install everything you need with one command, because it forces conda to resolve package conflicts.  E.g.,:

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install numpy scipy tensorflow
```

For _R_ packages, it is easiest to start an _R_ session and install the packages as you normally would with "install.packages".  E.g.,:

```
(mycustomenv) [johndoe@shas0137 ~]$ R
>install.packages("ggplot2")
```

### Basic conda commands to get you started:

#### To list the packages currently installed in the environment:

```
(mycustomenv) [johndoe@shas0137 ~]$ conda list
```

#### To list the conda environments currently available:

```
(base) [johndoe@shas0137 ~]$ conda env list
```

#### To add a new package named "foo" to your _custom_ environment:

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install foo 
```

#### To deactivate an environment:

```
(mycustomenv) [johndoe@shas0137 ~]$ conda deactivate
```

### Troubleshooting

If you are having trouble loading a package, you can use `conda list` or `pip freeze` to list the available packages and their version numbers in your current conda environment. Use `conda install <packagname>` to add a new package or `conda install <packagename==version>` for a specific verison; e.g., `conda install numpy=1.16.2`.

Sometimes conda environments can "break" if two packages in the environment require different versions of the same shared library.  In these cases you try a couple of things.
* Reinstall the packages all within the same _install_ command (e.g., `conda install <package1> <package2>`).  This forces conda to attempt to resolve shared library conflicts. 
* Create a new environment and reinstall the packages you need (preferably installing all with the same `conda install` command, rather than one-at-a-time, in order to resolve the conflicts).

### See Also

* [CURC JupyterHub](../gateways/jupyterhub.md)
