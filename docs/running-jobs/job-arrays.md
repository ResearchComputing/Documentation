```{warning}
This page assumes you are already familiar with the basics of writing and submitting SLURM batch job scripts. If you are new to batch jobs, please review our documentation on [batch jobs](./batch-jobs.md) before continuing. 

```

# Scaling Up with Job Arrays

Job arrays in SLURM simplify the running of multiple similar jobs. Instead of creating and submitting a separate batch script for each job, you use a single template script. SLURM then automatically generates and schedules each job, or {ref}`task <jobarray-note-interactive>`, in the array, saving you time and effort. Job arrays are best suited for workflows where the core computational task is consistent, but the input data and/or parameters vary for each run. 

Common job array scenarios include:

* **Processing multiple data files:** <br> Running the same analysis script on a large dataset where each file is processed as a separate, independent job.

* **Parameter sweeping:** <br> Executing simulations or models with a wide range of input parameters to explore a parameter space.

* **Monte Carlo simulations:** <br> Performing thousands or millions of independent trials to estimate a numerical result.

* **High-throughput computing:** <br> Launching a large number of short, non-communicating jobs that can be run in parallel.


(jobarray-note-interactive)=
```{note}
In the context of a job array, SLURM refers to the individual "jobs" within the array as "tasks". To avoid any confusion, we will use that same language here. 
```


## Elements of a Job Array
To convert a standard batch script into a job array, you will need to make three changes:

  1. Include the `--array` directive
  2. Modify the `--output` directive to include `%A` and `%a`
  3. Update your code to utilize the Job Array Environment Variables 

Below is an example script that includes all three of these changes to create a job array with 3 tasks. 

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --partition=atesting
#SBATCH --qos=testing
#SBATCH --array=1-3                # 1 - Set Array Indexes
#SBATCH --output=example-%A-%a.out # 2 - Add the Job ID and Task ID for each array task

module purge

# 3 - If necessary, update your script to use the Task ID. 
#     This ensures each task will run its assigned workflow

echo "This task's index is $SLURM_ARRAY_TASK_ID "
echo "This job array has $SLURM_ARRAY_TASK_COUNT tasks"
echo "The array's Job ID is $SLURM_ARRAY_JOB_ID"
echo "The task's Job ID is $SLURM_JOB_ID"
echo "The combined array Job ID and Task ID is ${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}"

```

```{note}
In order for SLURM to treat a batch script as a Job Array, it must include the `--array` directive. This can be added directly to the script, like in the example above, or added as a command-line argument when submitting the job (e.g., `sbatch --array=1-3 example.sh`). 

Also, please be aware that a job array can only be created from a [batch script](./batch-jobs.md). You cannot use the `--array` directive with [interactive sessions](./interactive-jobs.md).
```

```{important}
The tasks in a job array are not guaranteed to run simultaneously or in any specific order. Therefore, you must write your batch script so that each task can run independently. If your tasks must execute in a particular sequence, you may need to include the `--dependency` directive. 

