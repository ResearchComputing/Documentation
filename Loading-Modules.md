## Overview

Research Computing uses a module system to load software . Most software is not accessible by default and must be loaded into the environment. This allows Research Computing to provide multiple versions of the software concurrently and enables users to switch easily between different versions of software.  

## Video Tutorial

[![How-to-load-modules-video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Loading-Modules/videopreview.j.jpg)](https://youtu.be/csgl4czhD_k)

## The module command

**Modules should only ever be loaded in job scripts, interactive jobs, or on compile nodes and should never be loaded directly on a login node.** The login node will restrict loading of modules, so you won't be able to access software unless you do so through a job or a compile node.

To see what modules are available to load, ssh into a compile node and type:
```
module avail
```
This will return a list of modules available to load into the environment. **Please note if you run this command on a login node you will not receive a full list of modules present on the system.**

To load your modules into the environment type:
```bash
module load some_module

# example: "module load python"
```

You can specify version by appending a `/` with the version number:
```bash
module load some_module/version 

# example: "module load python/3.5.1"
```

The Lmod hierarchical module system provides five layers to support programs built with compiler and library consistency requirements. A module’s dependencies must be loaded before the module can be loaded.
The Layers include:
+ Independent programs
+ Compilers
+ Compiler dependent programs
+ MPI implementations
+ MPI dependent programs 

If you cannot load your module because of dependencies, you can use the `module spider` to find what dependencies you need to load your module.
```bash
module spider some_module

#example: "module spider openmpi"
```

## Loading Modules in a job script

Loading a module will set or modify a user’s environment variables. Additionally, modules will enable access to the software package provided by that module. This can be useful in interactive jobs or in job-scripts that are dependent on software like python.

Modules in a job script can be loaded after your `#SBATCH` directives and before your actual executable is called. A sample job script that loads python into the environment is provided below:

```bash
#!bin/bash
#SBATCH 
#SBATCH 
#SBATCH 
#SBATCH 
#SBATCH 
#SBATCH 

module purge
module load python/3.5.1

python3 hello-world.py

## Table of Sub-Commands
The `module` command has a variety of sub-commands, outlined in the table below. You may shorten the command to `ml`, but the shortened command may require specialized syntax.

Command                 | Shortened Command            | Description  | Example |
----------------------- | ---------------------------- | ------------ | --------|
`module avail`          | `ml av`                      | List available software. Modules not listed here may have unmet dependencies which must be loaded for the module to be available. | `module avail`
`module spider <module>`| `ml spider <module>`         | Searches for a particular software. | `module spider openmpi`
`module load <module>`  | `ml <module>`                | Load a module to use the software. In this example we are loading the GNU Compiler Collection. The default version will load because we have not specified a version. | `module load gcc`
`module load <module>/<version>` | `ml <module>/<version>`      | Load GCC version 6.1.0 | `module load gcc/6.1.0`
`module unload <module>`     | `ml -<module>`               | Remove or unload a module | `module unload gcc`
`module swap <module> <new_module>` | `ml -<module> <new_module>`  | Swap a module. In this example we are unloading GCC and loading Intel. Any GCC-dependent modules will also be unloaded, and the intel-dependent versions (if available) will be loaded in their place. | `module swap gcc intel`
`module purge`          | `ml purge`                   | Remove all modules. The `slurm` module will not be unloaded with this purge because it is sticky. Use the `--force` flag to unload a sticky module. | `module purge`
`module save <name>`       | `ml save <name>`            | Save the state of all loaded modules. In this example, we are saving all loaded modules as a collection called `foo` | `module save foo`
`module restore <name>`    | `ml restore <name>`  | Restore a state of saved modules. In this example, we are restoring all modules that were saved as the collection called `foo` | `module restore foo`
`module help`           |                   | Find information about additional module sub-commands. | `module help`
