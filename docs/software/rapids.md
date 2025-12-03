# RAPIDS

NVIDIA RAPIDS allows researchers to adapt existing CPU-based Python data analytics and machine learning workflows for GPU acceleration with relatively small code changes. 

## Using our RAPIDS Environment

```{note}
This environment contains only the basic packages required to run RAPIDS and Python 3.13. If you'd like to install additional packages for use alongside RAPIDS, please follow the instructions at the bottom to create your own custom environment.
```

1. Start an interactive session on an NVIDIA GPU compute node, or create a batch script.

```
sinteractive --ntasks=10 --gres=gpu:1 --nodes=1 --qos=testing --time=01:00:00 --partition=atesting_a100
```

2. Load the miniforge module:

```
module load miniforge
```

3. Activate the environment:

```
mamba activate /curc/sw/conda_env/rapids-25.10
```

## Creating a Custom RAPIDS Environment

1. Start an interactive session on a GPU node:

```
sinteractive --ntasks=10 --gres=gpu:1 --nodes=1 --qos=testing --time=01:00:00 --partition=atesting_a100
```

3. Load the miniforge module to use Mamba:

```
module load miniforge
```

5. Install RAPIDS:

```
mamba create -n rapids-25.10 -c rapidsai -c conda-forge -c nvidia  \
    rapids=25.10 python=3.13 'cuda-version>=12.0,<=12.9'
```

7. Activate the environment:

`mamba activate rapids-25.10`

RAPIDS is now ready for use!
