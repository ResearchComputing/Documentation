## Important Notes

1. **Software**: To see what modules are available on Alpine, start an interactive job on a compute node and use the `module avail` or `module spider` commands.
2. **Filesystems**: `/home`, `/projects`, and `/pl/active` (PetaLibrary Active) are mounted on all Alpine nodes.
3. **Scratch Space**: `/scratch/summit/$USER` is replaced by `/scratch/alpine/$USER`.
	> Alpine scratch will offer much better performance than doing I/O from `/projects`.
4. **Node-local scratch**: Most Alpine nodes also have at least 400 GB of scratch space on a local SSD disk, which will offer the fastest I/O possible.
	> We are presently working to make this space available to users, but at the time of writing _it is not available_. Once we make it available, this job specific directory will be available within jobs as `$SLURM_SCRATCH`. Note that this storage is only available during jobs and is deleted after jobs, so be sure to copy new data you want to keep off of it at the end of your job script. For more info on the different RC storage spaces, please see our page on [storage](../../compute/filesystems.html).
4. **Head-nodes**: There are presently no dedicated Alpine "head nodes" that would be analogous to the Summit "scompile" nodes.  We are working to address this need. In the meantime, to build software that will run on Alpine, start an interactive job on an Alpine node on the partition on which you expect your jobs to run, and compile your software there. _**Do not compile on the login nodes!**_

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
