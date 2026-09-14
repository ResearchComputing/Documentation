# Core Desktop (remote desktop)

The **Core Desktop** application provides users a remote desktop session. In this application you will get access to a nice graphical interface that looks like a desktop! Currently, this application is ran on our visualization cluster. This provides users the ability to run on either NVIDIA Tesla K80 or NVIDIA Quadro RTX 8000 GPUs. The **Core Desktop** application is a great place to use interactive applications that you have installed yourself! 
```{image} ./OnDemand/core_desktop_preview.png
:alt: A Core Desktop session in Open OnDemand showing a Linux desktop with terminal, file manager, and web browser windows, as examples of the types of applications that can be used in Core Desktop.
:align: center
```

```{attention}
The GPUs provided are not meant for computationally intensive workflows. These GPUs are a shared resource amongst all users running **Core Desktop** sessions. Thus, significant computation by one user can affect other users of this service.
```

## Launching a Core Desktop session

1. Navigate to either the __Interactive Apps__ or __My Interactive Sessions__ tab and select **"Core Desktop"**. 

2. Select your preferred configuration option and then click **“Launch”** to submit the remote desktop job to the queue. For more information on custom configuration options see [Configuring Open OnDemand interactive applications](./configuring_apps.md). The wait time depends on the number of other users presently on the resource. Requesting smaller and shorter jobs may facilitate shorter wait times. 

3. When your remote desktop is ready, you can click the **"Launch Core Desktop"** button to bring up a web page with the remote desktop. In most cases, the default compression and image quality will suffice. If you do have problems with image quality, you can adjust these settings as necessary. 
```{image} ./OnDemand/core_desktop_launch.png
:alt: The Open OnDemand interactive job information interface. The running job, labeled "Core Desktop (26525)", shows a hostname of "viz1.rc.int.colorado.edu", creation time, time remaining, session ID, and the number of nodes and cores available. Sliders for "Compression" and "Image Quality", increasing from zero (lowest) at the left to nine (highest) at the right are below the running job. The button "Launch Core Desktop" is visible in the bottom-left below the sliders. In the bottom right, a "View Only (Share-able Link)" button is visible. A "Delete" button is also visible in the top-right.
:align: center
:scale: 50%
```

4. With the remote desktop session running and open, you should be able to run standard Linux desktop applications that have a graphical user interface! 

````{note}
* You can copy/paste into/out of the desktop using the clipboard in the "hidden" tab on the left-hand-side of the desktop.
```{image} ./OnDemand/core_desktop_copy_paste.png
:alt: noVNC Clipboard panel used to copy and paste text between the local computer and Core Desktop session. It consists of a blank text box labeled "Clipboard", and a "Clear" button in the bottom-right below the text box.
:align: center
:scale: 50%
```
* Closing the window will not terminate the job. You can use the **“My Interactive Sessions”** tab to view all open interactive sessions and terminate them.
````