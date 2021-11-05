#Slurm Integration for CUmulus Virtual Machines

###Instructions for Ubuntu20.04:

```
#login to VM using your private key and the floating IP
ssh -i ~/.ssh/<ssh_key> ubuntu@<Floating IP>

#update and install dependencies
sudo apt-get update
sudo apt install -y libmysqlclient-dev libjwt-dev munge gcc make

#install slurm
cd /opt
sudo git clone -b slurm-20-02-4-1 https://github.com/SchedMD/slurm.git
cd slurm
sudo ./configure --with-jwt --disable-dependency-tracking
sudo make && sudo make install

#add slurm.conf
sudo mkdir -p /etc/slurm
cd /etc/slurm
sudo scp <RC_username>@login.rc.colorado.edu:/curc/slurm/blanca/etc/slurm.conf . #type your CURC password and accept Duo push
sudo vi slurm.conf #edit the following two variables as follows in slurm.conf:

ControlMachine=slurm3.rc.int.colorado.edu
BackupController=slurm4.rc.int.colorado.edu

#create a slurm user group
sudo groupadd -g 515 slurm
sudo useradd -u 515 -g 515 slurm

#Configure your user and group on the VM

#first query your user/group info on a CURC login node:
[user@login11 ~]$ ml slurm/blanca
[user@login11 ~]$ id -u $USER
111111
[user@login11 ~]$ id -g $USER
111111
[user@login11 ~]$ whoami
USERNAME
[user@login11 ~]$ id -g -n $USER
USERGROUP

#now create user/group on VM:
sudo groupadd -g 111111 USERGROUP
sudo useradd -u 111111 -g 111111 USERNAME

#now generate JWT (token) on a login node
ml slurm/blanca
scontrol token lifespan=72000 #token with 2 hour duration
SLURM_JWT=...

#in VM, sudo to your user and export token
sudo su - USERNAME
export SLURM_JWT=...

#tell slurm where slurm.conf is:
export SLURM_CONF=/etc/slurm/slurm.conf

#now try a test job:
sbatch --qos <blanca-qos> --chdir="/home/USERNAME" --wrap="hostname"
Submitted batch job 12451234
```
