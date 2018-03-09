Interactive jobs are jobs that allow a user to interact with applications in real time. With interactive jobs, applications such as python or matlab can be ran in an interactive environment. To run an interactive job load the slurm module into the enviornment with:

```bash
module load slurm/summit
```

and request an interactive session by utilizing the `sinteractive` command. 
The `sinteractive` command can take any number of flags that could be used with the `sbatch` command when submitted to slurm but the primary flags we will use are the `qos` flag and the `time` flag. These flags will specify quality of service and amount of time the job will run for respectively. We can run the command like so:

```bash
sinteractive --qos=debug --time=00:10:00
``` 

This will load us into an interactive session that will run on one core of one node on the debug quality of service for 10 minutes. From here you can run any interactive terminal application you may need.

## Interactive GUI Applications

To run an interactive General User Interface application, we must enable X11 forwarding on our personal computer.

### Windows

### Mac
 
## Videos:
General Interactive Jobs
Running GUI applications through an Interactive Job
