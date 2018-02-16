Research Computing uses a module system for loading software. Most software is not accessible by default and has to be loaded. This allows Research Computing to provide multiple versions of the software concurrently and enables users to switch easily between different versions of software.  

Loading a module:
+ Sets or modifies a user’s environment variables
+ Enables access to the software package provided by that module  

The Lmod hierarchical module system:
+ Five layers to support programs built with compiler and library consistency requirements
+ A module’s dependencies must be loaded before the module can be loaded
+ Layers include
    - Independent programs
    - Compilers
    - Compiler dependent programs
    - MPI implementations
    - MPI dependent programs

Need more assistance? Watch a tutorial video or read the template

## Video:

+ [Loading Modules](https://youtu.be/csgl4czhD_k)

## Template:

Loading Modules Template

The module command has a variety of sub-commands, outlined in the table below.
You may shorten the command to `ml`, but the shortened command requires different syntax.
- Loading modules in Slurm jobs
    + Load modules in your job script
         * Do this if an application running in a Slurm job needs access to any module-provided software packages
    + In script, place module load commands
         * After #SBATCH directives
         * Before the actual executable is called

Command          | Shortened Command | Description
---------------- | ----------------- | -------------
`module avail`   | `ml av`           | List available software. Modules not listed here may have unmet dependencies which must be loaded for the module to be available. 
`module spider`  | `ml spider`       | Searches for a particular software
`module load gcc`| `ml gcc`          | something


