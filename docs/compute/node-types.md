## Node types

Research Computing has several node types available on our resources.
Each node type is meant for certain tasks. These node types are
relatively common for other HPC centers. We will discuss each node
type and its intended use below.


### Login nodes

* Four virtual machines
* This is where you are when you log in
* No computation, compiling code, interactive jobs, or long running processes
* Script or code editing
* Submit Jobs


### Compile nodes

* Where you compile code, such as Fortran, C, C++
* No heavy computation
* Submit Jobs
* Access these nodes by typing `ssh scompile` from a login node


### Compute nodes

This is where jobs are executed after being passed to the scheduler.

* Intended for heavy computation
* When run an [interactive job](../running-jobs/interactive-jobs.html) will be
  performing tasks directly on the compute nodes

Couldn't find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/1WoP_KtLp9lnTEsgW7Os-we45_JbEt3aUgS6j61jARnk/edit)
