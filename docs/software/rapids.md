# CUDA-X (Formerly RAPIDS)

[NVIDIA CUDA-X](https://developer.nvidia.com/topics/ai/data-science/cuda-x-for-data-science?size=n_6_n&sort-field=featured&sort-direction=desc) allows researchers to adapt existing CPU-based Python data analytics and machine learning workflows for GPU acceleration with relatively small code changes. 

```{note}
Beginning August 11, 2026, the NVIDIA RAPIDS brand will transition to NVIDIA CUDA-X. All library functionality remains the same. However, during this transition, much of the documentation may continue to reference RAPIDS and/or CUDA-X. Please note that both refer to the same set of NVIDIA supported tools and libraries. 
```

## Using our CUDA-X Environment

```{note}
This environment contains only the basic packages required to run CUDA-X and Python 3.13. If you'd like to install additional packages for use alongside CUDA-X, please follow the instructions at the bottom to create your own custom environment.
```

1. Start an interactive session on an NVIDIA GPU compute node, or create a batch script.

```
sinteractive --partition=aa100 --qos=gpu-testing --ntasks=10 --gres=gpu:a100_3g.20gb:1 --nodes=1 --time=01:00:00 
```

2. Load the miniforge module:

```
module load miniforge
```

3. Activate the environment:

```
mamba activate /curc/sw/conda_env/rapids-25.10
```

4. Start using CUDA-X in your Python code! The [CUDA-X user guide](https://docs.nvidia.com/datascience/user-guide/) has some great examples.

## Creating a Custom CUDA-X Environment

```{note}
The example below is for installing CUDA-X version 26.08.  Information on installing the most recent version can be found in the [CUDA-X installation guide](https://docs.nvidia.com/datascience/install/).
```
1. Start an interactive session on a GPU node:

```
sinteractive --partition=aa100 --qos=gpu-testing --ntasks=10 --gres=gpu:a100_3g.20gb:1 --nodes=1 --time=01:00:00 
```

3. Load the miniforge module to use Mamba:

```
module load miniforge
```

5. Install CUDA-X:

```
mamba create -n rapids-26.08 -c rapidsai -c conda-forge rapids=26.08 python=3.14 'cuda-version>=13.0,<=13.3'
```

7. Activate the environment:

```
mamba activate rapids-26.08
```

8. Start using CUDA-X in your Python code! The [CUDA-X user guide](https://docs.nvidia.com/datascience/user-guide/) has some great examples.
