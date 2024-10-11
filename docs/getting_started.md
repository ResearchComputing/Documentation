# Getting Started 

HPC /documentation can be overwhelming 

## High Performance Computing 

```{eval-rst}
.. graphviz::
    :name: "Getting started HPC flowchart"
    :caption: Getting started on CURC resources flowchart 
    :align: center

     digraph "" {
         bgcolor="transparent";
         ranksep="0.5 equally";
         node [fontname="Verdana", fontsize="12", color="#CFB87C", style="filled", fillcolor="black", penwidth="2", fontcolor="white"];
         edge [color="#CFB87C", fillcolor="black", penwidth="1.5"];


         logging_in [label="Get an account", href="./access/logging-in.html", target="_blank"]
         policies [label="CURC Policies", href="./additional-resources/policies.html", target="_blank"]
         duo [label="DUO Authentication", href="./access/duo-2-factor-authentication.html", target="_blank"]
         compute_env [label="What does the HPC system look like?", style="filled,dashed", penwidth="3"]
         running_jobs [label="How do I run a job?"]
         clusters [label="What clusters are available?"]
         node_type [label="Node types", href="./compute/node-types.html", target="_blank"]
         filesystem [label="CURC filesystem", href="./compute/filesystems.html", target="_blank"]
         data_transfer [label="Transferring data", href="./compute/data-transfer.html", target="_blank"]
         petalibrary [label="PetaLibrary", href="./storage/petalibrary/index.html", target="_blank"]
         alpine [label="Alpine", href="./clusters/alpine/index.html", target="_blank"]
         blanca [label="Blanca", href="./clusters/blanca/blanca.html", target="_blank"]
         slurm [label="Slurm", href="./running-jobs/job-resources.html", target="_blank"]
         interactive [label="Interactive jobs", href="./running-jobs/interactive-jobs.html", target="_blank"]
         batch [label="Batch jobs", href="./running-jobs/batch-jobs.html", target="_blank"]
         ood [label="Open OnDemand", href="./open_ondemand/index.html", target="_blank"]
         using_software [label="How do I run software?"]
         modules [label="The module system", href="./compute/modules.html", target="_blank"]
         container [label="Containerization", href="./software/containerization.html", target="_blank"]
         spack [label="Spack", href="./software/spack.html", target="_blank"]
         conda [label="Conda environments", href="./software/python.html", target="_blank"]

         logging_in -> policies
         logging_in -> duo
         logging_in -> compute_env
         compute_env -> node_type
         compute_env -> filesystem
         filesystem -> data_transfer
         filesystem -> petalibrary
         filesystem -> clusters
         node_type -> clusters
         clusters -> alpine
         clusters -> blanca
         alpine -> running_jobs
         blanca -> running_jobs
         running_jobs -> slurm
         slurm -> interactive
         slurm -> batch
         slurm -> ood
         interactive -> using_software
         batch -> using_software
         ood -> using_software
         using_software -> modules
         using_software -> container
         using_software -> spack 
         using_software -> conda
     }
```

## Cloud computing 

```{eval-rst}
.. graphviz::
    :name: "Getting started Cloud flowchart"
    :caption: Getting started on Cloud resources flowchart 
    :align: center

     digraph "" {
         bgcolor="transparent";
         ranksep="0.5 equally";
         node [fontname="Verdana", fontsize="12", color="#CFB87C", style="filled", fillcolor="black", penwidth="2", fontcolor="white"];
         edge [color="#CFB87C", fillcolor="black", penwidth="1.5"];

         cloud [label="Cloud computing assistance"]
         aws [label="Amazon Web Services"]
         azure [label="Microsoft Azure"]
         gcp [label="Google Cloud Platform"]
         cumulus [label="CUmulus (On-Premise Cloud)"]

         cloud -> aws
         cloud -> azure
         cloud -> gcp 
         cloud -> cumulus
     }
```