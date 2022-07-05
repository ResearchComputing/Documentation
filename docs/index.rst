Research Computing User Guide
=============================

Documentation covering the use of Research Computing resources.

Here are some quick links into the documentation to get you started.

* :doc:`Logging In <access/logging-in>`
* :doc:`Research Computing Filesystems <compute/filesystems>`
* :doc:`Compiling Software <compute/compiling>`
* :doc:`Batch Jobs <running-jobs/batch-jobs>`
* :doc:`The Module System <compute/modules>`
* :doc:`Frequently Asked Questions (FAQ) <faq>`

`Can't find what you need? Provide feedback on the CURC docs! <https://forms.gle/bSQEeFrdvyeQWPtW9>`_

More information is available at https://www.colorado.edu/rc.

If you have any questions, please contact rc-help@colorado.edu.

Courses using RC Resources
--------------------------

Students are welcome to use RC resources on their own for class projects and can request access as a regular UCB affiliate via the link off the RC homepage at: https://www.colorado.edu/rc.  When requesting help please indicate that the work is for a class project and any deadlines.  
If students are to be required to use RC resources for a class, see below.

Instructors who wish to lead a class using RC resources must contact us at rc-help@colorado.edu before the class begins.  This is to insure that our resources can meet your needs and if adequate resources and support are available.
Early in the process we will need to know details about the proposed class usage such as:  

- Number of students  
- Software needed, and if it will be installed by instructor/TA  
- Typical computational work (number of jobs or sessions, length, number of CPUs)  
- Date if 1st usage in class/lab  
- Class roster including TAs and auditors.  
Acknowledging RC
----------------

Use of University of Colorado Research Computing resources, including (but not limited to) the Janus, Summit, and Alpine supercomputers, the Blanca Condo Cluster, and the PetaLibrary data storage service must be acknowledged in any and all publications.

**Acknowledging Alpine:**
“This work utilized the Alpine high performance computing resource at the University of Colorado Boulder. Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).”

**Acknowledging Cumulus:**
"This work utilized the CUmulus on-premise cloud service at the University of Colorado Boulder. CUmulus is jointly funded by the National Science Foundation (award OAC-1925766) and the University of Colorado Boulder."

**Acknowledging Summit:**
"This work utilized the Summit supercomputer, which is supported by the National Science Foundation (awards ACI-1532235 and ACI-1532236), the University of Colorado Boulder, and Colorado State University. The Summit supercomputer is a joint effort of the University of Colorado Boulder and Colorado State University."

**Acknowledging Blanca:**
"This work utilized the Blanca condo computing resource at the University of Colorado Boulder. Blanca is jointly funded by computing users and the University of Colorado Boulder."

**Acknowledging PetaLibrary:**
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
   access/allocations
   access/rmacc

.. toctree::
   :maxdepth: 2
   :caption: The Compute Environment

   compute/node-types
   compute/filesystems
   compute/modules
   compute/data-transfer
   compute/compiling
   compute/monitoring-resources

.. toctree::
   :maxdepth: 2
   :caption: Clusters

   clusters/alpine/index
   clusters/blanca/blanca 
   clusters/summit/summit

.. toctree::
   :maxdepth: 2
   :caption: Running Jobs

   running-jobs/running-apps-with-jobs
   running-jobs/batch-jobs
   running-jobs/interactive-jobs
   running-jobs/slurm-commands
   running-jobs/job-resources
   running-jobs/squeue-status-codes
   running-jobs/ssky

.. toctree::
   :maxdepth: 1
   :caption: Storage

   storage/petalibrary/index
   
.. toctree::
   :maxdepth: 2
   :caption: Gateways & Portals

   gateways/OnDemand
   gateways/jupyterhub
   gateways/enginframe

.. toctree::
   :maxdepth: 2
   :caption: Cloud

   cloud/aws/index
   cloud/cumulus
   cloud/project-management
   cloud/instance-creation
   cloud/slurm-integration

.. toctree::
   :maxdepth: 2
   :caption: Software

   software/loadbalancer
   software/gaussian
   software/matlab
   software/python
   software/GNUParallel
   software/ContainerizationonSummit

.. toctree::
   :maxdepth: 2
   :caption: Programming and Parallelization
   
   programming/coding-best-practices
   programming/parallel-programming-fundamentals
   programming/MPIBestpractices
   programming/MPI-C
   programming/MPI-Fortran
   programming/OpenMP-C
   programming/OpenMP-Fortran

.. toctree::
   :maxdepth: 2
   :caption: Additional resources

   additional-resources/CURC-cheatsheet
   additional-resources/utah-videos
   additional-resources/blanca-MOU
   additional-resources/other
   additional-resources/biokem-facility
   additional-resources/csu-xsede-usernames

.. toctree::
   :maxdepth: 2
   :caption: Maintenance

   changelogs/CHANGELOG

