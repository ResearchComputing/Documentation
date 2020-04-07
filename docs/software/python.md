# Python and R with Anaconda

To support the diverse _python_ and _R_ workflows and high levels of customization Research Computing users require, [Anaconda](http://anaconda.com) is installed on the CURC system. Anaconda uses the _conda_ package manager to easily install software and associated packages, and supports _python_, _R_, and many other applications. The following documentation describes how to activate the CURC Anaconda distribution and our default environments, as well as how to create and activate your own custom Anaconda environments. Additional documentation on the [CURC JupyterHub](../gateways/jupyterhub.md) is available for users desiring to interact with their custom environments via [Jupyter notebooks](https://jupyter.org). 

_Note: CURC also hosts several legacy python and R modules for those users who prefer modules over Anaconda. Type `module spider python` or `module spider R` for a list of available versions. We recommend using Anaconda._

## Configuring conda with `.condarc`

The conda package manager allows modification of default settings to be done through a text file known as the `.condarc`. This file exists within a user's `/home/$USER/` directory and can be quickly be accessed using the file's full path at `~/.condarc`.

Your `/home/$USER` directory is small -- only 2 GB. By default, conda puts all package source code and environments in your `/home/$USER` directory , and it will quickly become full. The steps here modify the conda configration file to change the default locations of for packages and environments to your larger `/projects/$USER` directory.

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

Note that there is [a varaitey of settings you can customize using the .condarc file](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html).

## Using the CURC Anaconda environment
Follow these steps from a Research Computing terminal session on a Summit `scompile` node or within a Summit/Blanca batch or interactive job.

### Activate the CURC Anaconda environment:

Loading the CURC Anaconda enviornment is a little different compared to other software on Summit. Run the following command to initialize the base Anaconda software:

```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/latest
```

___Note__: The command above activates the base envioronment for python3, which as of 2020 is the only supported python standard. For users requiring legacy python2, you can still use conda to create a custom environment with the python2.X version of your choice (we provide an example of how to do this below)_. 

You will know that you have properly activated the environment because you should see `(base)` in front of your prompt. E.g.: 

```
(base) [johndoe@shas0137 ~]$
```

### Using Conda:

Now that you have activated the _base_ conda environment, you can use conda for _python_ and _R_!  There are two ways forward, depending on your needs.  You can:

__1. Use one of CURC's pre-installed environments.__
* Pros: You can begin using one of these immediately, and they contain mainy of the most widely used python and R packages. 
* Cons: These are root-owned environments, so you can't add additional packages. 

or

__2. Create your own custom environment(s).__
* Pros: You own these, so you can add packages as needed, control package versions, etc.
* Cons: There really aren't any cons, other than the time needed to create a custom environment (usually 5-30 minutes depending on the number of packages you install).     

Both options are discussed below.

#### Using one of CURC's pre-installed enviroments:

To use the CURC Intel Python distribution or _"idp"_ (python v3.6.8), run the following command with Anaconda initialized:

```
(base) [johndoe@shas0137 ~]$ conda activate idp
```

You will know that you have properly activated the environment because you should see `(idp)` replace the `(base)` in front of your prompt. Now the intel python distribution is loaded into your enviornment and can be accessed with the `python` command.

To see the python packages available in the _"idp"_ environment, you can type `conda list`.   

Similarly to use the CURC R distribution (R v3.6.0), run the following command with Anaconda initialized:

```
(base) [johndoe@shas0137 ~]$ conda activate rstudio
```

You will know that you have properly activated the environment because you should see `(rstudio)` in front of your prompt. To see the R packages available in the environment, you can type `conda list`. Now, you can use R as you normally would. 

Because interactive development is more easily done locally, most CURC R users exclusively run R code within batch jobs. Should you need to use rstudio on top of R for interactive development on Summit, you can login to our system with X11-forwarding (`ssh -X`) and initiate an rstudio session from within an interactive job.  



#### Create your own custom environment:

\*Note: In the examples below the environment is created in `/projects/$USER/software/anaconda/envs`, which is specified under `envs_dirs` in your `.condarc file`. Environments can be installed in any user-writable location the user chooses; just add the path to `~/.condarc`.

__1. Initialize Anaconda if you haven't already done so:__
 
```
[johndoe@shas0137 ~]$ source /curc/sw/anaconda3/latest
(base) [johndoe@shas0137 ~]$ 
```

__2. Create a custom environment:__

Here we create a new environment called _mycustomenv_ (you can call it anything you want!)
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv
```

If you want a specific version of python or R, you can modify the above commmand as follows (e.g.): 
_Python v2.7.16:_
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv python==2.7.16
```

_Python v3.6.8:_
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv python==3.6.8
```

_Latest version of R:_
```
(base) [johndoe@shas0137 ~]$ conda create -n mycustomenv r-base
```

__3. Activate your new environment:__

```
(base) [johndoe@shas0137 ~]$ conda activate mycustomenv
```

If successful, your prompt will now be preceded with `(mycustomenv)`.

__4. Install needed packages in your new environment:__

The best way to do this for python packages is to install everything you need with one command, because it forces conda to resolve package conflicts.  E.g.,:

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install numpy scipy tensorflow
```

For R packages, it is easiest to start an R session and install the packages as you normally would with "install.packages".  E.g.,:

```
(mycustomenv) [johndoe@shas0137 ~]$ R
>install.packages("ggplot2")
```

### Basic conda commands to get you started:

__List the packages currently installed in the environment__

```
(mycustomenv) [johndoe@shas0137 ~]$ conda list
```

__List the conda environments currently available__

```
(base) [johndoe@shas0137 ~]$ conda env list
```

__Add a new package named "foo" to your _custom_ environment__

```
(mycustomenv) [johndoe@shas0137 ~]$ conda install foo 
```

__Deactivate an environment:__

```
(mycustomenv) [johndoe@shas0137 ~]$ conda deactivate
```

### Troubleshooting

If you are having trouble loading a package, you can use `conda list` or `pip freeze` to list the available packages and their version numbers in your current conda environment. Use `conda install <packagname>` to add a new package or `conda install <packagename==version>` for a specific verison; e.g., `conda install numpy=1.16.2`.

Sometimes conda environments can "break" if two packages in the environment require different versions of the same shared library. In these cases you try a couple of things.
* Reinstall the packages all within the same install command (e.g., `conda install <package1> <package2>`). This forces conda to attempt to resolve shared library conflicts. 
* Create a new environment and reinstall the packages you need (preferably installing all with the same `conda install` command, rather than one-at-a-time, in order to resolve the conflicts).

### See Also

* [CURC JupyterHub](../gateways/jupyterhub.md)
