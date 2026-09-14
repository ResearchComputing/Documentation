# Open OnDemand _(Browser Based HPC Portal)_

Open OnDemand is a browser based, integrated, single access point for all of your High-Performance Computing (HPC) resources at CU Research Computing. Open OnDemand provides a graphical interface to manage files; create and view job Slurm jobs on CURC's clusters; and access interactive applications (such as Jupyter and RStudio). All of these actions are completed via a web browser and require only minimal knowledge of Linux and scheduler commands.

## Getting started with Open OnDemand

(tabset-ref-ood-gs)=
`````{tab-set}
:sync-group: tabset-ood-gs

````{tab-item} CU Boulder
:sync: ood-gs-ucb

To connect to Open OnDemand, you must first have a CU Research Computing account. If you do not have an account, please consult [our account request page](../getting_started/logging-in.md) to get started. Once you have a CU Research Computing account you can connect to Open OnDemand by visiting <https://ondemand.rc.colorado.edu>. This link will bring you to a login page for Open OnDemand. Use your CU Research Computing credentials and [Microsoft multi-factor authentication (MFA)](https://oit.colorado.edu/services/identity-access-management/microsoft-multi-factor-authentication) to login. No additional MFA setup is required if you are already enrolled in Microsoft MFA.

```{image} ./OnDemand/login_page.png
:alt: University of Colorado Boulder Federated Identity Service login page for ondemand.rc.colorado.edu with text fields for "IdentiKey Username" and "IdentiKey Password." "Log In" and "Advanced Settings..." buttons are below the password field.
:align: center
```

````

````{tab-item} CSU
:sync: ood-gs-csu


To connect to Open OnDemand, you must first have a CU Research Computing account. If you do not have an account, please consult our [getting a CURC account for CSU users](../getting_started/logging-in.html?tabset-logging-in=logging-in-csu#tabset-ref-get-account){.external} documentation. Once you have obtained an account, you can connect to Open OnDemand by visiting <https://ondemand-rmacc.rc.colorado.edu>. This will bring you to a CILogon page. Once on this page, click the drop-down menu under **"Select an Identity Provider"** and select **"Colorado State University"**. 
```{image} ./OnDemand/csu_select_identity.png
:alt: Identity provider selection page with Colorado State University selected and a Log On button.
:align: center
```
This will bring you to a login prompt where you should use your CSU NetID and Duo 2-factor authentication to login. 
```{image} ./OnDemand/csu_ood_login.png
:alt: Colorado State University and CSU Pueblo CILogon page with NetID and password fields and a Login button.
:align: center
```

````

````{tab-item} AMC
:sync: ood-gs-amc

To connect to Open OnDemand, you must first have a CU Research Computing account. If you do not have an account, please consult our [getting a CURC account for AMC users](../getting_started/logging-in.html?tabset-logging-in=logging-in-amc#tabset-ref-get-account){.external} documentation. Once you have obtained an account, you can connect to Open OnDemand by visiting <https://ondemand-rmacc.rc.colorado.edu>. This will bring you to a CILogon page. Once on this page, click the drop-down menu under **"Select an Identity Provider"** and select **"ACCESS CI (XSEDE)"**. 

```{image} ./OnDemand/access_select_identity.png
:alt: Identity provider selection page with ACCESS CI (XSEDE) selected and a Log On button.
:align: center
```

This will bring you to a login prompt where you should use your XSEDE/ACCESS account information and Duo 2-factor authentication to login. 

```{image} ./OnDemand/access_ood_login.png
:alt: ACCESS login page with ACCESS ID and password fields and a Login button.
:align: center
```

````

````{tab-item} RMACC
:sync: ood-gs-rmacc

To connect to Open OnDemand, you must first have a CU Research Computing account. For more information on creating a CU Research Computing account, please see our [getting a CURC account for RMACC users](../getting_started/logging-in.html?tabset-logging-in=logging-in-rmacc#tabset-ref-get-account){.external} documentation. Once you have obtained an account, you can connect to Open OnDemand by visiting <https://ondemand-rmacc.rc.colorado.edu>. This will bring you to a CILogon page. Once on this page, click the drop-down menu under **"Select an Identity Provider"** and select **"ACCESS CI (XSEDE)"**. 
```{image} ./OnDemand/access_select_identity.png
:alt: Identity provider selection page with ACCESS CI (XSEDE) selected and a Log On button.
:align: center
```
This will bring you to a login prompt where you should use your XSEDE/ACCESS account information and Duo 2-factor authentication to login. 
```{image} ./OnDemand/access_ood_login.png
:alt: ACCESS login page with ACCESS ID and password fields and a Login button.
:align: center
```

````
`````

````{important}
_**When logging out**_ you must **completely quit your browser in order for "logout" to occur**. If after reopening your browser you are still logged in, please clear your cookies. If you are on a Chromebook or Chromebox, you will need to reboot your device in order to "quit the browser" and thus "logout".  
```{tip}
Using a **"private browsing mode"** window while using OnDemand is a great way to handle "auto-logout", as closing your browser window will remove all associated cookies and session information. 
```
````

## Overview of Open OnDemand's graphical interface 

When you have successfully logged into Open OnDemand, you will see the landing page with the following features broken into tabs along the top of the page: __Files__, __Jobs__, __Clusters__ (shell access), __Interactive Apps__, and __My Interactive Sessions__. These tabs are your main gateway to the amazing features Open OnDemand has available! For more information on these features, please see the section [What should I read next?](#what-should-i-read-next) at the bottom of this page. 
```{image} ./OnDemand/landing_page.png
:alt: University of Colorado Boulder Research Computing OnDemand homepage with navigation tabs at the top-left for Files, Jobs, Clusters (shell access), Interactive Apps, and My Interactive Sessions. At the top-right of the page a Help button, name of the currently logged-in user, and Log Out button are shown.
:align: center
```

All interactive applications can be accessed via the **"Interactive Apps"** drop-down menu (pictured left). This drop-down menu is meant as a convenience feature to get you quick access to your interactive applications. Although this is nice, sometimes you need to see more information about your interactive applications, such as currently running sessions, sessions waiting in the queue, and sessions that have completed. To obtain this information you can use select the **"My Interactive Sessions"** tab (pictured right).
```{image} ./OnDemand/interactive_access.png
:alt: Interactive Apps drop-down menu and My Interactive Sessions page showing queued and running sessions. The drop-down menu contains options for Core Desktop, MATLAB, Jupyter Session, RStudio Server, and VS Code-Server. The My Interactive sessions page shows one queued and one running job, each with a name, job ID, creation time, and Session ID, as well as a button on the right to delete each job. Additionally, the queued job shows time requested and the following text: "Please be patient as your job currently sits in queue. The wait time depends on the number of cores as well as time requested." The running job, on the other hand, shows a hostname of "c3cpu-a5-u1-3.rc.int.colorado.edu", time remaining, and the number of nodes and cores available. The button "Connect to Jupyter" is visible below the running job.
:align: center
```

---

## What should I read next? 

```{toctree}
:maxdepth: 1

configuring_apps
core_desktop
matlab
jupyter_session
rstudio
vs_code-server
files_app
jobs_app
terminal_app
llm_chat_interface

```
