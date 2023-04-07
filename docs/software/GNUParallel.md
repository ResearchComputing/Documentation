## GNU Parallel

GNU Parallel is an effective tool for optimally using multiple cores and nodes on CURC clusters to run a large number of independent tasks, without the need to learn 
OpenMP or MPI. It allows shell commands (for example, calls to serial programs) to be distributed amongst nodes and cores. For this reason, code can be written in any language that can be run from a Linux shell. 

### Why Use GNU Parallel?

Suppose you have a very simple serial program that crops a photo and you need to apply it to millions of photos. You could rewrite this serial program into a parallel program that would use multiple processors, however, this would require knowledge of parallel programming. If your code is in a language that has limited parallelization capabilities, then this may not even be an option. The easiest solution to this problem is to use GNU Parallel.

### Simple GNU Parallel Example

To begin, we will first construct a simple script (our serial program) that will be ran by GNU parallel. We will call this script `my_host_and_proc.sh`.

```bash
#!/bin/bash                                                                                                                    

# obtain the name of the node we are on                                                                 
MYHOST=$(hostname)

# obtain the processor being used on the node                                                               
MYPROC=$(cat /proc/self/stat |gawk '{print $39}')

# print the task, node, and processor ($1 is input being provided to the script)                                                            
echo "task $1 is being ran on node $MYHOST and processor $MYPROC"
```
Now, we create a job script called `run_gnu.sh` that is capable of using GNU Parallel to run as many instances of `my_host_and_proc.sh` as we want (here we choose to run 20). Additionally, this job script will be capable of running across multiple nodes. 

```bash
#!/bin/bash
#SBATCH --time=00:20:00                                             
#SBATCH --partition=amilan                                             
#SBATCH --nodes=2
#SBATCH --ntasks=3                                                         
#SBATCH --cpus-per-task=1                                                  
#SBATCH --job-name=gnu_test                                                
#SBATCH --output gnu_test.%j.out

# load modules
module purge
module load gnu_parallel

# obtain a bash array filled with the tasks assigned to each node
tasks_arr=(${SLURM_TASKS_PER_NODE//,/ })

# create bash array with corresponding node name for each task
nodes_arr=($(scontrol show hostname $SLURM_JOB_NODELIST))

# create a nodelist in the format of "tasks/hostname" 
task_node=$(for ((i=0; i<${#tasks_arr[@]}; i++)); do
            temp_name=("${tasks_arr[$i]}/${nodes_arr[$i]}");
            if (( $i < ${#tasks_arr[@]} - 1 )); then
                printf "$temp_name,";
            else
                printf "$temp_name";
            fi;
            done)

# set up bash environment used by env_parallel
. `which env_parallel.bash`

# Run GNU parallel with provided environment over the nodelist
env_parallel --sshlogin $task_node --workdir $PWD ./my_host_and_proc.sh ::: {1..20}
```

**_NOTE:_** You do not need to modify the creation of the bash variables `tasks_arr`, `nodes_arr`, or `task_node`. 

Breaking down the final line:
- `env_parallel` 
    - passes the bash environment (specified in the previous line) to the GNU parallel command [parallel](https://www.gnu.org/software/parallel/parallel.html)
- `--sshlogin $task_node` 
    - allows `env_parallel` to run on remote compute nodes specified by the bash variable `task_node` (which we created earlier) 
- `--workdir $PWD`
    - sets the working directory for all nodes ran by `env_parallel` to the current directory 
- `./my_host_and_proc.sh ::: {1..20}`
    - specifies that the script `my_host_and_proc.sh` should be ran in parallel 20 times.  



Running `run_gnu.sh` via `sbatch` will result in output similar to the following:

```
task 2 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 3 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 1 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 6 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 4 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 5 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 7 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 8 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 9 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 10 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 12 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 11 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 13 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 15 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 14 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
task 16 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 17 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 18 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 18
task 19 is being ran on node c3cpu-c11-u3-4.rc.int.colorado.edu and processor 34
task 20 is being ran on node c3cpu-c11-u3-1.rc.int.colorado.edu and processor 9
```

**_NOTE:_** You may receive warnings beginning with `Warning: Permanently added`. These types of warnings are the result of ssh-ing into a node for the first time. They may be ignored and will go away when you ssh into this node for a second time. 


### **Additional Resources**

- [https://www.gnu.org/software/parallel/](https://www.gnu.org/software/parallel/)
- [https://www.gnu.org/software/parallel/parallel_tutorial.html](https://www.gnu.org/software/parallel/parallel_tutorial.html)
- [https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019](https://github.com/ResearchComputing/HTC_Short_Course_Spring_2019)
- [https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html](https://rcc.uchicago.edu/documentation/_build/html/running-jobs/srun-parallel/index.html)
- [https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html](https://rcc.uchicago.edu/docs/tutorials/kicp-tutorials/running-jobs.html)

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