Further information on the `--dependency` directive can be found in [SLURM's documentation](https://slurm.schedmd.com/job_array.html#dependencies).
```

## Task Indexes

The `--array` directive provides three methods for defining the job array's task indexes: 
  * a range with a default step size of 1
  * a range with a specific step size
  * or a list of specific index values

An example of each of these is provided below. 

(tabset-ref-ex-job-array-config)=
`````{tab-set}
:sync-group: tabset-ex-job-array-config

````{tab-item} Default Step
:sync: ex-job-array-config-range

Request 3 Jobs with Indexes 1, 2, and 3
```bash
#SBATCH --array=<START>-<STOP> 
#SBATCH --array=1-3
```

````

```` {tab-item} Specific Step Size
:sync: ex-job-array-config-basic-step

Request 4 Jobs with Indexes 3, 6, 9, and 12
```bash
#SBATCH --array=<START>-<STOP>:<STEP>
#SBATCH --array=3-12:3 
```

````

```` {tab-item} List of Indexes
:sync: ex-job-array-config-basic-list

Request 5 Jobs with Indexes 10, 45, 83, 96, and 103
```bash
#SBATCH --array=<INDEX 1>,<INDEX 2>,<INDEX N>
#SBATCH --array=10,45,83,96,103
```

````

```` {tab-item} Limiting Concurrent Tasks
You can limit the number of tasks that can run concurrently, i.e., at the same time, by adding the `%` modifier. This can be necessary when submitting job arrays that request a large number of tasks and/or a large number of resources per task. Without the `%` modifier, all of the tasks will try to run at once, which might cause your RC account to hit the system's resource limits and prevent you from running other jobs on a given partition and/or the cluster itself. 

To see the current resource limits for jobs submitted to the Alpine cluster, please check the [Quality-of-Service table](../clusters/alpine/alpine-hardware.md#quality-of-service-qos) and the [Partitions table](../clusters/alpine/alpine-hardware.md#partitions).

```bash

#SBATCH --array=<INDEXES>%<# OF CONCURRENT JOBS> 

# Limit to 2 concurrent jobs
#SBATCH --array=1-10%2 
```
````

`````

```{important}
Currently, a single job array is limited to, at most, {{ alpine_max_number_array_jobs }} tasks. This limit is in place to protect the SLURM controller and ensure it isn't overwhelmed trying to track too many tasks for a given user.

Please, be careful that you do not submit a large number of concurrent job arrays; this too can overwhelm the SLURM controller. To protect the stability of the cluster, Research Computing reserves the right to suspend and/or cancel any jobs that overwhelm the system. 

If you have questions about submitting large job arrays and/or multiple job arrays, please reach out to us at <rc-help@colorado.edu>.
```

## Output Filenames
To differentiate the output files generated by each task, it is important to include `%A` (`SLURM_ARRAY_JOB_ID`) and `%a` (`SLURM_ARRAY_TASK_ID`) in the filename. These can be included in both the `--output` and `--error` SBATCH directives, like so: 

```bash
#SBATCH --output=example-%A-%a.out
#SBATCH --error=example-%A-%a.err
```

## Environment Variables

SLURM provides a set of environment variables specific to job arrays. Those variables are listed and defined in the table below. 

| Variable  | Description                                                      | 
| :-------------------------- | :--------------------------------------------- |
| SLURM_JOB_ID                | The unique Job ID of a task in the array        |
| SLURM_ARRAY_JOB_ID          | The primary Job ID shared by all tasks in the array |
| SLURM_ARRAY_TASK_ID         | The specific index of a task in the array       |
| SLURM_ARRAY_TASK_COUNT      | The number of tasks within the array            |
| SLURM_ARRAY_TASK_MAX        | The highest index in the array                 |
| SLURM_ARRAY_JOB_MIN         | The lowest index in the array                  |

As an example, if a job array was submitted with `--array=1-3`. It would result in a set of three tasks with values similar to these: 

```bash
# 1
SLURM_JOB_ID=507
SLURM_ARRAY_JOB_ID=505
SLURM_ARRAY_TASK_ID=1
SLURM_ARRAY_TASK_COUNT=3
SLURM_ARRAY_TASK_MAX=3
SLURM_ARRAY_TASK_MIN=1

# 2
SLURM_JOB_ID=506
SLURM_ARRAY_JOB_ID=505
SLURM_ARRAY_TASK_ID=2
SLURM_ARRAY_TASK_COUNT=3
SLURM_ARRAY_TASK_MAX=3
SLURM_ARRAY_TASK_MIN=1

# 3
SLURM_JOB_ID=505
SLURM_ARRAY_JOB_ID=505
SLURM_ARRAY_TASK_ID=3
SLURM_ARRAY_TASK_COUNT=3
SLURM_ARRAY_TASK_MAX=3
SLURM_ARRAY_TASK_MIN=1
```

## Canceling Job Arrays and Tasks
You can use `scancel` to cancel all of the tasks or a specific set of tasks in a job array. 

  * Cancel an individual task 

    ```
    scancel <SLURM_ARRAY_JOB_ID>_<SLURM_ARRAY_TASK_ID>
    scancel 505_3
    ```
  * Cancel a subset of tasks

    ```
    scancel <SLURM_ARRAY_JOB_ID>_[<SLURM_ARRAY_TASK_ID>-<SLURM_ARRAY_TASK_ID>]
    scancel 505_[2-3]
    ```
  * Cancel all tasks

    ```
    scancel <SLURM_ARRAY_JOB_ID>
    scancel 505
    ```


## Example Batch Scripts

### Assigning Data to Tasks

This example shows you how to organize your data so it's "job array friendly" by giving each task its own data file to process. One way to do this is to break your data into smaller files and name each file with a specific task id.

Here's how it works in this example:
  * You create a job array batch script.
  * You name the data files with the task ids (e.g., `DATA_1.csv`).
  * In the batch script, use the `SLURM_ARRAY_TASK_ID` so that each task only reads its assigned file.

```bash
#!/bin/bash
#SBATCH --time=00:00:10
#SBATCH --partition=amilan
#SBATCH --qos=normal
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --job-name=Array_Example_Multiple_Files
#SBATCH --output=files.%A_%a.out
#SBATCH --array=1-3

module purge

# Prints the contents of the assigned data file to the standard output.
cat "DATA_${SLURM_ARRAY_TASK_ID}.csv"
```


### Assigning Parameters to Tasks

This example shows how to assign unique parameters to each task in a job array. The parameters are stored in a text file called `parameters.txt`.

Here's how it works:
* A batch script creates a job array with five tasks.
* Each task uses the `sed` command to read its specific parameters from `parameters.txt`.
* These parameters are then passed to a Python script, `cars_mpg.py`, which prints them out.

You can use this method with any program that takes command-line arguments, not just Python. For more on the `sed` command, review its help page by running `sed --help`.

Batch Script:
```bash
#!/bin/bash
#SBATCH --time=00:00:10
#SBATCH --partition=amilan
#SBATCH --qos=normal
#SBATCH --nodes=1 
#SBATCH --ntasks=1 
#SBATCH --job-name=cars
#SBATCH --output=cars.%A_%a.out
#SBATCH --array=1-5

module purge
module load miniforge

# run workflow
python cars_mpg.py $(sed -n "${SLURM_ARRAY_TASK_ID}p" parameters.txt)
```

Python Script: 
```python
import sys

car=sys.argv[1]
mpg=sys.argv[2]

print("The " + car + " gets " + mpg + " mpg.")
```

Input File (parameters.txt):
```bash
mustang 25
pinto 30
chevette 33
nova 21
cutlass 23
```
````


```{seealso}
If you would like to learn more about Job Arrays, please see the official [Job Array Support page](https://slurm.schedmd.com/job_array.html). 
```