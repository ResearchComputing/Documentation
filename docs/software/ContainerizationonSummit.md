# Containerization on Summit

When installing software, you may come across applications that have complex chains of dependencies that are challenging to compile and install. Some software may require very specific versions of libraries that may not be available on Summit or conflict with libraries needed for other applications. You may also need to move between several workstations or HPC platforms, which often requires reinstalling your software on each  system. Containers are a good way to tackle all of these issues and more.

## Containerization Fundamentals

Containers build upon an idea that has long existed within computing: hardware can be emulated through software. **Virtualization** simulates some or all components of computation through a software application. Virtual machines use this concept to generate an entire operating system as an application on a host system. Containers follow the same idea, but at a much smaller scale and contained within a system's kernel

**Containers** are portable compartmentalizations of some or all of the following: An operating system, software, libraries, data, and workflows. Containers offer: 

- Portability: containers can run on any system equipped with its specified container manager.
- Reproducibility: because containers are instances of prebuilt isolated software, software will always execute the same every time.

Containers distinguish themselves through their low computational  overhead and their ability to utilize all of a host system’s resources. Building containers is a relatively simple process that starts with a container engine.

## Docker

Docker is by far the most popular container engine, and  can be used on any system where you have administrative privileges. Because of this need for administrative privileges, Docker containers cannot be built or run directly on Research Computing resources. **To utilize a Docker container on Research Computing resources please build a singularity image using a Docker image as a base.**

See the documentation on Singularity (below) if you wish to run a Docker container on RMACC Summit or Blanca. 
<!--
Docker can be divided into 4 primary components:

- The Docker application
- A Dockerfile
- A Docker image
- A Docker container

The **Docker application** is the primary tool that creates, runs, and manages Docker images and containers. This application acts as the user interface for Docker images and containers stored on a system.

A **Dockerfile** is essentially *the recipe* for how to construct a Docker image. Dockerfiles can be created when attempting to build your own containers.

A **Docker image** is a saved instance of all the software, tools, and workflows you would like containerized. A Docker image is never run with the Docker application. Instead, Docker generates a running version of this image called a **Docker container**. A Docker image is immutable upon creation and must be recreated to make any changes.

A **Docker container** is an ephemeral instance of a Docker image. Docker images are mutable, but because they are killed on exit, and do not actually save any changes made to the container.

### Running a Docker container

**Note:** Docker containers cannot be run with Docker on RMACC Summit or Blanca, because the Docker software is not HPC-safe. Instead, Docker containers are run using a software called Singularity.  See the documentation on Singularity (below) if you wish to run a Docker container on RMACC Summit or Blanca. 

To run a Docker container on your laptop or other system on which you have Docker installed, simply type the command:

```bash
docker run <docker-image> 
```

If you run a docker container from an image that does not currently exist on your computer, then Docker will go ahead and search Docker-hub and attempt to pull the image from a public repository.

Docker will then run the default command executed for the application. This can range from printing a help message to the terminal to executing a complex workflow using multiple applications in your image. If there is no default command to execute, the Docker container will simply run Bash.

```
docker run <docker-image>
```

You can also run specific applications within a container by specifying the application after the command.

```
docker run <docker-image> <application>
```

Docker containers will execute non-interactively by default. You can run a container interactively with the `-it` flag:

```
docker run -it <docker-image>
```

Using all of this we can effectively *shell* into our container by specifying bash as our application and passing the `-it` flag.

```
docker run -it <docker-image> bash 
```

Shelling into a container interactively will take you into the root directory of the container. From here you can run applications or tools that have been built into the container. By default, Docker containers will have very few tools available for users. If you need generic Linux tools, you will want to include a base Linux distribution.

**It is important to note that when you run a Docker image you are actually running an instance of that image called a container. Because of this, any changes you may make to the container will be lost on exiting that process.**

Example:

Say we have an image named: *example-python* and we wish to interactively run the Python application within the container. If Python is set up to be the default application of this container, we can do this with the command:

```
docker run -it example-python 
```

If Python is not the default application of the container, then we can specify the Python application by appending python to the end of the command:

```
docker run -it example-python python
```

### Building a Docker image

To build your own custom Docker images that can then be run as containers, you will need to first create a Dockerfile. As stated above, a Dockerfile is essentially a recipe that specifies a source image to build upon, along with a set of instructions Docker will run when building the new image. The Dockerfile will also contain a set of instructions that Docker can run by default when the image is executed as a container instance.

