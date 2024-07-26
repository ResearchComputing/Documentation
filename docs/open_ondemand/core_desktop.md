# Core Desktop (remote desktop)

The **Core Desktop** application provides users a remote desktop session. In this application you will get access to a nice graphical interface that looks like a desktop! Currently, this application is ran on our visualization cluster. This provides users the ability to run on either NVIDIA Tesla K80 or NVIDIA Quadro RTX 8000 GPUs. The **Core Desktop** application is a great place to use interactive applications that you have installed yourself! 

```{eval-rst}
.. figure:: ./OnDemand/core_desktop_preview.png
   :align: center
```

```{attention}
The GPUs provided are not meant for computationally intensive workflows. These GPUs are a shared resource amongst all users running **Core Desktop** sessions. Thus, significant computation by one user can affect other users of this service.
```

## Launching a Core Desktop session

1. Navigate to either the __Interactive Apps__ or __My Interactive Sessions__ tab and select **"Core Desktop"**. 

2. Select your preferred configuration option and then click **“Launch”** to submit the remote desktop job to the queue. The wait time depends on the number of other users presently on the resource. Requesting smaller and shorter jobs may facilitate shorter wait times. 

3. When your remote desktop is ready, you can click the **"Launch Core Desktop"** button to bring up a web page with the remote desktop. In most cases, the default compression and image quality will suffice. If you do have problems with image quality, you can adjust these settings as necessary. 

```{eval-rst}
.. figure:: ./OnDemand/core_desktop_launch.png
   :align: center
   :scale: 50%
```

4. With the remote desktop session running and open, you should be able to run standard Linux desktop applications that have a graphical user interface! 

````{note}
* You can copy/paste into/out of the desktop using the clipboard in the "hidden" tab on the left-hand-side of the desktop.
```{eval-rst}
.. figure:: ./OnDemand/core_desktop_copy_paste.png
   :align: center
   :scale: 50%
```
* Closing the window will not terminate the job. You can use the **“My Interactive Sessions”** tab to view all open interactive sessions and terminate them.
````