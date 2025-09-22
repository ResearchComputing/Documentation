# Scaling Up with Job Arrays

Job arrays streamline the submission and management of large collections of conceptually similar jobs where a single batch script serves as a template from which SLURM automatically generates and schedules each job, or {ref}`task <jobarray-note-interactive>`, in the array. This approach eliminates the need to manually create and submit each variation of the primary bash script, significantly simplifying the workflow for running numerous independent tasks.

Job arrays are best suited for workflows where the core computational task is consistent, but the input data and/or parameters vary for each run. Common scenarios include:

* **Processing multiple data files:** Running the same analysis script on a large dataset where each file is processed as a separate, independent job.

* **Parameter sweeping:** Executing simulations or models with a wide range of input parameters to explore a parameter space.

* **Monte Carlo simulations:** Performing thousands or millions of independent trials to estimate a numerical result.

* **High-throughput computing:** Launching a large number of short, non-communicating jobs that can be run in parallel.

```{warning}
This page assumes you already know the basics of writing and submitting SLURM batch scripts. If you are new to writing and submitting batch jobs, please review our documentation on [batch jobs](./batch-jobs.md) before continuing on. 

Please be aware that a job array can only be created from a [batch script](./batch-jobs.md). [Interactive sessions](./interactive-jobs.md) cannot be submitted with the `--array` directive.
```

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
echo "The shared Job ID for this array is $SLURM_ARRAY_JOB_ID"
echo "The unique Job ID for this specific task is $SLURM_JOB_ID"

