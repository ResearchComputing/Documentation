# The Modules System

Research Computing uses a module system to load most software into a
user's environment. Most software is not accessible by default and
must be loaded in. This allows Research Computing to provide multiple
versions of the software concurrently and enables users to easily switch 
between different versions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/csgl4czhD_k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


## The `module` Command

**_Modules should be loaded in job scripts, interactive jobs, or on
compile nodes only. They should not be loaded when on one of the
login nodes._** The login node will restrict the loading of modules,
so you won't be able to access software unless you do so through a job
or a compile node.

To see what modules are available to load, ssh into a compile node by
typing `acompile` from a login node, and type:

```
module avail
```

This will return a list of modules available to load into the
environment. **_Please note if you run this command on a login node
you will not receive a list of modules present on the system._** It is also important to note that if a module has dependencies, you may not see the module listed until dependencies are loaded.  

To load your chosen modules into the environment type:

```bash
module load some_module

# example: "module load python"
```

You can specify the version of the software by appending a `/` with
the version number:

```bash
module load some_module/version 

# example: "module load python/3.5.1"
```

The Lmod hierarchical module system provides five layers to support
programs built with compiler and library consistency requirements. A
module’s dependencies must be loaded before the module can be loaded.

The Layers include:

+ Independent programs
+ Compilers
+ Compiler dependent programs
+ MPI implementations
+ MPI dependent programs 

If you cannot load a module because of dependencies, you can use the
`module spider` to find what dependencies you need to load the module.

```bash
module spider some_module

# example: "module spider openmpi"
```

## Subcommands

The `module` command has a variety of subcommands, outlined in the
table below. You may shorten the command to `ml`, but the shortened
command may require specialized syntax.

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

## Loading Modules in a Job Script

Loading a module will enable access to the modules 
described software package. Additionally, modules 
will set or modify a user’s environment
variables.

Modules in a job script can be loaded after your `#SBATCH` directives
and before your actual executable is called. A sample job script that
loads Python into the environment is provided below:

```bash
#!bin/bash
#SBATCH --nodes=1
#SBATCH --time=00:01:00
#SBATCH --ntasks=1
#SBATCH --job-name=test-job
#SBATCH --output=test-job.%j.out

module purge
module load python/3.5.1

python3 test-program.py
```