Just like a Makefile, a Dockerfile must be named `Dockerfile and will look something like this:

```dockerfile
FROM 	ubuntu:18.04

RUN 	apt-get update; \
   		apt-get install nano -y; \
   	    apt-get install gcc -y; \
  	    mkdir target;

CMD		echo “Default Command”

WORKDIR /target
```



The `FROM` tag indicates the source image you wish to build upon.

The `RUN` tag indicates commands that you wish to run inside the container.

The `CMD` tag indicates the default command you wish your container to run (optional)

The `WORKDIR` tag indicates the directory you wish start in when running the container.

Docker will parse through the Dockerfile and build the image exactly as you’ve specified. There is a large assortment of commands that can be utilized in a Dockerfile including default file transfers, volume mounting, changing the default shell, and more. Read more about creating Dockerfiles here: <https://docs.docker.com/engine/reference/builder/>

In the directory with your Dockerfile, you can build your Docker image with the following command:

```
docker build -t <container-name> .
```

The `-t` flag specifies the name or title of container. If you do not provide a title for the container then docker will assign the image with an auto-generated name.

### File access

By default, Docker containers are run without access to any part of the host file system. Luckily we can use Docker mounts to circumvent this restriction and link a location in the container file system with a location in the host file system. Directories linked this way will be visible to both the host operating system and the container. There are 2 different forms of mounting available to Docker containers: **Bind mounts** and **Volume mounts**.

#### Bind Mounts

A bind mount is a simple binding between a folder on the host filesystem and a folder on the container filesystem. All files within the bind mount are available to both container and host operating systems. To invoke a bind mount, simply add the following to your docker run script: 

```
docker run --mount type=bind,source=<host-folder>target=<container-folder> <docker-image>
```

#### Volume Mounts

Similar to a bind mount, a volume mount is a simple bind between a folder on the host filesystem and and a folder on the container filesystem. Volumes, however, are completely managed by Docker. Because of this, volumes must be managed much like containers and images. You must first create a volume with the command:

```
docker create volume <volume-name>
```

Then to invoke a volume mount, simply add the following to your docker run script:

```
docker run --mount type=volume,source=<volume>target=<container-folder> <docker-image>
```

Docker volumes are almost entirely managed by Docker so you will not be able to specify the location of your volume in the filesystem directly.  

### Docker Hub

Docker Hub is Docker’s solution for cloud storage of Docker images. Docker Hub is a repository system that allows users of docker to upload or download docker images from public or private repositories. Unlimited public repositories are available for free while users are limited to 1 private repository on free accounts. To pull an image from Docker Hub, simply type:

```
docker pull <image-name>
```

To push a Docker image to a new repository or existing repository, begin by logging into your Docker Hub account via web browser and creating a new repository. Take note of the repository name being `<your-docker-username>/<repository>`. Then, log into your docker account within your host machine by typing:

```
docker login --username=<your-docker-username>
```

...and type in your password to finish logging in. From here we must create a tag for the image we would like to push. First we obtain the image’s Image ID by utilizing the `docker image ls` command. Once we obtain this information, we can tag our image to our repository by typing:

```	
docker tag <image-ID> <your-docker-username>/<repository>:<tag>
```

We can then push our image with the command:

```
docker push <your-docker-username>/<repository>
```
-->
## Singularity

Singularity is a containerization software package that does not require users to have administrative privileges when running containers, and can thus be safely used on Research Computing resources such as RMACC Summit and Blanca. Singularity is preinstalled on Research Computing resources, so all that is needed to run Singularity containers is to load the Singularity module on a compute node on RMACC Summit or Blanca:

```
module load singularity/3.0.2
```

Much like Docker, Singularity is a containerization software designed around compartmentalization of applications, libraries, and workflows. This is done through the creation of Singularity images which can be run as ephemeral Singularity containers. Unlike Docker, however, Singularity does not manage images, containers, or volumes through a central application. Instead, Singularity generates saved image files that can either be mutable or immutable based on compression.

### Singularity Hub

Singularity Hub is a container registry that allows users to pull images from a server and into a system with Singularity installed. Singularity Hub uses Github to host image recipes, builds images in the cloud from these recipes, and places the resulting images in the Singularity Hub registry. .

**Note:** You do not need an account with Github if you only wish to pull Singularity images. 

<https://singularity-hub.org/>

Singularity Hub has a variety of useful prebuilt images for different software packages and workflows so be sure to check if the software you need is already available.

**Note:** As of 2019, there are presently two Singularity container registries. The former is Singularity Hub, described above, which is managed by Stanford University and Lawrence Berkeley National Laboratory.  The latter is the Sylabs Singularity Container Library, which was created in late 2018 when Singularity was spun off into the private company Sylabs.  Below we provide documentation on how to pull images from either repository, and on how to build images on Singularity Hub via Github, and in the Sylabs Singularity Container Library using their “Remote Builder” functionality.

### Pulling Singularity Images

Because we cannot build our own Singularity images on HPC systems, we must instead bring our images over from another location. Pulling images from public repositories is often the easiest solution to this problem. 

We can use the `singularity pull` command to remotely download our chosen image file. The command requires the container registry we would like to use, followed by the repository’s name:

```
singularity pull <container-registry>://<repository-name>
```

A container registry is simply a server that manages uploaded containers. Some examples of these container registries include Docker Hub, Singularity Hub, and the Singularity Container Library.

Pull from Docker Hub:

```
singularity pull docker://another:example
```

Pull from Singularity Hub:

```
singularity pull shub://example:repo
```

Pull from Singularity Container Library (Singularity version 3.0 and greater):

```
singularity pull library://example:repo
```

Lastly we can rename the Singularity image file pulled from a repository by utilizing the `-n/--name` flag.

```
singularity pull -n ExampleContainer.sif shub://example:tag
```

Example: 

Pulling the Docker image of the latest tag of ubuntu can be done with the following command:

```
singularity pull docker://ubuntu:latest
```

### Running a Singularity image as a container

Singularity images can be run as containers much like Docker images. Singularity commands, however, follow a bit more nuanced syntax depending on what you’d like to do. After pulling your image from either Docker Hub or Singularity Hub, you can run the image by using the `singularity run` command. Type:

```
singularity run <image-name>
```

Running a Singularity container will execute the container’s default program that is specified in container definition file. To execute specific programs in your container, we can use the `singularity exec` command, and then specify the program:

```
singularity exec <image-name> <program>
```

Much like specifying an application in Docker, this will allow a user to execute any program that is installed within your container. Unlike Docker however, you do not need to specify a shell application to shell into the container. We can simply use the `singularity shell` command:

```
singularity shell <image-name>
```

*Example:*

Say we have a Singularity image that contains python 3.7 as the default software, and we want to run python from the container. We can do this with the command:

```
singularity run python-cont.img
```

If the default application for the image is not python we could run python as follows:

```
singularity exec python-cont.img python
```

### File Access

By default most user-owned files and directories are available to any container that is run on RMACC Summit and Blanca (this includes files in `/home/$USER`, `/projects/$USER`, `/scratch/summit/$USER` and `/rc_scratch/$USER`). This means that normally a user will not need to bind any folders to the container’s directory tree. Furthermore, a container will also have access to the files in the same folder where it was initialized. 

Sometimes, however, certain folders that are not bound by default may be necessary to run your application. To bind any additional folders or files to your Singularity container, you can utilize the -B flag in your singularity run, exec, and shell commands. To bind an additional folder to your Singularity container, type:

```bash
singularity run -B /source/directory:/target/directory sample-image.img
```

Additionally you can bind directories by utilizing the `SINGULARITY_BINDPATH` environment variable. Simply export a list of directory pairs you would like to bind to the your container:

```bash
export SINGULARITY_BINDPATH=/source/directory1:/target/directory1,\
/source/directory2:/target/directory2
```

Then run, execute, or shell into the container as normal.

### Building a Singularity image

**Important: You cannot build Singularity images directly on Summit. If you cannot build an image on your local machine you will need to build it on Singularity Hub or Sylabs Remote Builder.**

#### Singularity Build

Just like Docker, Singularity allows a user to build images using a *definition file*. The file is saved with the name “Singularity” and contains instructions on how to prepare a Singularity image file. Just like a Dockerfile, this file has a variety of directives that allow for the customization of your image. A sample image would look something like this: 

```
Bootstrap: shub
From: ubuntu

