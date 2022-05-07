## Parallel programming with Jupyter

This tutorial demonstrates simple parallel processing examples using
the CURC JupyterHub web service, in both ipyparallel and MPI for
Python.

### Prerequisites

Before you begin, you need

* an RC account
* Duo credentials
* access to a CU campus network or VPN
* a web browser

### Log in

First, log into the RC JupyterHub service by nagivating to
[https://jupyter.rc.colorado.edu](https://jupyter.rc.colorado.edu). Enter your RC username and password
(where your password may be a combination of a password, OTP, and/or
credential prefix).

After authenticating, you should be redirected to your Jupyter
notebook server; but this process is a queued process, so you may have
to wait if the JupyterHub resources are otherwise fully utilized.

### Prepare an IPython cluster

Navigate to the _IPython Clusters_ tab to access a list of available
parallel profiles. Each profile represents an IPython cluster you can
initialize, with a predefined configuration; the _# of engines_ is the
number of processes you will spawn for the cluster.

Any of the RC-provided cluster profiles (though not the default
profile) can be used for these examples. Specify 2 engines for the
`example-shas` node, and use the _Start_ button to start the compute
cluster.

### Creating a parallel-processing notebook

Return to the _Files_ tab and use the _New_ button to create a Python
3 notebook. A new notebook should include an initial Python code cell;
but, if necessary, use the _Insert_ menu to insert a new cell, and use
the _Cell > Cell Type_ menu to configure the new cell as a _Code_
cell.

This first cell includes code to initialize access to the running
cluster using `ipyparallel`. You can simply paste this code into the
cell, all of which executes within the Jupyter notebook.

```python
import ipyparallel

# attach to a running cluster
cluster = ipyparallel.Client(profile='example-shas')
print('profile:', cluster.profile)
print("IDs:", cluster.ids) # Print process id numbers
```

Execute the cell using Shift+Return, which produces output identifying
the engine IDs available in the cluster.

```
profile: example-shas
IDs: [0, 1]
```

**Note:** IPython engines on RC cluster resources are provisioned as
batch jobs using Slurm, but Jupyer does not yet report queue
progress. If no IDs are listed, or an exception "NoEnginesRegistered:
Can't build targets without any engines" is raised, the cluster job is
still in the queue and is not ready to accept work.

### IPython Parallel

Once the above code has successfuly reported the engine IDs for the
cluster, insert a new code cell below the existing code block.

```python
# The %px magic executes a single Python command on
# the engines specified by the targets attribute of
# the DirectView instance.
#
# http://ipython.org/ipython-doc/stable/parallel/magics.html#px
%px import socket
%px print("hosts:", socket.gethostname())

# calculate square numbers in parallel. Print result.
squares = cluster[:].map_sync(lambda x: x**2, range(32))
print("squares:", squares)
```

Execute this cell using Shift+Return, which outputs the hostname of
the host for each engine, as well as the calculated square numbers in
each cell. In this cell, code prepended with `%px` is executed in each
engine; and the `squares` are calculated using the `cluster` reference
obtained in the previous code block.

#### MPI for Python

Insert a new code cell below the existing code block to demonstrate
message passing using MPI.

```python
%%px

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(100, dtype='i')
    numpy.random.shuffle(data)
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print("{0}: sent data to 1: {1}".format(rank, data))
elif rank == 1:
    data = numpy.empty(100, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print("{0}: received data from 0: {1}".format(rank, data))
else:
    print("{0}: idle".format(rank))
```

Execute this cell using Shift+Returm. This cell is prepended with
`%%px`, which causes the entire cell to execute in parallel on all
nodes. Rank 0 generates a random numpy array which is then sent to
rank 1.

### Shutting down

Both the IPython cluster and notebook server will persist until
manually stopped or each reaches its time limit. IPython clusters have
a 4-hour time limit by default (though this can be changed by editing
the profile in `$HOME/.ipython/`). The notebook server itself has a
time limit of 2 or 12 hours depending on which job profile you select. 
When you are done using a resource, please shut
it down so that the resources can be used for other work.

Return to the "IPython Clusters" tab and press the "Stop" button for
`example-shas` (or whichever profile was used during the example).

Finally, if you are done using Jupyter notebook for now, access the
"Control Panel" and press the "Stop My Server" button to stop the
Jupyter notebook server. After that, you may press "Logout", or simply
close the browser window.

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
