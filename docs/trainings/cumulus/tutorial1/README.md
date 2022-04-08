# Tutorial: Creating a CUmulus instance

---

#### _Learning Objectives:_

* [Logging into CUmulus via Horizon](#part-1-logging-in-to-cumulus-via-horizon) (the CUmulus web portal)
* [Creating your instance](#part-2-instance-creation) (i.e. virtual machine)
* [Logging into your instance](#part-3-logging-into-your-instance) via `ssh` 

---
###  Part 1: Logging in to CUmulus via Horizon
---

_Horizon is the CUmulus web portal, hosted at https://cumulus.rc.colorado.edu. Let’s take a brief tour of Horizon_.

#### _Log in with your institution’s credentials:_

Navigate to https://cumulus.rc.colorado.edu and authenticate using your insitution's credentials (e.g., University of Colorado Boulder)

<p align="center">
<img src="images/login.png" width="40%" />
</p>

---

#### _Navigate Horizon_

* Choose your project (top left)
  * _Note: Generally users only have 1 project_

* There are 4 main sections we use to administer projects:
  * `Compute`
  * `Volumes`
  * `Networks`
  * `Orchestration`
 
<p align="left">
<img src="images/navigate_intro.png" width="35%" />
</p>

---

#### _Navigate Horizon: Overview_

* Land on the Overview page under “Compute” to get a quick summary of your project

<p align="center">
<img src="images/navigate_overview.png" width="70%" />
</p>

---

#### _Navigate Horizon: Instances_

* Navigate to: `Project->Compute->Instances`

* Instances are virtual machines that run inside the cloud, more simply: an instance is just a digital version of a physical computer.
  * Instances can perform almost all of the same functions as a computer, including running applications and operating systems.

* You are now ready for instance creation! ...


---
### Part 2: Instance Creation
---

* From here, let’s create a simple instance
  * From the Instances page click `Launch Instance` to begin creating your virtual machine.

#### _Instance creation: Details_
 
The first instance creation screen is entiled ___Details___: 

<p align="center">
<img src="images/instance_details.png" width="70%" />
</p>

* Fill out the instance _name_ and _description_
  * _availability zone_ and _count_ can be left as default. This value is set to the availability zone given by the cloud provider (for example, us-west or apac-south).
* click `Next` when done to go to the ___Source___ screen.
 
---

#### _Instance creation: Source_
Next, we'll select our boot source. We're starting a new instance from scratch here so we'll boot from a source OS image.

<p align="center">
<img src="images/instance_source.png" width="70%" />
</p>

* Choose an operating system from the list of images CURC provides (in this example we pick Ubuntu 18.04)
* Choose a storage volume size 
  * _For this tutorial, choose 4 GB_
  * _Choosing an image will auto-populate the size, warning you if it is too small_
* Choose to have your storage volume deleted on Instance Deletion
  * If you select _No_ be aware “zombie” volumes will remain when the instance is deleted (you will need to remove them manually later!)
* click `Next` when done to go to the ___Flavor___ screen.

---

#### _Instance creation: Flavor_
A flavor defines the compute, memory, and storage capacity of our instance.

<p align="center">
<img src="images/instance_flavor.png" width="70%" />
</p>

* Choose the most appropriate sizing for your use case from a list of pre-selected resources
  * _For this tutorial, select the smallest size_
* click `Next` when done to go to the ___Networks___ screen.

---

#### _Instance creation: Networks & Network Ports_

<p align="center">
<img src="images/instance_networks.png" width="70%" />
</p>

* Select a project network, which determines routability of either a public/internet or campus/internal floating IP.
  * _For this tutorial we’ll choose an external network (the default)_
* click `Next` when done to go to the ___Ports___ screen.
  * Ports provide extra communication channels to your instances. 
  * You can select ports instead of networks or a mix of both.
* click `Next` when done to go to the ___Security Groups___ screen.

---

#### _Instance creation: Security Groups_

<p align="center">
<img src="images/instance_security_groups.png" width="70%" />
</p>

* Security Groups act as a virtual firewall for your instance to control inbound and outbound traffic.
  * Choose `ssh-restricted`, `http`, and `https` for this tutorial
* click `Next` when done to go to the ___Key Pair___ screen.

---

#### _Instance creation: Key Pair_

<p align="center">
<img src="images/instance_keypair.png" width="70%" />
</p>

* A key pair allows you to SSH into your new instance.
* You may select an existing key pair, import a key pair, or generate a new key pair.
  * _Tip: it is often easiest to create a keypair in a terminal on your local machine and import it: https://www.ssh.com/academy/ssh/public-key-authentication_ 
* click `Next` when done to go to the ___Configuration___ screen.

> _**An aside on SSH keypairs:**_ SSH keys are an access credential that is used in the SSH protocol and they are foundational to modern Infrastructure-as-a-Service platforms. Public key authentication provides cryptographic strength that even extremely long passwords can not offer. With [SSH](https://www.ssh.com/ssh/), public key authentication improves security considerably as it frees the users from remembering complicated passwords (or worse yet, writing them down).
>
> They can be tricky to set up for new users however, so we'll go over a simple example here. From your terminal in a local machine use the `ssh-keygen` command to create a new ssh keypair (you can specify cryptographic algorithm, in this case we'll use the Ed25519 algorithm):
>  ```shell
> $ ssh-keygen -t ed25519
> Generating public/private ed25519 key pair.
> Enter file in which to save the key (/home/username/.ssh/id_ed25519):
>```
>
> Here you can specify the full path/name of the keypair files and even set a extra passwords. We'll press enter twice for the `no passphrase` option. Our new keypairs have been created at `/home/username/.ssh/` and are called `id_ed25519`  and `id_ed25519.pub.` The public key (.pub) can be transferred to other remote servers (this is the key we will import to our CUmulus instance) but the private key (no suffix) should never leave the host machine. 

---

#### _Instance creation: Configuration, Server Group, Scheduler Hints, and Metadata_

<p align="center">
<img src="images/instance_config.png" width="70%" />
</p>

* For the remaining screens -- _Configuration_, _Server Group_, _Scheduler Hints_, and _Metadata_ -- leave these as defaults, as they are extra, optional configuration for the instances.

---

#### _Instance creation: Launch Instance and Associate IP_

* ___Finally___ you can click `Launch instance`! 
  * the instance will take a few minutes to finish provisioning.

* You can now associate a Floating IP to enable access to the instance from outside of the CU network.
  * On the right hand side of the newly created instance choose `Associate Floating IP` under the `Actions` dropdown
  
<p align="center">
<img src="images/instance_ip1.png" width="40%" />
</p>


* Now select from available IP addresses if needed (e.g., if you'll be adding a web portal to your instance)
* The _Select port to be associated_ option should already be pre-populated with the internal IP of your new instance

<p align="center">
<img src="images/instance_ip2.png" width="70%" />
</p>

---
### Part 3: Logging into your Instance
---

At a minimum, you'll need to login to your instance via `ssh` to install the software you'll be using. Other reasons to login to the instance may be to stop or start services, associate a domain name with your IP, run your software, troubleshoot problems, etc. You are essentially the "system administrator" of your own instance.

* To login to an instance via `ssh`, you _must_ be on CU VPN to connect (this is CURC restriction)
* Open up an ssh connection providing the identity (key) file that you associated with the instance in the _Key Pair_ step covered earlier:

```bash
$ ssh -i ~/.ssh/<private key> <hostname>@<external floating IP>
```

* Note that `hostname` will be "ubuntu" for Ubuntu instances, "centos" for Centos instances, etc. 
  * For example, for an ubuntu instance your `ssh` command may look something like this:

```bash
$ ssh -i ~/.ssh/testkey ubuntu@123.456.789.123
```

__Congratulations! You are now logged into your instance!__ 

* You can now:
  * Install Software
  * Administer your instance
  * Run applications and jobs
* If you need to perform actions as the _root_ (administrative) user, once logged in you can "sudo" to the _root_ account as follows:

```bash
$ sudo su - root
```
  or run a command with the `sudo` prefix.

---  
### Additional Information
---

  * [CUmulus documentation](https://curc.readthedocs.io/en/latest/hybrid-cloud/cumulus.html)
  * [OpenStack User Documentation](https://docs.openstack.org/horizon/latest/user/index.html)
