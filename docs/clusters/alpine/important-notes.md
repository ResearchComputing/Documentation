## Important Notes

1. **Software**: To see what modules are available on Alpine, start an interactive or `acompile` on a compute node and use the `module avail` or `module spider` commands.
2. **Filesystems**: `/home`, `/projects`, and `/pl/active` (PetaLibrary Active) are mounted on all Alpine nodes.
3. **Scratch Space**: `/scratch/summit/$USER` is replaced by `/scratch/alpine/$USER`.
	> Alpine scratch will offer much better performance than doing I/O from `/projects`.
4. **Node-local scratch**: Most Alpine nodes also have at least 400 GB of scratch space on a local SSD disk, which will offer the fastest I/O possible.
	> This job specific directory is available within jobs as `$SLURM_SCRATCH`. Note that this storage is only available during jobs and is deleted after jobs, so be sure to copy new data you want to keep off of it at the end of your job script. For more info on the different RC storage spaces, please see our page on [storage](../../compute/filesystems.html).
4. **Head-nodes**: There are no dedicated Alpine "head nodes" that would be analogous to the Summit "scompile" nodes, instead `acompile` jobs have been implemented with the `acompile` command (note the lack of `ssh`). To build software that will run on Alpine, start an interactive or an `acompile` job on Alpine and compile your software there. _**Do not compile on the login nodes!**_

Note: For more information on `acompile` options use the command:
```bash
$ acompile --help
acompile: CURC utility to access a single alpine compute node for compiling software
usage:
       -t | --time=<time-limit>        : set the job's minimum runtime (default 60 minutes/max 12 hours)
       -n | --ntasks=<number-of-cores> : set the number of cores required for the session (default 1/max 4)
       -X | --x11                      : enable x11 support for the session (requires user to login w/ -X or -Y flag)
          | --test-only                : stop job submission and print submit command
       -h | --help                     : print this message
```


Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
