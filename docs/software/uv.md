# uv

To support fast and reproducible Python workflows, CURC now provides [uv](https://docs.astral.sh/uv/), a modern Python package and environment manager developed by Astral. `uv` is implemented in Rust and is designed for speed, reliability, and Python-native workflows using `venv`. `venv` is the standard tool in Python for creating lightweight, isolated environments. Each environment created with `venv` has its own directory with a Python interpreter and a separate set of installed packages. 

```{note}
**uv is a new and actively developed tool.**  Because it is still evolving, new versions and features are released frequently. CURC will aim to keep this tool updated, but we cannot guarantee that the module will always reflect the absolute latest release.

```

## Using `uv` on CURC

### Loading the `uv` Module

To start using `uv`, you must first load the relevant module in your interactive session:

```
module load uv
```

```{important}
Loading the `uv` module sets a key environment variable `$UV_ENVS`. This environment variable specifies the default directory where `uv` will create virtual environments. This path is set to:
`/projects/$USER/software/uv/envs`
This directory gets created for you the first time you load `uv`. You do not need to manually create it.

```

```{note}
**What Is venv?**

`venv` is the standard tool in Python for creating lightweight, isolated environments. Each environment created with venv has its own directory with a Python interpreter and a separate set of installed packages. This helps avoid conflicts between different projects or dependencies. 

`uv` builds on top of `venv`, offering a faster and more user-friendly experience, especially for managing packages and Python versions.

```

### View run options

To view a list of all available commands and options for `uv`, run:

```
uv --help
```

You can also see additional help for each command by running:

```
uv <command> --help
```

For example, to get detailed help for creating a virtual environment with `uv venv`, run:

```
uv venv --help
```

### Creating a Virtual Environment with `uv`

Once the `uv` module is loaded, you can create a new Python virtual environment by running:

```
$ uv venv $UV_ENVS/mycustomenv
```

This will create a virtual environment named `mycustomenv` in the directory specified by the `$UV_ENVS` environment variable.

### Specifying Python Versions with `uv`

You can create virtual environments with specific Python versions using the `--python` flag.

```
$ uv venv $UV_ENVS/mycustomenv --python 3.8
```

```{important}
While  `uv` can be used with beta versions of Python, this is not recommended, as many community-contributed modules may not function correctly until an official Python release is available.
```

### Activate the virtual environment

To activate the environment, use the command:

```
$ source $UV_ENVS/mycustomenv/bin/activate
```
### Deactivate the virtual environment

To deactivate the environment, use the command:

```
$ deactivate
```

### Using Python with `uv`

After activating the virtual environment, you can install Python packages using `uv`'s `pip` interface. For example, to install a package named `numpy`, run:

```
(mycustomenv) $ uv pip install numpy
```

This will install the `numpy` package in the active virtual environment.

```{tip}
To manage disk usage, you can clear unused or outdated files from `uv's` cache directory using: `uv cache clean`. This command removes cached Python builds, packages, and temporary files. This is useful if you regularly install new packages or Python versions.
```

### Removing a `uv` Environment

If you want to remove a `uv` environment, run:
```
$ rm -rf $UV_ENVS/mycustomenv
```

```{warning}
Be very careful when using the `rm -rf` command. This command will permanently delete the specified directory and all of its contents, with no confirmation prompt. Make sure you are deleting the correct environment and that you don't need any of its files before running this command.
```

## Example Job Script

Here’s an example Slurm job script for running a Python task within a `uv` virtual environment.

``` bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=06:00:00
#SBATCH --partition=aa100
#SBATCH --qos=normal
#SBATCH --job-name=python_task
#SBATCH --output=python_task_%j.out
#SBATCH --ntasks=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<your email address>

module purge
module load uv

# Activate the virtual environment
source $UV_ENVS/mycustomenv/bin/activate

# Run your Python script or command
python myscript.py
```

### Additional Resources

-  `uv` Documentation: [https://astral.sh/blog/uv/](https://astral.sh/blog/uv/)

- Python `venv` Documentation: [https://docs.python.org/3/library/venv.html](https://astral.sh/blog/uv/)