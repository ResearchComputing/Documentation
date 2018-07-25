## Table of Contents

- [Overview](#overview)
- [Why Use the Load Balancer?](#why-use-the-load-balancer)
- [Using the Load Balancer](#using-the-load-balancer)

## Overview
The CU Research Computing Load Balancer is an effective tool for optimally utilizing multiple processors and nodes on the Summit HPC resource, without the need to learn OpenMP or MPI. This tutorial assumes user knowledge of Slurm job submission, shell scripting, and some python.
 
## Why Use the Load Balancer?
Suppose you have a very simple serial program that crops a photo, and you need to apply it to crop several million photos. You could rewrite the serial program into a parallel program that would utilize multiple processors to more quickly run the program over the entire set of photos (compared to doing one-at-a-time), but this would require some knowledge of parallel programming. Even worse, if your code is in a language that has limited parallelization capabilities, this may not be an option. The easiest solution for this problem is to utilize the Load Balancer.
 
## Using the Load Balancer
The Load Balancer is a tool written by CU Boulder Research Computing that allows shell commands (for example, calls to serial programs) to be distributed amongst nodes and cores on Summit. This means code doesn’t need to be explicitly parallelized for MPI or OpenMP. Additionally, code can be written in any language that can be run from a Linux shell.
 
Let’s create a simple ‘Hello World’ serial python script to demonstrate the Load Balancer tool. We will call the script `hello_World.py` and it will print “Hello World from process: ” followed by a command line argument:
 
```python
import sys
 
print “Hello World from process: ”, sys.argv[1]
```

Now we will create a list of calls to the python script that will be distributed to multiple cores (note that a processor may have one or more cores, and each core can perform a task). Instead of slowly typing out commands one-at-a-time, we will use a bash shell script to create our commands. In a text editor, create a bash shell script called `create_hello.sh`, that has the following text:  

```bash
#!/bin/bash

for i in {1..4}
do
  echo “python hello_World.py $i;” >> lb_cmd_file
done
``` 

Next run the bash script by first changing permissions of the script to be executable by typing: `chmod +x create_hello.sh` and then typing `./create_hello.sh` at the terminal prompt. It will create a file called `lb_cmd_file` that contains 4 calls to our `hello_World.py` script:  

```bash
python hello_World.py 1;
python hello_World.py 2;
python hello_World.py 3;
python hello_World.py 4;
```

Now create a job script called `run_hello.sh` that will submit all instances of your python script in `lb_cmd_file` using the Load Balancer. Within the script, before using Load Balancer, we need to load the Intel C++ compiler, Intel MPI, Python, and the Load Balancer utility itself. We load Intel and Intel MPI because the Load Balancer uses mpirun to parallelize commands. Your job script should look something like this:
 
```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time 00:02:00
#SBATCH --qos=testing
#SBATCH --partition shas-testing
#SBATCH --ntasks=4
#SBATCH --job-name lbPythonDemo
#SBATCH --output loadbalance.out
 
module purge
 
module load intel
module load impi
module load python
module load loadbalance

mpirun lb cmd_file
```

Submitting this script via sbatch will run the commands we stored in lb_cmd_file in parallel. A successful job will result in output that looks something like this:
 
```
Hello World from process: 2
Hello World from process: 1
Hello World from process: 4
Hello World from process: 3
```

### Additional Resources 
https://github.com/ResearchComputing/lb
https://github.com/t-brown/lb
https://computing.llnl.gov/tutorials/parallel_comp/#DesignLoadBalance
https://www.inspirenignite.com/load-balancing-in-parallel-computers/