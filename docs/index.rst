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

Instructors who wish to lead a class using RC resources must contact us at rc-help@colorado.edu before the class begins.  This is to ensure that our resources can meet your needs and if adequate resources and support are available.
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

- DOI: https://doi.org/10.25811/k3w6-pk81 
- Citation: University of Colorado Boulder Research Computing. (2023). Alpine. University of Colorado Boulder. https://doi.org/10.25811/k3w6-pk81

**Acknowledging Cumulus:**
"This work utilized the CUmulus on-premise cloud service at the University of Colorado Boulder. CUmulus is jointly funded by the National Science Foundation (award OAC-1925766) and the University of Colorado Boulder."

**Acknowledging Summit:**
"This work utilized the Summit supercomputer, which is supported by the National Science Foundation (awards ACI-1532235 and ACI-1532236), the University of Colorado Boulder, and Colorado State University. The Summit supercomputer is a joint effort of the University of Colorado Boulder and Colorado State University."

- DOI: https://doi.org/10.25811/8np0-je59
- Citation: University of Colorado Boulder Research Computing. (2021). RMACC Summit Supercomputer. University of Colorado Boulder. https://doi.org/10.25811/8np0-je59

**Acknowledging Blanca:**
"This work utilized the Blanca condo computing resource at the University of Colorado Boulder. Blanca is jointly funded by computing users and the University of Colorado Boulder."

- DOI: https://doi.org/10.25811/v32c-gy42
- Citation: University of Colorado Boulder Research Computing. (2021). Blanca Condo Cluster. University of Colorado Boulder. https://doi.org/10.25811/v32c-gy42

**Acknowledging PetaLibrary:**
"Data storage supported by the University of Colorado Boulder 'PetaLibrary'"

- DOI: https://doi.org/10.25811/81nc-wv41
- Citation: University of Colorado Boulder Research Computing. (2021). PetaLibrary. University of Colorado Boulder. https://doi.org/10.25811/81nc-wv41

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
   access/amc-access

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

.. toctree::
   :maxdepth: 1
   :caption: Storage

   storage/petalibrary/index
   
.. toctree::
   :maxdepth: 2
   :caption: Gateways & Portals

   gateways/OnDemand
   gateways/jupyterhub
   
.. toctree::
   :maxdepth: 2
   :caption: Cloud

   cloud/aws/index
   cloud/azure/index
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
   software/vasp
   software/Containerizationon
   software/spack

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
   :caption: Tutorials
   
   tutorials/index
   
.. toctree::
   :maxdepth: 2
   :caption: Additional resources

   additional-resources/policies
   additional-resources/CURC-cheatsheet
   additional-resources/registrycilogon-instructions
   additional-resources/utah-videos
   additional-resources/blanca-MOU
   additional-resources/other
   additional-resources/biokem-facility
   additional-resources/csu-xsede-usernames


.. toctree::
   :maxdepth: 2
   :caption: Maintenance

   changelogs/CHANGELOG

