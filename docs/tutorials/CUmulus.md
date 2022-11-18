# Clearing the Fog! Getting Started on CUmulus, a Near to the Ground On Campus Cloud Solution


## What is CUmulus?

[Cumulus](https://curc.readthedocs.io/en/latest/hybrid-cloud/cumulus.html) is [CU Research Computing](https://www.colorado.edu/rc)'s free-to-use on-premise cloud service, which supports cases not well-suited for HPC such as web servers, databases, workflow managers, and other long-running services. CUmulus is funded in part by the National Science Foundation under grant OAC-1925766.

Cumulus provides users with persistent or ongoing availability by allocating them a logically isolated section of the cloud

You get your own virtual “world” for experimentation - an environment that can be easily created/deleted.
* Install Software
* Administer your instance (you’re in control!)
* Run applications and jobs
* Interface w/ other CURC services: Blanca, Alpine, PetaLibrary

You can request specific resources (CPU, storage, memory) and can set up persistent storage.

#### Cumulus specifications

* 244 total CPU cores
* 4GB RAM per CPU core
* 101.3TB of object-oriented storage

## What would I do on CUmulus? 

#### Appropriate use cases:
- Workflow management software that monitors/schedules jobs on Summit, Alpine, or Blanca
- Running a research database/website application that queries data stored on CURC PetaLibrary 
- Web-based research “Hubs” (JupyterHub, Rstudio-server, Shiny Apps)
- License servers for software used in CURC ecosystem

#### Inappropriate use cases: 
- Running workflows that can more efficiently be run on Summit, Alpine or Blanca
- Personal websites or websites unrelated to research
- Serverless applications

## Who can use CUmulus? 

CUmulus is a free-to-use cloud system where:
- 80% of cycles: CU Boulder faculty, staff, students, and affiliates
- 20% of cycles: RMACC affiliates (CSU, Wyoming, UC system campuses, [and many more](https://rmacc.org/partners)) 

> To ensure optimal usage, unused cycles are preemptively available to the Open Science Grid ([OSG](https://opensciencegrid.org/))

## How do I access CUmulus? 

_Step 1:_ Users will submit a proposal for your use case (email rc-help@colorado.edu):
* Describe your CUmulus workflow
* Describe why your [workflow is appropriate for CUmulus](https://curc.readthedocs.io/en/latest/hybrid-cloud/cumulus.html#appropriate-use-cases)
* Estimate the resources you require: operating system, CPU cores, disk space, memory

_Step 2:_ The CURC allocation committee reviews your proposal and provide feedback.  This is an iterative process where we work with you to make sure the request for resources fits your (and our) needs. 

_Step 3:_ After iteration, a decision on your proposal is made.  If awarded, you can proceed with [creating a CUmulus instance](./tutorial1/README.md) and start using CUmulus!

## Using CUmulus

Using CUmulus is best explained via a series of tutorials that enable you to learn in a hands-on manner.  The first tutorial, "Creating a CUmulus Instance" is recommended for anyone using CUmulus.  Subsequent tutorials are optional and cover some common use cases and may be useful for informing your how to set up your specific workflow. 

* [Tutorial 1: Creating a CUmulus instance](./cumulus_tutorial1/README.md)
* [Tutorial 2: Establish a MySQL database to query Twitter and store results](./cumulus_tutorial2/README.md)
* [Tutorial 3: Integrating CUmulus with CURC HPC Resources](./cumulus_tutorial3/README.md)
* [Tutorial 4: Mounting filesystems on CURC HPC Resources from CUmulus](./cumulus_tutorial4/README.md)

> This work has been funded in part by the National Science Foundation under grant OAC-1925766
