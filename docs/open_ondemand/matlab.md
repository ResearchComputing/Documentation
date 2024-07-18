# MATLAB

1. To start an interactive MATLAB session, select either `MATLAB (Custom)` or `MATLAB (Presets)` from the interactive applications menu. When starting a `MATLAB (Custom)` session, you may customize resources allocated to the session and other characteristics of the dispatched Slurm job. For more information on these options, please see the [Running Custom Interactive applications](./index.md#running-custom-interactive-applications) section. If you select `MATLAB (Presets)`, you may select from standard configurations we provide.

  ![](OnDemand/matlab_custom.png)

2. Once either option is selected, click “Launch” to submit the MATLAB job to the queue. The wait time depends on user provided options, such as the number of cores and time requested.
3. When your Matlab session is ready, you can click the “Launch MATLAB (Custom)” or "Launch MATLAB (Presets)" button to bring up a web page with the MATLAB session. In most cases, the default compression and image quality will suffice. If you do have problems with image quality of the MATLAB session, you can adjust as necessary.

  ![](OnDemand/matlab_custom_launch.png)

4. Once launched, it may take a few minutes for MATLAB to begin. However, once started, you should be able to interact with MATLAB as you would on your own computer.  

## Notes
* <mark style="background-color: #FFF36D">
  GPU based options are not meant for computationally intensive workflows. Additionally,
  please keep in mind that these GPU based options are a shared
  resource amongst all users. Thus, significant computation by one
  user can affect other users of this service.
  </mark>
* Closing the window will not terminate the job, you can use the “My Interactive Sessions” tab to view all open interactive sessions and terminate them.