```

```{note}
In order for SLURM to treat a batch script as a Job Array, it must include the `--array` directive. This can be added directly to the script, like in the example above, or added as a command-line argument when submitting the job (e.g. `sbatch --array=1-3 example.sh`). 
```

```{important}
The tasks in a job array are not guaranteed to run simultaneously or in any specific order. Therefore, it is crucial that you write your batch script so that each task in your job array can run independently. If your tasks must execute in a particular sequence, you will need to include the `--dependency` directive. Further information on the `--dependency` directive can be found in [SLURM's documentation](https://slurm.schedmd.com/job_array.html#dependencies).
```

## Setting the Job Array Indexes

The `--array` directive provides three methods for defining the job array's indexes: 
  * a range with a default step size of 1
  * a range with a specific step size
  * or a list of specific index values

An example of each of these is provided below. 

(tabset-ref-ex-job-array-config)=
`````{tab-set}
:sync-group: tabset-ex-job-array-config

````{tab-item} Setting a Range
:sync: ex-job-array-config-range

Request 3 Jobs with Indexes 1, 2, and 3
```bash
#SBATCH --array=<START>-<STOP> 
#SBATCH --array=1-3
```

````

```` {tab-item} Setting a Step Size
:sync: ex-job-array-config-basic-step

Request 4 Jobs with Indexes 3, 6, 9, and 12
```bash
#SBATCH --array=<START>-<STOP>:<STEP>
#SBATCH --array=3-12:3 
```

````

```` {tab-item} Setting a Specific List of Indexes
:sync: ex-job-array-config-basic-list

Request 5 Jobs with Indexes 10, 45, and 83
```bash
#SBATCH --array=<INDEX 1>,<INDEX 2>,<INDEX N>
#SBATCH --array=10,45,83,96,103
```

````

```` {tab-item} Limiting Concurrent Tasks
You can limit the number of tasks that can run cuncurrently, i.e. at the same time, by adding the `%` modifier. This can be necessary when submitting job arrays that request a large number of tasks and/or a large number of resources per task. Without the `%` modifier, all of the tasks will try to run at once, which might cause your RC account to hit the system's resource limits and prevent you from running other jobs on a given partition and/or the cluster itself. 

To see the current resource limits for jobs subbmitted to the Alpine cluster, please check the [Quality-of-Service table](../clusters/alpine/alpine-hardware.md#quality-of-service-qos) and the [Partitions table](../clusters/alpine/alpine-hardware.md#partitions).

```bash

#SBATCH --array=<INDEXES>%<# OF CONCURRENT JOBS> 

# Limit to 2 concurrent jobs
#SBATCH --array=1-10%2 
```
````

`````

```{important}
Currently, job arrays can contain at most {{ alpine_max_number_array_jobs }} tasks. Please do not submit a multiple large job arrays at the same time. Too many concurrent job arrays can overwhelm the SLURM controller. To protect the stability of the cluster, Research Computing reserves the right to suspend and/or cancel any jobs that overwhelm the system. 

If you have questions about submitting large job arrays, please reach out to us at <rc-help@colorado.edu>.
```

## Output Files
To differentiate the output files generated by each task, it is important to include the `%A` and `%a`, which SLURM will replace with their corresponding environment variables. `%A` refers to the `$SLURM_ARRAY_JOB_ID` and `%a` refers to the `$SLURM_ARRAY_TASK_ID`. These can be included in the `--output` and `--error` SBATCH directives: 

```bash
#SBATCH --output=example-%A-%a.out
#SBATCH --error=example-%A-%a.err
```

## Job Array Environment Variables

| Variable  | Description                                                      | 
| :-------------------------- | :--------------------------------------------- |
| SLURM_JOB_ID                | The unique Job ID of a task in the array        |
| SLURM_ARRAY_JOB_ID          | The primary Job ID shared by all tasks in the array |
| SLURM_ARRAY_TASK_ID         | The specific index of a task in the array       |
| SLURM_ARRAY_TASK_COUNT      | The number of tasks within the array            |
| SLURM_ARRAY_TASK_MAX        | The highest index in the array                 |
| SLURM_ARRAY_JOB_MIN         | The lowest index in the array                  |

SLURM provides a set of Job Array specific environment variables.  For example, `--array=1-3` will result in a set of three tasks which have values similar to these: 

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
You can use `scancel` to cancel all or a specific set of the tasks in a job array. 

  * Cancel an individual task
  ```bash
  scancel <SLURM_ARRAY_JOB_ID>_<SLURM_ARRAY_TASK_ID>
  scancel 505_3
  ```

  * Cancel a subset of tasks
  ```bash
  scancel <SLURM_ARRAY_JOB_ID>_[<SLURM_ARRAY_TASK_ID>-<SLURM_ARRAY_TASK_ID>]
  scancel 505_[2-3]
  ```

  * Cancel all tasks
  ```bash
  scancel <SLURM_ARRAY_JOB_ID>
  scancel 505
  ```


## Example Batch Scripts

### Reading from Indexed Files or Directories
This example demonstrates how you can organize your data to be "Job Array Friendly" by placing each task's data into a corresponding file. In order to pair each task with a unique data file, you must ensure the files are named in such a way that they include the job array's indexes (i.e. `$SLURM_ARRAY_TASK_ID`). 

Example Directory of Data Files: 
 * `DATA_1.txt`
 * `DATA_2.txt`
 * `DATA_3.txt`

The batch script, provided below, will create a Job Array with 3 tasks. Each task will echo the contents of its corresponding data file to standard output

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

# run workflow
cat "DATA_${SLURM_ARRAY_TASK_ID}.txt"
```


### Reading Task-Specific Parameters from a text file

This example includes three parts - a batch script, a python script, and a text file. The batch script is designed to create a Job Array with 5 tasks. Each task will read its assigned data `$(sed -n "${SLURM_ARRAY_TASK_ID}p" arguments.txt)` from the text file and pass it to the python script `python cars_mpg.py`. The python script then prints the provided arguments to standard output.  

Please note, while this example uses Python, this approach can be used with just about any workflow that accepts commandline arguments. Also, if you would like to learn more about the `sed` command, consider checking its help page with `sed --help`. 

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
python cars_mpg.py $(sed -n "${SLURM_ARRAY_TASK_ID}p" arguments.txt)
```

Python Script: 
```python
import sys

car=sys.argv[1]
mpg=sys.argv[2]

print("The " + car + " gets " + mpg + " mpg.")
```

Input File (arguments.txt):
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