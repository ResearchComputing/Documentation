Interactive jobs are jobs that allow a user to interact with applications in real time. With interactive jobs, applications such as python or matlab can be ran in an interactive environment. To run an interactive job load the slurm module into the enviornment with:

```bash
module load slurm/summit
```

and request an interactive session by utilizing the `sinteractive` command. 
The `sinteractive` command can take several flags when submitted to slurm but the primary 2 flags we will use are the `qos` flag and the `time` flag. These two flags will specify quality of service and amount of time the job will run for respectively. We can run the command like so:

```bash
sinteractive --qos=debug --time=00:10:00
``` 


