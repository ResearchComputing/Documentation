# Running jobs on RoCE enabled Nodes

We have some nodes in Blanca that are equipped with Mellanox 10G cards and RoCE v2
enabled switches to enable users to run MPI jobs over the 10G interfaces. While the 
10G network is not as performant with regards to latency as Infiniband or Omnipath,
you can still get line speed for bandwidth.

In order to take advantage of RoCE on these nodes, you will need to compile your code with a
MPI compiler that was built with support for Unified Communication X (UCX). Without UCX, a job
submitted to these nodes will fail.

## Using pre-built modules

You can easily build/rebuild your binaries with support for the 10G RoCE network by building 
your code with the module keys gcc/8.2.0 and openmpi_ucx/4.0.0.  Once you have loaded those software
keys you can begin building your code as you normally would.

## Build a MPI compiler with support for UCX

First ensure that you have UCX installed on the node you intend to build the MPI on

```bash
yum info ucx ucx-devel
```

Then you can move on to building the MPI, in this example we are using the default GNU compiler,
and are using the most recent version for OpenMPI.
```bash
./configure --prefix=/home/jobl6604/soft/openmpi-4.0.0 --with-ucx
```

After successfully building the MPI, you can then compile your code against it and start running jobs.
You do not need to worry about passing any flags or arguements into the MPI command for your job script.

## Tips

If you are still have issues trying to run your code you can try passing some flags to MPI

```bash
mpirun --mca pml ob1 --mca btl openib,self,vader --mca btl_openib_cpc_include rdmacm --mca btl_openib_rroce_enable 1 <command>
```


