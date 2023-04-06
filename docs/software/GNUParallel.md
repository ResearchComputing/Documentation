## GNU Parallel

GNU Parallel is an effective tool for optimally using multiple cores and nodes (when paired with `srun`) on CURC clusters to run a large number of independent tasks, without the need to learn 
OpenMP or MPI. It allows shell commands (for example, calls to serial programs) to be distributed amongst nodes and cores. For this reason, code can be written in any language that can be run from a Linux shell. 

### Why Use GNU Parallel?

Suppose you have a very simple serial program that crops a photo and you need to apply it to millions of photos. You could rewrite the serial program into a parallel program that would use multiple processors to more quickly run the program over the entire set of photos (compared to doing them one-at-a-time), but this would require knowledge of parallel programming. If your code is in a language that has limited parallelization capabilities then this may not even be an option. The easiest solution to this problem is to use GNU Parallel.

### Simple GNU Parallel Example

To begin, we will first create a simple serial program. We will call the script `my_host_and_proc.sh` and it will print the task number (provided by GNU parallel), the node being used, and the processor performing the work:

```bash
#!/bin/bash                                                                                                                    

# obtain the name of the node we are on                                                                 
MYHOST=$(hostname)

# obtain the processor being used on the node                                                               
MYPROC=$(cat /proc/self/stat |gawk '{print $39}')

# print the task, node, and processor ($1 is input being provided to the script)                                                            
echo "task $1 is being ran on node $MYHOST and processor $MYPROC"
```
Now we create a job script called `run.sh` that is capable of using GNU Parallel to run as many instances of `my_host_and_proc.sh` as we want. Additionally, this job script will be capable of running across multiple nodes. 

```bash
#!/bin/bash
#SBATCH --time=00:20:00                                                    
#SBATCH --partition=atesting                                               
#SBATCH --qos=testing                                                      
#SBATCH --ntasks=4                                                         
#SBATCH --cpus-per-task=1                                                  
#SBATCH --job-name=gnu_test                                                
#SBATCH --output gnu_test.%j.out

# create a variable that assigns one task for each slurm job step                                                                                     
my_srun="srun --export=all --exclusive --nodes=1-$SLURM_JOB_NUM_NODES --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --cpu-bind=cores"

# tells GNU parallel to run "ntasks" in parallel at one time                                                                   
my_parallel="parallel -j $SLURM_NTASKS"

# runs "my_srun" command in parallel with script "my_host_and_proc.sh" for 20 iterations                                       
$my_parallel "$my_srun ./my_host_and_proc.sh" ::: {1..20}
```



_Edit the below items!!!_

Breaking down the constructed lines: 
- We customize the GNU Parallel 
`parallel` command by creating a variable called `$my_parallel`
    - `-j $SLURM_NTASKS` specifies that we will be running `$SLURM_NTASKS` in parallel at one time
    - `$SLURM_NTASKS` is a environment variable set by Slurm at runtime and is equal to the values specified by `--ntasks`
- The `my_srun="srun --export=all --exclusive --nodes=1-$SLURM_JOB_NUM_NODES --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --cpu-bind=cores"` allows for multi-node runs
    - `--export=all` loads our environment for each `srun` call
    - `--exclusive` ensures that the allocations requested will not be shared amongs the job steps 
    - `--nodes=1-$SLURM_JOB_NUM_NODES` dictates that we can use 1 to `$SLURM_JOB_NUM_NODES` number of nodes
    - `--ntasks=1` states that each `srun` will only use one task
    - `--cpus-per-task=$SLURM_CPUS_PER_TASK` sets the number of CPU used for each task to the value provided by the `#SBATCH` directive `--cpus-per-task`
    - `--cpu-bind=cores` 



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

### **Additional Resources**

- [https://www.gnu.org/software/parallel/](https://www.gnu.org/software/parallel/)
- [https://www.gnu.org/software/parallel/parallel_tutorial.html](https://www.gnu.org/software/parallel/parallel_tutorial.html)
- [https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019](https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019)
- [https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html](https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html)
- [https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html](https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html)

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
