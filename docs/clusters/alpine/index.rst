Alpine
===============

Starting May 18, 2022, CU Research Computing will be releasing phase 1 of Alpine, the third generation CURC High Performance Computing Cluster. CU Boulder users can begin using Alpine at that time. The warranty of the Summit cluster's storage will end in September of 2022 with the full sun-setting of the Summit system yet to be finalized. 

.. image:: ./images/alpine_summit_timeline.png
  :width: 400
  :align: center

  :alt: Summit-Alpine timeline

**Early Release: Pardon our dust! We are actively developing the Alpine cluster -- if you see or experience any errors or unexpected behavior, please report them to rc-help@colorado.edu**

**Overview:**

Alpine is the University of Colorado Boulder Research Computing's third-generation high performance computing (HPC) cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado Boulder. Additional contributions provided from Colorado State University and Anschutz Medical Campus are planned for the near future. Alpine currently offers 80 compute nodes and a total of 5120 cores.

Alpine can be securely accessed anywhere, anytime using OpenOnDemand or ssh connectivity to the CURC system.

**Hardware Summary:**

Total Core Count: **5120**

Nodes: The Alpine cluster is made up of different types of nodes outlined below.

* **CPU nodes:**
 * 64 AMD Milan Compute nodes (64 cores/node)

* **GPU nodes:**
 * 8 GPU-enabled (3x AMD MI100) atop AMD Milan CPU
 * 8 GPU-enabled (3x NVIDIA A100) atop AMD Milan CPU

.. toctree::
    :maxdepth: 1
    :caption: Alpine Table of Contents 

    quick-start
    alpine-hardware
    examples
    software
    moving-from-summit
    important-notes


Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).