%help
	I am help text!

%setup		
	apt-get update
	apt-get install nano
	apt-get install gcc 

%runscript
	echo “hello! I am a container!”
```

Once you have written your Singularity recipe, you can build the application either remotely (see below) or locally with the singularity build command. To build a Singularity image locally, type:

```
sudo singularity build <img-name.img> <recipe-name.def>
```

**Again, it is important to note that if you build an image locally as described above, you must build your image on a computer that you have administrative privileges on. If you do not have administrative privileges you will not be able to build the container in this manner.  Fortunately, there are other ways to build containers remotely, which are discussed next.**

#### Building Images Remotely with Singularity Hub

To  build images with Singularity Hub, you must first create a Github account at [https://github.com/join](https://github.com/join) if you do not have one already. After completing this step log into your github account and create an empty repository. 

After creating your repository, upload a Singularity definition file named “Singularity” to the repository. This is all we need to generate our Singularity image.

Now, log into Singularity Hub with your Github credentials and navigate to “My Container Collections” and click the link “Add a Collection.” From here a list of Github repositories you contribute to will be listed. Simply click the button on the repository you wish to add to Singularity Hub.

Your container should build automatically if you have a recipe file named “Singularity” within your repository. By default Singularity Hub will attempt to build any time something is pushed to the github repository. This can be changed in the settings tab in the containers build page.  If the build fails the first time, revise the Singularity recipe and the build will initiate again.

More on building containers: <https://www.sylabs.io/guides/3.0/user-guide/build_a_container.html>

#### Building Images Remotely with the Singularity Remote Builder

With Singularity 3.0, users have the ability to build containers remotely through Sylabs remote builder. Unlike Singularity Hub though, the Singularity remote builder can be utilized directly on the command line from RMACC Summit or Blanca without needing to upload to a repository.  

To begin using Singularity Remote Builder, navigate to your home directory and run the commands:

```
mkdir .singularity
cd .singularity 
```

Now on your local machine, navigate to: <https://cloud.sylabs.io/auth>

...and log into Sylabs with your Google, Github, Gitlab, or Microsoft account. Once you have logged into Sylabs, provide a label for your token under the field “Create A New Access Token” and click “Create a new Token.” This will generate a large string that will be read by Singularity on RMACC Summit or Blanca.

Now on RMACC Summit or Blanca run the command:

```
echo “<your-token>” > ~/.singularity/sylabs-token
```

After this you can now build containers through the Sylabs remote builder on RMACC Summit or Blanca. Simply load Singularity 3.0.2 into your module stack and run the command:

```
singularity build --remote <desired-image-name> <your-recipe>
```

### Building MPI-enabled Singularity images
MPI-enabled Singularity containers can be deployed on RMACC Summit with the caveat that the MPI software within the container stays consistent with MPI software available on the system. This requirement diminishes the portability of MPI-enabled containers, as they may not run on other systems without compatible MPI software. Regardless, MPI-enabled containers can still be a very useful option in many cases. 

Here we provide an example of using a gcc compiler with OpenMPI. RMACC Summit uses an Omni-Path interconnect (a low latency network fabric that enables MPI to be efficiently implemented across nodes). In order to use a Singularity container with OpenMPI (or any MPI) on Summit, there are two requirements:

Singularity container needs to have Omni-Path libraries installed inside. 
OpenMPI needs to be installed both inside and outside of the Singularity container. More specifically, the SAME version of OpenMPI needs to be installed inside and outside (at least very similar, you can sometimes get away with two different minor versions, ex: 2.1 and 2.0). 

The following Singularity recipe ensures that OpenMPI 2.0.1 is installed in the image, which matches the openmpi/2.0.1 module that is available on RMACC Summit. This recipe can be used as a template to build your own MPI-enabled container images for RMACC Summit and can be found at: [https://github.com/ResearchComputing/core-software/tree/master/singularity](https://github.com/ResearchComputing/core-software/tree/master/singularity)

Once you’ve built the container with one of the methods outlined above, you can place it on RMACC Summit and run it on a compute node. The following is an example of running a gcc/OpenMPI container with Singularity on RMACC Summit. The syntax is a normal MPI run where multiple instances of a Singularity image are run. The following example runs `mpi_hello_world` with MPI from a container.

```
ml gcc/6.1.0
ml openmpi/2.0.1
ml singularity/3.0.2

mpirun -np 4 singularity exec openmpi.sif mpi_hello_world"
```

Note that it is also possible to build intel/IMPI containers for use on RMACC Summit, which are likely to have enhanced performance on Summit’s intel architecture compared to gcc/OpenMPI containers. If you would like assistance building MPI-enabled containers contact <rc-help@colorado.edu>.
