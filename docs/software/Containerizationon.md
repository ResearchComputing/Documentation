# Containerization 

When installing software, you may come across applications that have complex chains of dependencies that are challenging to compile and install. Some software may require very specific versions of libraries that may not be available on Alpine or conflict with libraries needed for other applications. You may also need to move between several workstations or HPC platforms, which often requires reinstalling your software on each  system. Containers are a good way to tackle all of these issues and more.

## Containerization Fundamentals

Containers build upon an idea that has long existed within computing: hardware can be emulated through software. **Virtualization** simulates some or all components of computation through a software application. Virtual machines use this concept to generate an entire operating system as an application on a host system. Containers follow the same idea, but at a much smaller scale and contained within a system's kernel.

**Containers** are portable compartmentalizations of an operating system, software, libraries, data, and/or workflows. Containers offer portability and reproducibility. 

- Portability: containers can run on any system equipped with its specified container manager.
- Reproducibility: because containers are instances of prebuilt isolated software, software will always execute the same every time.

Containers distinguish themselves through their low computational overhead and their ability to utilize all of a host system’s resources. Building containers is a relatively simple process that starts with a container engine.

## Container engines

[Docker](https://www.docker.com/) is the most widely used container engine, and  can be used on any system where you have administrative privileges. _Docker cannot be run directly on high-performance computing (HPC) platforms like Alpine because users do not have administrative privileges._ CURC documentation on Docker can be found below. 

[Apptainer](https://apptainer.org/) (formerly Singularity) is a container engine that does not require administrative privileges to execute. Therefore, it is safe to run on HPC platforms like Alpine or Blanca.   

## Apptainer

Apptainer is a containerization software package that does not require users to have administrative privileges when running containers, and can thus be safely used on Research Computing resources. Apptainer is installed directly on all Alpine compute nodes, so there is no need to load any module to run Apptainer commands on Alpine. However, **Apptainer is not currently installed on Blanca nodes**. It is recommended that users running containers on Blanca load the newest Singularity module, rather than Apptainer: 

```
module load singularity/3.7.4
```

**Note that users who use Singularity instead of Apptainer will not be able to deploy all of the functionality illustrated in this documentation.** Most notably, users will be unable to deploy `build` functionality when using Singularity instead of Apptainer. 

Much like Docker, Apptainer is a containerization software designed around compartmentalization of applications, libraries, and workflows. This is done through the creation of compressed images in the `.sif` format which can be run as ephemeral containers. Unlike Docker, however, Apptainer does not manage images, containers, or volumes through a central application. Instead, Apptainer generates saved image files that can either be mutable or immutable based on compression.

### Pulling Images

In the case that there is an existing container for an application, we can simply load the images from another location. Pulling images from public repositories is often the easiest method of using a containerized application. 

We can use the `apptainer pull` command to remotely download our chosen image file and convert it to the Apptainer `.sif` format. The command requires the container registry we would like to use, followed by the repository’s name:

```
apptainer pull <localname>.sif <container-registry>://<repository-name>
```

Where `<localname>.sif` is the name you choose for the Apptainer image. 

A container registry is simply a server that manages uploaded containers. Docker Hub is the most widely used register. To pull a container image from Docker Hub:

```
apptainer pull docker://another:example
```

### Running a SIF image as a container

SIF images can be run as containers much like Docker images. Apptainer commands, however, follow a bit more nuanced syntax depending on what you’d like to do. After pulling your image from Docker Hub you can run the image by using the `apptainer run` command. Type:

```
apptainer run <image-name>
```

Running a container will execute the default program that the container developer will have specified in the container definition file. To execute specific programs in your container, we can use the `apptainer exec` command, and then specify the program:

```
apptainer exec <image-name> <program>
```

Much like specifying an application in Docker, this will allow a user to execute any program that is installed within your container. Unlike Docker however, you do not need to specify a shell application to shell into the container. We can simply use the `apptainer shell` command:

```
apptainer shell <image-name>
```

Note that both `apptainer run` and `apptainer shell` will create an interactive terminal within the container, whereas `apptainer exec` will not. Rather, `apptainer exec` will execute the provided command and return the output. 

*Example:*

Say we have an image that contains Python 3.7 as the default software, and we want to run Python from the container. We can do this with the command:

```
apptainer run python-cont.sif
```

If the default application for the image is not Python we could run Python as follows:

```
apptainer exec python-cont.sif python
```

### File Access

By default, only `/home/$USER` is available within any given container. This means that a user will need to bind any other required folders to the container’s directory tree. Furthermore, a container will also have access to the files in the same folder where it was initialized (`$PWD`). 

To bind any additional folders or files to your container, you can utilize the `-B` flag in your Apptainer run, exec, and shell commands:

```
apptainer run -B /source/directory:/target/directory sample-image.sif
```

Alternatively, users wishing to bind their entire CURC filesystem to a container do not necessarily need to specify the target directory in the container when using `run`, `shell`, and `exec` commands. Rather, you can run the container as follows: 
```
apptainer run -B /projects/$USER,/pl/active,/scratch/alpine/$USER sample-image.sif
```

Additionally, you can bind directories by utilizing the `APPTAINER_BINDPATH` environment variable. Simply export a list of directory pairs you would like to bind to the your container:

```
export APPTAINER_BINDPATH=/source/directory1:/target/directory1,\
/source/directory2:/target/directory2
```

Then run, execute, or shell into the container as normal. 

### Building a SIF image

In the event that a container is unavailable for a given application, you may need to build your own container from scratch. Apptainer allows a user to build images using a *definition file*. This file has a variety of directives that allow for the customization of your image. A sample image would look something like this: 

```
Bootstrap: docker
From: ubuntu:20.04

%help
	I am help text!

%setup		
	apt-get update
	apt-get install nano
	apt-get install gcc 

%runscript
	echo “hello! I am a container!”
```

#### Apptainer Build

Once you have written your Apptainer definition file, you can build the application locally on **Alpine** with the `apptainer build` command, as follows:

```
apptainer build <localname>.sif <recipe-name>.def
```

Although the above build command can be sufficient, for more complex container builds, it may be necessary to add the `--fix-perms` and `--fakeroot` options to `apptainer build`. Please see the "Useful Apptainer Features" section below.

### Useful Apptainer Features

When using/constructing containers using Apptainer, there are a number of tools that users can deploy to ensure desired functionality. Features of high-importance are as follows: 

* **Fakeroot**: Fakeroot is a feature which allows a non-root user to obtain nearly-root-level administrative permissions **only within the requisite container**. This affords users the ability to perform high-level operations within a container, such as: 

<ol>
  <li>Package installation using `sudo`</li>
  <li>Changing user/group identity</li>
  <li>Permissions changes</li>
</ol> 

Note that any changes made within the container with Fakeroot are not reflected outside of the container. Users can deploy fakeroot by running any of `shell`, `exec`, `run`, or `build` with the `--fakeroot` flag. For example:
```
apptainer build --fakeroot test.sif test.def
```

* **Fix-Perms**: Performing a container operation with the fix-perms flag will ensure that the user has read, write, and execute permissions for all container content. This flag can often be needed for software installs (e.g. `apt install <program>`). For example, if you receive a error stating permission issues, this command often resolves those errors. Users can deploy fix-perms by running `build` with the `--fix-perms` flag. For example:
```
apptainer build --fix-perms test.sif test.def
```

* **Sandbox**: Building containers can be a time-consuming process if building from the definition file. This is because you may have build errors that need to be resolved, which requires that you rebuild the container multiple times. For this reason, you may want to perform iterative installs within the container first to ensure compatibility, then transfer these commands to a definition file. For this purpose, you can use the sandbox option. Users can construct a sandbox by using the `--sandbox` flag. For example: 
```
apptainer build --sandbox test.sif
```

From there, you can install software and dependencies directly within the sandbox and have those changes reflected in the sandbox using `apptainer shell --writable <my.sif>`. **Important: a sandbox cannot be converted into a definition file. This means there is no record of what you installed in the sandbox. It is highly suggested that you add actions completed in the sandbox (e.g. software installs) to a definition file as you modify the sandbox. This will ensure that you can reproduce the sandbox at a later time.**

### Building MPI-enabled images
MPI-enabled Apptainer containers can be deployed on Alpine with the caveat that the MPI software within the container has a similar (not necessarily exact) version with MPI software available on the system. This requirement diminishes the portability of MPI-enabled containers, as they may not run on other systems without compatible MPI software. Regardless, MPI-enabled containers can still be a very useful option in many cases. 

Here we provide an example of using a gcc compiler with OpenMPI. Alpine uses an Infiniband interconnect. In order to use a Singularity container with OpenMPI (or any MPI) on Alpine, OpenMPI needs to be installed both inside and outside of the container. More specifically, the _same_ version of OpenMPI needs to be installed inside and outside (at least very similar, you can sometimes get away with two different minor versions, e.g. 2.1 and 2.0). 

CURC can provide users with a recipe that ensures the appropriate version of OpenMPI is installed in the image. This recipe can be used as a template to build your own MPI-enabled container images for Alpine.

Once you’ve built the container with one of the methods outlined above, you can place it on Alpine and run it on a compute node. The following is an example of running a gcc/OpenMPI container with Apptainer on Alpine. The syntax is a normal MPI run where multiple instances of a Singularity image are run. The following example runs `mpi_hello_world` with MPI from a container.

```
ml gcc/11.2.0
ml openmpi/4.1.1

mpirun -np 4 apptainer exec openmpi.sif mpi_hello_world"
```

## Docker

**Note:** Docker containers cannot be run *with Docker* on Alpine or Blanca, because the Docker software is not HPC-safe. Instead, Docker containers are run using Apptainer.  See the documentation on Apptainer above if you wish to run a Docker container on Alpine or Blanca. 

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

To run a Docker container on your laptop or other system on which you have Docker installed, simply type the command:

```
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

Docker Hub is Docker’s solution for cloud storage of Docker images. Docker Hub is a repository system that allows users of docker to upload or download docker images from public or private repositories. Unlimited public repositories are available for free while users are limited to 1 private repository on free accounts. To pull an image from Docker Hub, use the command:

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

Note that it is also possible to build intel/IMPI containers for use on Alpine. If you would like assistance building MPI-enabled containers contact <rc-help@colorado.edu>.

## Requesting a Container Installation

Users can request that a container be installed on our system by filling out the [Software Request Form](https://www.colorado.edu/rc/userservices/software-request). Please note that all software installations are “Best Effort” and are not guaranteed. RC reserves the right to deny any software installation that is requested on CURC resources. Additionally, please review the [Alpine Software Policy](https://curc.readthedocs.io/en/latest/clusters/alpine/software.html#alpine-software-policy). 