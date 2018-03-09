Interactive jobs are jobs that allow a user to interact with applications in real time. With interactive jobs, applications such as python or matlab can be ran in an interactive environment. To run an interactive job load the slurm module into the enviornment with:
```bash
module load slurm/summit
```
and request an interactive session by utilizing the `sinteractive` command. 
The `sinteractive` command takes in several flags to take in some information about the interactive session:
