
# Establish a Database to query Twitter and Store Results

___Learning Objectives:___
* Download software to our new CUmululs instance.
* Run a simple web application on our instance.
* Run a simple persistent db from our instance. 

## Introduction

We will use CUmulus to create an instance with a persistent database (MySQL) and a python application which will use the Twitter API and a Flask web server to query data from Twitter and store it in the database. The following tutorial uses Docker containers and the Docker-Compose orchestration tool to allow simple build-up/tear-down and development of the application.

> Note: An in depth discussion of Docker and Docker-Compose is out of the scope of this demo, but further reading will be provided.

Our main objective in tutorial is to demonstrate potential workflows that could be useful in research. This tutorial showcases a few important features of Cumulus:
* A persistent workflow not limited by wall clock times
* User administration of compute resources (using root privileges for applications such as Docker) 
* Routable floating IPs that enable you to access your instance via the Public Internet

## Tutorial


Before we can get this application up and running in a CUmulus instance we have some house-keeping to take care of. Many of the steps below assume you have worked through [tutorial1](./cumulus1.md), which describes the instance creation process.

###  Part 1: Instance Setup

We need a working CUmulus instance running Ubuntu with http port exposed (default 80) and a public floating IP. 
* Adding a routable http port to an instance can be done within the instance creation launcher by adding the `http` security groups or after the instance has been created by editing the security groups of the individual instance.
* Add a floating IP after the instance has been created.
	- Log into your instance via ssh (see  [tutorial 1](./cumulus1.md)); *ensure you are on the CU VPN*.
	- Updating and upgrading you instance at this point is a good idea, you can do so with the following command:
		 ```
		 $ sudo apt-get update && sudo apt-get upgrade -y
		``` 

###  Part 2: Getting your Twitter API Credentials

 In order to query Twitter with the Twitter API V2 you must first obtain a Twitter Developer Account and get access to a number of secret API keys:
*   go to the following website [https://developer.twitter.com/](https://developer.twitter.com/content/developer-twitter/en.html) and create an account.
* Once you have verified your email you can log into your account. You should be able to create a new app on the following webpage: [https://developer.twitter.com/en/apps](https://developer.twitter.com/en/apps)
* Fill in all the details about your app and then create your access token.
* Make a note of your consumer key, consumer secret, OAuth access token and OAuth access token secret. These are needed to connect to the API.

###  Part 3: Getting the Source Code

Download the source code into your home (`~`) directory, unzip it, and cd into it: 

```
$ cd ~
$ wget https://github.com/ResearchComputing/CUmulus_tutorials/raw/main/app.zip
$ unzip ~/app.zip
$ cd ~/app
```

###  Part 4: Configuring your Environment

 Once you have your Twitter API keys, we can set up our config file which will allow for our applications to use the necessary passwords, ports, keys, etc. as environment variables.
* Using a text editor of your choice create the file `~/app/.env` (*note the period in front of `.env`*) and paste the following lines in adding your web port (default 80 for http in CUmulus), your mysql password (you choose this), and your Twitter API keys. You can use the examples to format your environment variables.
```
#### Comment out or delete any unused entries

#### EXAMPLE 
# DO NOT USE QUOTES TO ENCLOSE THE VALUES
EXAMPLE_VARIABLE=true
EXAMPLE_PORT=1234
EXAMPLE_PASSWORD=kdos9lsk@1l1!
EXAMPLE_EMAIL=myemail@domain.com
EXAMPLE_IP=123.123.123.123

#### BELOW ARE SOME OF THE VARIABLES USED IN docker-compose.yml

WEB_PORT=

MYSQL_ROOT_PASSWORD=

API_KEY=
API_KEY_SECRET=
BEARER_TOKEN=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=
```

Okay, now we can get into the  real content of this Demo!

###  Part 5: Setting up Docker

The next thing we'll need to do is install Docker. Docker is an open source containerization platform. It enables developers to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment. For a great overview of Docker containerization visit https://docs.docker.com/get-started/overview/. In this tutorial we will use Docker to "pull" and "run" a mysql database image that we can store data (in this case tweets) into. A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments.  Instead of downloading mysql directly to the host machine (your instance) and having to deal with dependencies and uninstalling/fixing if anything goes wrong we can use the mysql image which we can easily create/remove a Docker container from.

The python application will also be containerized when run, but in order to give you a platform to iterate and develop this application on your own going forward we are going to include the source code and Dockerfile which will allow you to tweak the application, build the container back up to use it, and even [publish the container](https://docs.docker.com/docker-hub/) if you'd like.

#### Installing and Testing

1) The first thing we'll need to do is install Docker. There are many ways to install Docker based on your OS, but we're going for an [Ubuntu install](https://docs.docker.com/engine/install/ubuntu/) in this tutorial. We will assume this is a brand new instance so we don't have to check for previous versions of Docker so we will go straight to the "install with the convenience script" section (bottom of the page). From the home directory (`~`) of your instance run the following: 
	```
	 $ curl -fsSL https://get.docker.com -o get-docker.sh
	 $ sudo sh get-docker.sh
	```
2) To test the install we can check for versioning, then run a Docker hello world.
	- Check version:
	```
	$ sudo docker --version
	```
	- Run docker hello world:
	```
	sudo docker run hello-world
	```
	It will download a test container and run it. You should see an output similar to the one below:
	```
	Hello from Docker!
	This message shows that your installation appears to be working correctly.

	To generate this message, Docker took the following steps:
	 1. The Docker client contacted the Docker daemon.
	 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
	    (amd64)
	 3. The Docker daemon created a new container from that image which runs the
	    executable that produces the output you are currently reading.
	 4. The Docker daemon streamed that output to the Docker client, which sent it
	    to your terminal.

	To try something more ambitious, you can run an Ubuntu container with:
	 $ docker run -it ubuntu bash

	Share images, automate workflows, and more with a free Docker ID:
	 https://hub.docker.com/

	For more examples and ideas, visit:
	 https://docs.docker.com/get-started/
	```
Docker is setup!

###  Part 6: Setting  up Docker-Compose

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. Read more about docker compose here: https://docs.docker.com/compose/.

#### Installing and Testing
1) We'll install docker-compose next (https://docs.docker.com/compose/install/), from the home directory (`~`) of your instance run the following command to download the current stable release of Docker Compose:
	```
	 $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	```
	Apply executable permissions to the binary:
	```
	$ sudo chmod +x /usr/local/bin/docker-compose
	```
2) Test the Docker Compose installation by verifying the version:
	```
	$ docker-compose --version
	```
	You should see the following:
	```
	ubuntu@RC-teaching:~$ docker-compose --version 
	docker-compose version 1.29.2, build 5becea4c
	```

We define two images in our `docker-compose.yml` file, if you'd like you can take a look inside the Compose file. Briefly, you will see that we start off by explicitly declaring the Compose version then move into the images (called "services" in the context of Compose) in which we see the two containers we'll use:

#### Docker images
1)  Python Web App: This container is build and run straight from this directory (i.e. we're not pulling it from a docker repository). In the compose file we pass the web app environment variables (such as our port and Twitter API keys) which it will access directly from the `.env` file. This particular application was modeled after the [official Docker Python App tutorial](https://docs.docker.com/language/python/) and the twitter python api tutorial from [Skolo Online Learning](https://github.com/skolo-online/twitter-v2-api). The twitter application uses a combination of a Flask web server and the Tweepy Python library to query twitter then return those results to us via a a browser. Feel free to dig into the `app.py` page for a look into how this application actually works.

2) [Official mysql database](https://hub.docker.com/_/mysql): We use the official mysql database image hosted on the Dockerhub repository and pass it the mysql password you chose in `.env` as well as some paths for volumes (which we will discuss below)

#### Persistent Data
When a container runs, it uses the various layers from an image for its filesystem. Each container also gets its own “scratch space” to create/update/remove files. Any changes won’t be seen in another container, _even if_ they are using the same image. This means that anytime you stop a container from running, all of the data will vanish. There are a couple different ways of persisting data while using Docker (read more https://docs.docker.com/storage/volumes/) such as volumes and bind-mounts. Here we will be using volumes which we define at the bottom of the Compose file.


###  Part 7: Running the Application

We're all set and ready to run our application and database! From the `~/app` directory run:
```
$ sudo docker-compose up --build -d
```
This command brings up *all* of the images in the `docker-compose.yml` file (the "up"), builds the web application (the "--build"), and run's the containers in "detached" mode (the "-d") which will give us access to our terminal once the images have been pulled and containers are running. If you need to debug you can leave off the "-d" flag to see the output straight to the console, then exit and stop the containers with "ctr-c."

If all went well, in a browser you can navigate to `<your floating IP>:80`, for example: 123.456.789.123:80 and find a web page which allows you query Twitter via a keyword and will return the last 10 tweets. On the back-end, those tweets are being stored in our mysql database. You can view the full database store via the browser as well by navigating to 123.456.789.123:80/tweets. This route just spits out all of the data we're collecting from the tweets, in this case just username and tweet contents. If you go back to the original tweet query page you can search for more tweets and see that those tweets will be populated in our database for later retrieval. 

###  Part 8: Finishing up

Your application is up and running and accessible through the Public internet! Because this is a public facing page, I would suggest bringing down the application after playing around with it a bit in order to prevent others from finding and filling up the database. You can do that with the following command from  the `~/app` directory:
```
$ docker-compose down
```
This will shut down all of the containers.

This Demo demonstrated a basic workflow to get a web application and persistent data via Docker containers running on CUmulus. Docker containers allow for easy creation and tear-down of your applications and allows them to persist as long as you'd like them to. This demo took advantage of:
* A persistent workflow not limited by wall clock times: this application could be long-lived querying data whenever necessary. 
* User administration of compute resources: using root privileges to download software and run applications such as Docker.
* Routable floating IPs: we made our application available via http port 80 which allowed us to access access instance via the Public Internet.


> This work has been funded in part by the National Science Foundation under grant OAC-1925766
