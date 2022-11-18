Alpine
===============

On May 18, 2022, CU Research Computing released phase 1 of Alpine, the third generation CURC High Performance 
Computing Cluster. Phase 2 was released in September 2022. The warranty of the Summit cluster's storage will end 
September 30, 2022 with the full sun-setting of the Summit system yet to be finalized. 

.. image:: ./images/alpine_summit_timeline.png
  :width: 400
  :align: center

  :alt: Summit-Alpine timeline


**Overview:**

Alpine is the University of Colorado Boulder Research Computing's third-generation high performance computing (HPC) 
cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado 
Boulder. Additional contributions provided from Colorado State University and Anschutz Medical Campus are planned for the 
near future. Alpine currently offers 204 compute nodes and a total of 12,992 cores.

Alpine can be securely accessed anywhere, anytime using OpenOnDemand or ssh connectivity to the CURC system.

**Hardware Summary:**

Total Core Count: **12,992**

Nodes: The Alpine cluster is made up of different types of nodes outlined below.

* **CPU nodes:**
 * 188 AMD Milan EPYC Compute nodes (184 nodes with 64 cores/node; 4 nodes with 48 cores/node)

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
    allocations
    moving-from-summit
    important-notes
    condo-fairshare-and-resource-access.md

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).
