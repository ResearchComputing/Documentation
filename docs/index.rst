Research Computing User Guide
=============================

Documentation covering the use of Research Computing resources.

Here are some quick links into the documentation to get you started.

* :doc:`Logging In <access/login>`
* :doc:`Research Computing Filesystems <compute/filesystems>`
* :doc:`Compiling Software <compute/compiling>`
* :doc:`Batch Jobs <running-jobs/batch-jobs>`
* :doc:`The Module System <compute/modules>`
* :doc:`Frequently Asked Questions (FAQ) <faq>`

More information is available at https://www.colorado.edu/rc.

If you have any questions, please contact rc-help@colorado.edu.

----

Acknowledging RC
================

Use of University of Colorado Research Computing resources, including (but not limited to) the Janus and Summit supercomputers, the Blanca Condo Cluster, and the PetaLibrary data storage service must be acknowledged in any and all publications.

Acknowledging Summit:
"This work utilized the Summit supercomputer, which is supported by the National Science Foundation (awards ACI-1532235 and ACI-1532236), the University of Colorado Boulder, and Colorado State University. The Summit supercomputer is a joint effort of the University of Colorado Boulder and Colorado State University."

Acknowledging PetaLibrary:
"Data storage supported by the University of Colorado Boulder 'PetaLibrary'"

----

.. toctree::
   :maxdepth: 1

   faq

.. toctree::
   :maxdepth: 2
   :caption: Accessing RC Resources

   access/logging-in
   access/duo-2-factor-authentication
   access/rmacc
   access/blanca
   access/allocations

.. toctree::
   :maxdepth: 2
   :caption: The Compute Environment

   compute/node-types
   compute/filesystems
   compute/modules
   compute/data-transfer
   compute/compiling
   compute/petalibrary

.. toctree::
   :maxdepth: 2
   :caption: Running Jobs

   running-jobs/running-apps-with-jobs
   running-jobs/batch-jobs
   running-jobs/interactive-jobs
   running-jobs/slurm-commands
   running-jobs/job-resources
   running-jobs/squeue-status-codes
   running-jobs/roce-enabled

.. toctree::
   :maxdepth: 2
   :caption: Gateways

   gateways/jupyterhub
   gateways/parallel-programming-jupyter
   gateways/enginframe

.. toctree::
   :maxdepth: 2
   :caption: Software

   software/loadbalancer
   software/gaussian
   software/matlab

.. toctree::
   :maxdepth: 2
   :caption: Programming and Parallelization
   
   programming/coding-best-practices
   programming/parallel-programming-fundamentals
   programming/MPI-C
   programming/MPI-Fortran
   programming/OpenMP-C
   programming/OpenMP-Fortran

.. toctree::
   :maxdepth: 2
   :caption: Additional resources

   additional-resources/utah-videos
   additional-resources/other

.. toctree::
   :maxdepth: 2
   :caption: Maintenance

   maintenance/CHANGELOG
