Alpine
===============

On May 18, 2022, CU Research Computing released phase 1 of Alpine, the third generation CURC High Performance 
Computing Cluster. Phase 2 was released in September 2022. The warranty of the Summit cluster's storage ended on 
September 30, 2022. The full sun-setting of the Summit system is yet to be finalized. 

.. image:: ./images/alpine_summit_timeline.png
  :width: 400
  :align: center

  :alt: Summit-Alpine timeline


**Overview:**

Alpine is the University of Colorado Boulder Research Computing’s third-generation high performance computing (HPC) cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado Boulder, Colorado State University, and Anschutz Medical Campus. Alpine currently offers 317 compute nodes and a total of 18,080 cores.

Alpine can be securely accessed anywhere, anytime using OpenOnDemand or ssh connectivity to the CURC system.

**Nodes and Hardware Summary:**

Total Core Count: **18,080**

The Alpine cluster is made up of different types of nodes outlined below:

CPU nodes: 188 AMD Milan Compute nodes (184 nodes with 64 cores/node, 4 nodes with 48 cores/node) with 256 GB RAM
GPU nodes:
8 GPU-enabled (3x AMD MI100) atop AMD Milan CPU
8 GPU-enabled (3x NVIDIA A100) atop AMD Milan CPU
High-memory nodes: 12 AMD Milan nodes with 1TB of memory
Alpine also includes nodes contributed by partner institutions. Contributors with nodes in either deployment or production are:

Colorado State University: 77 AMD Milan compute nodes (28 nodes with 48 cores/node, 49 nodes with 32 cores/node)
CU Anschutz Medical Campus: 16 AMD Milan compute nodes (64 cores/node), 2 AMD Milan nodes with 1TB of RAM, and 4 GPU-enabled (3x NVIDIA A100 atop AMD Milan)

All nodes are available to all users. For full details about node access, please refer to the Alpine Node Access and FairShare policy.

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
