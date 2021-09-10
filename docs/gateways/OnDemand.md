## CU OnDemand _(Browser Based Access for all of your HPC resources)_

CU OnDemand is a browser based, integrated, single access point for all of your HPC resources. CU OnDemand provides a graphical interface to view, edit, download, and upload files, manage and create job templates, and access CURC interactive applications (Viz cluster, Matlab, and JupyterNotebooks), all via a web browser and with minimal knowledge of Linux and scheduler commands.

### Getting started with OnDemand

> **_NOTE:_** _OnDemand is in beta and is currenly only available to CU users_
 
To connect to CU OnDemand, visit https://ondemand.rc.colorado.edu/. The first page of CU OnDemand will bring you to a login prompt. Use your CU Research Computing credentials to login and 2-factor authenticate using Duo. If you need a CU Research Computing account please visit https://curc.readthedocs.io/en/latest/access/logging-in.html to get started.

Once you successfully login you will land on the welcome page.

### Features

#### File Menu

The File menu allows users to view and operate on files in three different file spaces: the user’s home directory, project directory, and if applicable shared PetaLibary directories.

Selecting one of the file spaces will open a separate browser window which will allow you to navigate the space in a graphical setting similar to a file browser on personal computers. From here users can download, upload, create, delete, and open files.

> **_NOTE 1:_** _Use Globus to transfer files to /scratch/summit or /rc_scratch._

> **_NOTE 2:_** _If you have more than 1 GB of data to transfer, please use Globus._

For additional detail: OSC's File Transfer and Management help page provides details on its use.

#### Jobs Menu

Jobs can be monitored, created, edited and scheduled with the job management tools under the “Jobs” menu.

Active Jobs: Under the “Active Jobs” tab you can view active jobs. You can choose to view your jobs (or all jobs) as well as choose from specific clusters (Blanca, Summit, Viz-Core, or all Custers). From this menu you can cancel your own jobs.

Job Composer: Create and edit job scripts and schedule jobs under this menu.  OSC's File Transfer and Management help page provides details on its use.

#### Shell Access

The Clusters tab provides shell access to login nodes on CURC clusters. The shell terminal is similar to many other tools that provide terminal access.

Summit: The Summit tab will launch a terminal that RC users can use to manually access an RC Login node. After the tab opens, type your CURC password and accept the Duo push to your phone to complete login to the terminal.

Blanca: The Blanca tab will launch a terminal that RC users can use to manually access an RC Login node. After the tab opens, type your CURC password and accept the Duo push to your phone to complete login to the terminal. To load the Blanca Slurm environment, make sure to type “module load slurm/blanca upon login. More information on using the Blanca cluster can be found here.

#### Interactive Applications
