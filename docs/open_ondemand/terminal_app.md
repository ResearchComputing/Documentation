# Terminal application

Individuals who are comfortable with the Linux command line may be interested in accessing a terminal. Through this terminal, individuals can navigate the filesystem, start interactive jobs, submit batch jobs, perform software installs, and much more. To access a terminal in Open OnDemand, select the **Clusters** tab and then select **Alpine Shell Access** (pictured left). Once selected, a new window will open and place the user in a terminal (pictured right) on a **login node** with the Slurm Alpine module loaded. 

```{eval-rst}
.. figure:: ./OnDemand/cluster_terminal_app.png
   :align: center
```


````{important}

- As stated above, the user will be placed on a login node, login nodes are not meant for running code. If you would like to run code, please use a compute node. For more information on different node types, please see our [node types](../compute/node-types.md) documentation. 

- By default, the module `slurm/alpine` will be loaded (allowing you to submit jobs to Alpine). If you would like to submit a job to Blanca, please load the Blanca module: 
    ```
    module load slurm/blanca
    ```

- If prompted for a password, type your password and accept the Duo push sent to your phone.

````