# GNU Parallel

GNU Parallel is an effective tool for optimally using multiple cores and 
nodes on CURC clusters to run lots of independent tasks without the need 
to learn 
OpenMP or MPI. This tutorial assumes user knowledge of Slurm jobs, shell scripting, and some Python.

## Why Use GNU Parallel?

Suppose you have a very simple serial program that crops a photo, and you 
need to apply it to crop several million photos. You could rewrite the 
serial program into a parallel program that would use multiple processors 
to more quickly run the program over the entire set of photos (compared to 
doing one-at-a-time), but this would require knowledge of parallel 
programming. If your code is in a language that has limited 
parallelization capabilities then this may not even be an option. The 
easiest solution to this problem is to use GNU Parallel.

## Using GNU Parallel

GNU Parallel is provided as a software module on Alpine. It allows shell 
commands (for example, calls to serial programs) to be distributed amongst nodes and cores. This means code doesn’t need to be explicitly parallelized for MPI or OpenMP. Additionally, code can be written in any language that can be run from a Linux shell.

Let’s create a simple ‘Hello World’ serial python script to demonstrate the GNU Parallel tool. We will call the script `hello_World.py` and it will print “Hello World from task: ” followed by a command line argument:

```python
import sys

print "Hello World from task: ", sys.argv[1]
```

Now create a job script called `run_hello.sh` that will use GNU Parallel 
to run as many instances of your python script as you want. Before running GNU Parallel in our script, we need to load the python and GNU Parallel modules. Your job script should look something like this:

> _Note: This example uses a custom python environment built with conda, 
more infomation on using python or R with conda can be found 
[here](./python.md)

```bash
#!/bin/bash

#SBATCH --time 00:02:00
#SBATCH --partition atesting
#SBATCH --qos testing
#SBATCH --ntasks=4
#SBATCH --job-name gpPythonDemo
#SBATCH --output gnuparallel.out

module purge
module load anaconda 
conda activate your_custom_env
module load gnu_parallel

my_parallel="parallel --delay .2 -j $SLURM_NTASKS"
my_srun="srun --export=all --exclusive -n1 --cpus-per-task=1 --cpu-bind=cores"
$my_parallel "$my_srun python hello_World.py" ::: {1..20}
```

Note the last three lines of the script. We customize the GNU Parallel 
`parallel` command by creating a variable called `$my_parallel` that 
delays the execution of each task by 0.2 seconds (`--delay 0.2`) to 
mitigates bottlenecks for tasks that have heavy I/O, and which specifies 
the number of tasks to run simultaneously (`-j $SLURM_NTASKS`). The environment variable `$SLURM_NTASKS` is set by Slurm at runtime and contains the number of `—ntasks` (cores) requested in the `#SBATCH` directives. We then customize the `srun` command so that it properly allocates the GNU parallel tasks to the allocated cores (`--export=all --exclusive -N1 -n1 --cpus-per-task=1 --cpu-bind=cores`). Note that the use of `srun` will also ensure that GNU parallel runs properly for cases where we request cores across multiple nodes (e.g., if we request `--ntasks=100`). Finally, we invoke GNU Parallel to run our python script 20 times using the customized `parallel` and `srun` commands we just created, `$my_parallel` and `$my_srun` respectively. Running this script via `sbatch` will run the commands. A successful job will result in output that looks something like this:

```
Hello World from task: 1
Hello World from task: 2
Hello World from task: 3
Hello World from task: 4
Hello World from task: 5
Hello World from task: 6
Hello World from task: 7
Hello World from task: 8
Hello World from task: 9
Hello World from task: 10
Hello World from task: 11
Hello World from task: 12
Hello World from task: 13
Hello World from task: 14
Hello World from task: 15
Hello World from task: 16
Hello World from task: 17
Hello World from task: 18
Hello World from task: 19
Hello World from task: 20
```

In this example the 20 invocations of your python script will run across the 4 cores requested; as each core finishes one task, the next remaining task will be executed on that core until all 20 have finished. The printed output above may or may not be in order depending on how quickly each task completes.

Tip: For sufficiently-large workflows one can add the `--joblog` and `--resume` flags in `$my_srun`. These flags will enable GNU Parallel to keep track of tasks it has run successfully and, if needed, rerun tasks that failed or were not executed. Additional details can be found in the links below. 

## **Additional Resources**

- [https://www.gnu.org/software/parallel/](https://www.gnu.org/software/parallel/)
- [https://www.gnu.org/software/parallel/parallel_tutorial.html](https://www.gnu.org/software/parallel/parallel_tutorial.html)
- [https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019](https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019)
- [https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html](https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html)
- [https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html](https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html)

