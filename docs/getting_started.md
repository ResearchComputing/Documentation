# Getting Started 

HPC /documentation can be overwhelming 

## High Performance Computing 

```{eval-rst}
.. raw:: html
   :file: ../igraphviz_flowcharts/generated_images/getting_started_hpc_flowchart.svg
```

## Cloud computing 

```{eval-rst}

.. graphviz::

     digraph {
        bgcolor="transparent";
        ranksep="0.5 equally";
        node [fontname="Verdana", fontsize="12", color="#CFB87C", style="filled", fillcolor="black", penwidth="2", fontcolor="white"];
        edge [color="#CFB87C", fillcolor="black", penwidth="1.5"];

        cloud [label="Cloud computing assistance"];
        aws [label="Amazon Web Services"];
        azure [label="Microsoft Azure"];
        gcp [label="Google Cloud Platform"];
        cumulus [label="CUmulus (On-Premise Cloud)"];

        cloud -> aws;
        cloud -> azure;
        cloud -> gcp;
        cloud -> cumulus;
     }
```