## Node types

Research Computing has several node types available on our resources.
Each node type is meant for certain tasks. These node types are
relatively common for other HPC centers. We will discuss each node
type and its intended use below.


### Login nodes

* Four virtual machines
* This is where you are when you log in
* _Do not use for_: computation, compiling code, interactive jobs, or long running processes
* _Use for_: editing scripts, moving files, scheduling jobs

#### Policy for use of login nodes:

The RC login nodes are lightweight virtual machines that serve as gateways to CURC computing resources including Blanca, Summit and Alpine. They are strictly intended for non-computational tasks including editing scripts, moving files, scheduling jobs to run on CURC computing resources, and non-intensive workflow monitoring/management tasks. They are not intended for computational tasks of any kind. CURC personnel regularly monitor processes on the login nodes and reserve the right to terminate processes in violation of this policy without notice.  Repeated violations by the same user may result in a suspended account.


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

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
