# Node types

Research Computing has several node types available on our resources.
Each node type is meant for certain tasks. These node types are
relatively common for other HPC centers. We will discuss each node
type and its intended use below.


## Login nodes

* Four virtual machines
* This is where you are when you log in
* _Do not use for_: computation, compiling code, interactive jobs, or long running processes
* _Use for_: editing scripts, moving files, scheduling jobs

Users should familiarize themselves with [CURC User Policies](../additional-resources/policies.md#login-nodes) regarding login nodes.

## Compile nodes (Alpine only)

* Where you compile code, such as Fortran, C, C++
* No heavy computation
* Submit Jobs
* Access these nodes by typing `acompile` from a login node


## Compute nodes

This is where jobs are executed after being passed to the scheduler.

* Intended for heavy computation
* When run an [interactive job](../running-jobs/interactive-jobs.md) will be
  performing tasks directly on the compute nodes

## Data Transfer Nodes
* Data Transfer Nodes (DTNs) are nodes which support [data transfer](data-transfer.md#data-transfer) on CURC systems. 
* When transferring files using `scp`, `sftp`, or `ssh`, you can choose to host your transfers on a DTN.

