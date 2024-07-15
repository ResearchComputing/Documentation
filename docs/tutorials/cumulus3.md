# CUmulus integration with CURC HPC 

One potentially useful application of CUmulus is the ability to integrate your VMs with CU Research Computing High Performance Computing (HPC) resources. HPC compute is typically time-limited (at CURC 24 hours for regular job and 7 days long job) due to finite resources and user competition for those resources. One way to deal with this problem is to schedule your jobs over time (e.g. by using cronjobs) though this isn't always practical for more complex workflows. Using authentication keys (in this case Java Web Tokens or JWTs) you can setup a connection from your CUmulus instance to CURC HPC and schedule jobs remotely to set up more complex workflow specific pipelines. 

We have documented the process for an **Ubuntu 20.04 instance on CUmulus connecting to the CURC Blanca cluster**. Below is an outline with links to specific sections:
1. Create your CUmulus instance
2. Install SLURM on CUmlus Instance
3. Configure SLURM in CUmulus
4. Generate Java Web Token (JWT) in CURC HPC
5. Submit your job from your CUmulus instance 

## Instructions for Ubuntu 20.04:

###  Part 1 Create your CUmlus instance:

The first thing we will need to do is create a Ubuntu 20.04 CUmulus instance. Log in to the [CUmlus portal](https://cumulus.rc.colorado.edu) and follow our [tutorial1](./cumulus1) to create a CUmulus instance with the following specifications: 
* Image: Ubuntu 20.04 
* Flavor: 
* Network: 
* Security groups: ssh-restricted
* Set up a Floating IP

###  Part 2: Install SLURM on CUmlus Instance

The second thing we'll need to do is install SLURM on our CUmulus instance. To do so we will log into our instance using ssh, update our instance, then install SLURM. 

* **Log in to your instance** from a local machine by specifying your ssh key file (with the `-i` flag) and the floating IP you set up in step 1:
	> Note: this command is entered from your local machine's terminal
	```
	$ ssh -i ~/.ssh/<ssh_key> ubuntu@<Floating IP>
	```
* From your CUmulus instance **update and install SLURM dependencies** 
	> Note: these commands require administative (sudo) privilage
	```
	$ sudo apt-get update
	$ sudo apt install -y libmysqlclient-dev libjwt-dev munge gcc make
	```
* **Install SLURM**. It looks like there's a lot going on with this step, but all we're doing is downloading SLURM from github to the `/opt` directory of your instance, configuring the compilation to include Java Web Tokens (JWT) functionality, and then compiling and installing SLURM. Note that it is **VERY IMPORTANT** that the SLURM version on your CUmulus instance matches the CURC HPC version otherwise it will not connect. 

	> You can check the SLURM version on CURC HPC resources by loading your cluster specific SLURM module from a login node (either `module load slurm/blanca` or `module load slurm/alpine`) then checking the version of a SLURM command (e.g. `sbatch --version`). 

	> In this example we're using the 20.02.4 SLURM version and specifying it with git clone branch flag (`-b`)
	```
	$ cd /opt
	$ sudo git clone -b slurm-20-02-4-1 https://github.com/SchedMD/slurm.git
	$ cd slurm
	$ sudo ./configure --with-jwt --disable-dependency-tracking
	$ sudo make && sudo make install
	```

###  Part 3. Configure SLURM in CUmulus

Now that we have SLURM installed we can start to configure our instance to make the proper connection to CURC HPC resources. In this step we'll add/edit the `slurm.conf` file, create a user and group for SLURM, create a user and group for you that match your user/group from CURC HPC.  

* Add `slurm.conf`. Here we make a slurm directory at `/etc/slurm` and copy the `slurm.conf` file straight from CURC HPC using the secure copy (`scp`) tool into that new directory.

	> Note: We are copying the `slurm.conf` file from Blanca in this example
	```
	$ sudo mkdir -p /etc/slurm
	$ cd /etc/slurm
	$ sudo scp <RC_username>@dtn.rc.colorado.edu:/curc/slurm/blanca/etc/slurm.conf . 
	```
	to finish the copy from CURC HPC, type your CURC password and accept Duo push.

* Edit the following two variables in slurm.conf using a text editor of your choice (i.e. vim, nano):
	* Change `ControlMachine=slurm3` to `ControlMachine=slurm3.rc.int.colorado.edu`
	* Change `BackupController=slurm4` to `BackupController=slurm4.rc.int.colorado.edu`

* Create a SLURM user & group. Use the group and user add commands to create the SLURM user and group with the 515 IDs:
	```
	sudo groupadd -g 515 slurm
	sudo useradd -u 515 -g 515 slurm
	```

* Configure your user and group on the VM. First we will query our user/group info on CURC HPC. From a CURC login node run the following commands and note the outputs: 
	```
	[user@login11 ~]$ id -u $USER
	<userid>
	[user@login11 ~]$ id -g $USER
	<groupid>
	[user@login11 ~]$ whoami
	<username>
	[user@login11 ~]$ id -g -n $USER
	<groupname>
	```

	We can now create a user and group for ourselves on our instance that match CURC HPC:
	```
	$ sudo groupadd -g <groupid> <groupname> 
	$ sudo useradd -u <userid> -g <groupid> <username> 
	```

###  Part 4. Generate Java Web Token (JWT) in CURC HPC 

* Next we will generate the Java Web Token on a CURC login node. Keep in mind that these tokens are generated with an expiration. Note the JWT output in order submit jobs.
	> Note: In this example we are generating this token on the Blanca cluster 
	```
	$ module load slurm/blanca
	$ scontrol token lifespan=72000 #token with 2 hour duration
	$ SLURM_JWT=<jwt-token>
	```

###  Part 5. Submit your job from your CUmulus instance 

Our CUmulus instance is now configured to submit jobs to CURC HPC resources. When we ssh to our instance we are (likely) logged in as the admin user. We need to log in to the user we created in the previous step to submit jobs so CURC HPC will recognize the incoming request.

* Use the `sudo su -` command to log into your user 
	```
	$ sudo su - <username> 
	```
* Set the `SLURM_JWT` and `SLURM_CONF` variables in your environemt:
	```
	export SLURM_JWT=<jwt-token>
	export SLURM_CONF=/etc/slurm/slurm.conf
	```
* Submit a test job! We're finally ready to test a job submission from CUmulus. Use the `sbatch` command to submit a job from the command line (i.e. without a batch script). In the example job submission below we use the `--chdir` flag to change into our home directory (so we can easily find the job output) and use the `--wrap` command to run the simple `hostname` bash command on a CURC compute node.

	```
	$ sbatch --qos=<blanca-qos> --chdir="/home/<username>" --wrap="hostname"
	Submitted batch job 12451234
	```
	> Note: you can use the `--chdir` flag to direct the output to an directory you have write access to.

You have now successfully connected your CUmulus instance to CURC HPC resources! From this point you have a number of ways to integrate this connection into your workflow:
* Pass raw data to CURC HPC resources for post-processing once it becomes available.
	
> This work has been funded in part by the National Science Foundation under grant OAC-1925766
