# Alpine Software

## Software Installed on Alpine

This list includes the software applications, compilers, libaries, and software development kits (SDKs) installed as modules on CURC Alpine. 

Refer to our [Modules System](https://curc.readthedocs.io/en/latest/compute/modules.html) page for instructions on how to view and load software.
 
| Application | Version(s) | Description |
| ----------- | ---------- | ----------- |
| [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/) (L) | V6R2019x | Abaqus FEA is a software suite for finite element analysis and computer-aided engineering.|  
| [Allinea DDT](https://developer.nvidia.com/allinea-ddt) | 6.0.4 | Graphical debugging tool for single-process, OpenMP, and MPI applications.| 
| [Anaconda](https://www.anaconda.com/products/distribution) | 2020.11, 2022.10 (D) | Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/python.html)|




**(D)** Default module version **(G)** GPU-accelerated **(L)** License-restricted

**Last updated:** January 28, 2023

## Alpine Software Policy 

Historically, software installations have been a sticking point for many users or CURC resources. Though we still encourage users to 
install and manage their own packages locally, CURC has decided to move forward with the following software policy:

CURC will perform software installations for users of CURC resources in a globally accessible module stack provided:

- A user requires a specified software that is unavailable on the current stack.
- A user requires a different version of a currently existing software which provides additional functionality required for the user’s work.
- The user provides all of the relevant information including release, version, etc. 
- The installation will not violate the software’s User Agreement policy.
- The installation is not better suited for a local install (I.E. Anaconda Environments, Singularity Containers).

Furthermore, licensed/proprietary software are subject the following requirements:

- The user has access to an appropriate license for cluster usage.
- The license can be installed or accessed on the cluster. 

Software accepted for installation will be given an estimated installation time based on capacity of the team and urgency of the request. Note that this time is an estimation and not a strict deadline. Installed software will be available to load with a module in the ‘User Software’ category in the software stack. Unused modules will be pruned after 12 months without usage. Any pruned module may be restored by user request.

Core software such as compilers, MPIs, and relevant libraries will be updated at a semesterly interval. A different version of these core softwares can be requested at any point, but installation may be performed in accordance to that timeline.

All software installations are “Best Effort” and are not guaranteed. RC reserves the right to deny any software installation that is requested on CURC resources.

To request a software installation please fill out the [Software Request Form](https://www.colorado.edu/rc/userservices/software-request)

_Please note that this software policy is subject to change. Please review the software policy before submitting a request._


Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
