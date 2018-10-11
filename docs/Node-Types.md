### Table of Contents

- [Overview](#overview)
- [Login nodes](#login-nodes)
- [Compile nodes](#compile-nodes)
- [Compute nodes](#compute-nodes)

# Overview

Research Computing has several node types available on our resources.  Each node type is meant for certain tasks. These node types are relatively common for other HPC centers.  We will discuss each node type and its intended use below.

# Login nodes

  * Four virtual machines
  * This is where you are when you log in
  * No computation, compiling code, interactive jobs, or long running processes
  * Script or code editing
  * Job submission
  * To submit jobs from these nodes, will first need to run the command `module load slurm/summit`

# Compile nodes
  
  * Where you compile code, such as Fortran, C, C++
  * No heavy computation
  * Can submit jobs from compile nodes, but do not need to run `module load slurm/summit`
  * Access these nodes by typing `ssh scompile` from a login node

# Compute nodes
  * This is where jobs that are submitted through the scheduler run
  * Intended for heavy computation
  * When run an [interactive job](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki/Interactive-Jobs) will be performing tasks directly on the compute nodes


