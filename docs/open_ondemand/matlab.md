# MATLAB GUI

The **MATLAB** application provides users with a MATLAB graphical user interface (GUI). This GUI can often be helpful when prototyping code. The **MATLAB** application is configured such that a **Core Desktop** session is started and then MATLAB is launched. Due to this reason, all the functionalities and limitations of the **Core Desktop** application also apply. For more information on the **Core Desktop** application, see our documentation [Core Desktop (remote desktop)](./core_desktop.md). 

```{eval-rst}
.. figure:: ./OnDemand/matlab_gui_app.png
   :align: center
```

```{attention}
The GPUs provided are not meant for computationally intensive workflows. These GPUs are a shared resource amongst all users running **MATLAB** sessions. Thus, significant computation by one user can affect other users of this service. For computationally intensive workflows, please use Alpine or Blanca resources according to our [MATLAB](../software/matlab.md) documentation. 
```

## Launching a MATLAB GUI session

1. Navigate to either the __Interactive Apps__ or __My Interactive Sessions__ tab and select **"MATLAB"**. 

2. Select your preferred configuration option and then click **“Launch”** to submit the MATLAB job to the queue. The wait time depends on the number of other users presently on the resource. Requesting smaller and shorter jobs may facilitate shorter wait times. 

3. When your MATLAB session is ready, you can click the **"Launch MATLAB"** button to bring up a web page with the MATLAB GUI. In most cases, the default compression and image quality will suffice. If you do have problems with image quality, you can adjust these settings as necessary. 

```{eval-rst}
.. figure:: ./OnDemand/matlab_gui_launch.png
   :align: center
   :scale: 50%
```

4. Once launched, it may take a few minutes for MATLAB to begin. However, once started, you should be able to interact with MATLAB as you would on your own computer.  

````{note}
* Currently, the MATLAB software is installed locally on the resources. This restricts users to the provided versions, if you want to launch MATLAB via this application. Alternatively, you may also start up a [Core Desktop](./core_desktop.md) session and launch MATLAB from the command line. This is often useful if you would like to utilize a different version of MATLAB. 

* You can copy/paste into/out of the desktop using the clipboard in the "hidden" tab on the left-hand-side of the screen.
```{eval-rst}
.. figure:: ./OnDemand/core_desktop_copy_paste.png
   :align: center
   :scale: 50%
```

* Closing the window will not terminate the job. You can use the **“My Interactive Sessions”** tab to view all open interactive sessions and terminate them.
````
 
