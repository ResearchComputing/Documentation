# Profiling NVIDIA GPU Performance

The NVIDIA Performance Counters provide low-level metrics on GPU usage, enabling users to understand how efficiently their code uses the GPU. This is especially important for optimizing workloads on Alpine’s A100 GPU nodes, where GPU time is a valuable and shared resource.

The following tools are available for interacting with performance counters:

- `nvidia-smi`: For basic monitoring of GPU resource usage.

- `Nsight Compute (ncu)`: For detailed GPU kernel performance analysis.

- `Nsight Systems (nsys)`: For system-wide GPU and CPU performance tracing.

## Sample CUDA Code: Vector Addition
This code example will be used throughout this guide to demonstrate how to use each NVIDIA profiling and monitoring tool.

Here’s a simple CUDA program `vectorAdd.cu` that adds two vectors of floats.

```
#include <iostream>
#include <cuda_runtime.h>

#define N 1024  // Size of the vectors

__global__ void vectorAdd(float *A, float *B, float *C) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}

int main() {
    float *A = new float[N], *B = new float[N], *C = new float[N];
    for (int i = 0; i < N; i++) {
        A[i] = static_cast<float>(rand()) / RAND_MAX;
        B[i] = static_cast<float>(rand()) / RAND_MAX;
    }

    float *d_A, *d_B, *d_C;
    size_t size = N * sizeof(float);
    cudaMalloc(&d_A, size); cudaMalloc(&d_B, size); cudaMalloc(&d_C, size);
    cudaMemcpy(d_A, A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, size, cudaMemcpyHostToDevice);

    dim3 block(256);
    dim3 grid((N + block.x - 1) / block.x);
    vectorAdd<<<grid, block>>>(d_A, d_B, d_C);
    cudaMemcpy(C, d_C, size, cudaMemcpyDeviceToHost);

    delete[] A; delete[] B; delete[] C;
    cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
    return 0;
}
```

## nvidia-smi

`nvidia-smi` (System Management Interface) is a command-line utility that provides real-time information about GPU utilization, memory usage, temperature, and running processes.

### Getting Started

```
$ nvidia-smi
```
Example output of `nvidia-smi` on the `aa100` partition
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-PCIE-40GB          Off |   00000000:21:00.0 Off |                    0 |
| N/A   33C    P0             40W /  250W |       1MiB /  40960MiB |      2%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0    0    0           110318      C    ./vectorAdd                            34MiB  |
+-----------------------------------------------------------------------------------------+

```

#### Header Information

| Column               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| `NVIDIA-SMI 570.124.06` | The version of the nvidia-smi utility installed  |
| `Driver Version: 570.124.06` | The installed NVIDIA driver version. Any CUDA version used, must be compatible with this driver version. |
| `CUDA Version: 12.8` | The highest version of the CUDA Toolkit supported by the driver. |

#### GPU Hardware Overview

| Column               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| GPU |	The GPU index (starting from 0). In this case, GPU 0 is being shown. |
| Name | Full name of the GPU model. Here, it's NVIDIA A100-PCIE-40GB. |
| Persistence-M	| Shows whether Persistence Mode is enabled (helps reduce driver load time). It is Off here. |
| Bus-Id |	PCIe Bus ID of the GPU. Useful for identifying GPUs in multi-GPU systems. |
| Disp.A | Whether the GPU is attached to a display (usually Off on HPC systems). |
| Volatile Uncorr. ECC |	Reports single-bit error corrections that could indicate hardware instability (shows 0 here, which is good). |

#### Sensor and Resource Usage Metrics

| Metric               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| Fan | GPU fan speed percentage. Often N/A on datacenter GPUs like A100.| 
| Temp	| Current temperature of the GPU in Celsius (e.g., 33C).| 
| Perf	| Performance state of the GPU, ranging from P0 (maximum performance) to P12 (minimum).| 
| Pwr:Usage/Cap	| Current power draw and the maximum power cap of the GPU (40W / 250W).| 
| Memory-Usage	| GPU memory in use vs total available. Only 1 MiB out of 40960 MiB is in use, indicating an idle GPU.| 
| GPU-Util	| Percentage of time over the last few seconds that the GPU was busy. Low values (like 2%) indicate little to no workload.| 
| Compute M. | Compute mode status. Default means any user with permission can use the GPU. Other modes include Exclusive Process and Prohibited.| 
| MIG M. | MIG (Multi-Instance GPU) mode status. Here it is Disabled, meaning the GPU is operating in full-capacity mode, not subdivided.| 

#### Processes Table

| Column               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| GPU | Index of the GPU the process is using. In this case, the GPU being used is GPU 0. | 
| GI/CI	| GPU Instance (GI) / Compute Instance (CI). Used only when MIG mode is enabled. Since MIG mode is disabled here, both values are set to 0. | 
| PID	| Unique Process ID (PID) of the application utilizing the GPU. Example: 110318. | 
| Type	| Type of process using the GPU. Possible values include C (Compute), G (Graphics), etc. In this instance, C indicates a Compute process, meaning the GPU is being used for calculations or data processing. | 
| Process Name	| Name of the executable or command utilizing the GPU. In this case, `./vectorAdd` is the name of the executable. | 
| GPU Memory Usage	| Amount of GPU memory the process is using. This process is using 34 MiB of memory. | 

```{note}
- Run `nvidia-smi` inside your allocated job session (e.g., after using `sinteractive`) to check whether your job is using the GPU.
- If no processes appear in the list but you expect your application to be running, it likely means the GPU is not being utilized. Please verify that your code is GPU-enabled and that CUDA is properly initialized.

```

### nvidia-smi on MIG-Enabled GPUs

Some A100 GPUs on our systems are MIG-enabled (Multi-Instance GPU). On these nodes, `nvidia-smi` shows a different output format, displaying information for both full GPUs and individual MIG instances.

Here's an example output from a MIG-enabled A100 node:
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------|
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-PCIE-40GB          On  |   00000000:21:00.0 Off |                   On |
| N/A   28C    P0             32W /  250W |     213MiB /  40960MiB |     N/A      Default |
|                                         |                        |              Enabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A100-PCIE-40GB          On  |   00000000:81:00.0 Off |                   On |
| N/A   27C    P0             33W /  250W |     213MiB /  40960MiB |     N/A      Default |
|                                         |                        |              Enabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA A100-PCIE-40GB          On  |   00000000:E2:00.0 Off |                   On |
| N/A   28C    P0             34W /  250W |     213MiB /  40960MiB |     N/A      Default |
|                                         |                        |              Enabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| MIG devices:                                                                            |
+------------------+----------------------------------+-----------+-----------------------+
| GPU  GI  CI  MIG |                     Memory-Usage |        Vol|        Shared         |
|      ID  ID  Dev |                       BAR1-Usage | SM     Unc| CE ENC  DEC  OFA  JPG |
|                  |                                  |        ECC|                       |
|==================+==================================+===========+=======================|
|  0    1   0   0  |             107MiB / 20096MiB    | 42      0 |  3   0    2    0    0 |
|                  |                 0MiB / 32767MiB  |           |                       |
+------------------+----------------------------------+-----------+-----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

```
#### What’s Different with MIG?

- **MIG Mode:** You'll see `MIG M.: Enabled` in the main GPU listing.

- **GPU Utilization:** The parent GPU will often show `N/A` for `GPU-Util`; usage is tracked per MIG instance instead.

- **MIG Devices Section:** This shows each available MIG instance, how much memory and compute it has, and its usage stats.

- **Process Table:** When jobs are running, this table will show which process is attached to which MIG slice.

```{note}
When using MIG-enabled GPUs, refer to the MIG devices section for information about individual MIG slices. Do not rely on the main GPU table for MIG-specific details.
```

### Manually Monitoring GPU Usage While a Job is Running

To check performance while your job is active:

1. Submit or start your GPU job

     - You can run your GPU job either interactively (e.g. using `sinteractive`) or via a batch script submitted with `sbatch`

2. Identify the node where your job is running

     - When the job is running, use the squeue command to find which compute node it's on:

      ``` 
      $ squeue -u $USER 
      ```

     - Look for the NODELIST(REASON) column, this shows the name of the compute node assigned to your job (e.g. `c3gpu-c2-u13`).

3. ```ssh``` into the compute node

     - Once you have the node name, `ssh` into it directly. For example, if your GPU job was running on `c3gpu-c2-u13`, you would do the following:

      ```
      $ ssh c3gpu-c2-u13
      ```

      ```{note} 
      You can only `ssh` into a compute node if you have an active job running on it. 
      ```

4. Run `nvidia-smi` 

    - Once logged into the node, you can use the `nvidia-smi` command to monitor GPU usage. 
    - You can alternatively use:
    ```
    $ nvidia-smi -l 2
    ```
   where `-l 2` is a flag that will refresh the output every 2 seconds. You can change the interval by adjusting the number (`-l 5` for every 5 seconds). Press `Ctrl+C` to stop the loop.

### Monitoring GPU Usage within a Job Script

To actively monitor GPU performance within a job script, you can run `nvidia-smi` as a background process and redirect its output. Below we provide an example script that redirects the `nvidia-smi` output to the output file `gpu_usage-jobid-${SLURM_JOB_ID}.log` every 60 seconds, where `${SLURM_JOB_ID}` is an environment variable specifying the Job ID. 

```
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --gres=gpu
#SBATCH --partition=atesting_a100 
#SBATCH --qos=testing
#SBATCH --time=00:10:00

# Start GPU monitoring in the background
nvidia-smi -l 60 >> gpu_usage-jobid-${SLURM_JOB_ID}.log &
MONITOR_PID=$!

# Replace the sleep command with your own command e.g. "python my_script.py"
# Here we just sleep for 100 seconds
sleep 100

# Stop monitoring after job finishes
kill $MONITOR_PID
```


## Nsight Compute (ncu)

NVIDIA Nsight Compute is a command-line CUDA kernel profiler that provides detailed performance metrics for GPU kernels, helping users identify, and resolve bottlenecks in CUDA applications. It is particularly well-suited for low-level kernel analysis and optimization.

### Why These Metrics Matter?

Modern GPUs, such as the NVIDIA A100, have hundreds of compute units (Streaming Multiprocessors or SMs). To fully exploit this parallel architecture, your kernel must be configured to launch enough threads and blocks to keep these units busy.

Key Features:

- Collects performance data on SM utilization, memory throughput, warp execution efficiency, and more.

- Offers optimization guidance via diagnostic messages.

- Enables deep inspection of stalls, occupancy, and instruction efficiency.

```{caution}
Collecting performance data using `ncu` can incur significant runtime overhead. For production runs, disable profiling. See [Nsight Compute Overhead](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#overhead) for more details.
```

### Getting Started

To use `ncu`, first load the appropriate CUDA module:

```
$ module load cuda
```
Compile the CUDA code (`vectorAdd.cu`), provided in [Sample CUDA Code: Vector Addition](../programming/profiling-nvidia-gpu-performance.md#sample-cuda-code-vector-addition) section, using the `nvcc` compiler:

```
$ nvcc -o vectorAdd vectorAdd.cu
```

Next, to invoke `ncu`, prefix it to your compiled CUDA application:

```
$ ncu --set full --target-processes all ./vectorAdd
```
- `--set full`: Collects a comprehensive set of performance metrics.

- `--target-processes all`: Profiles all child processes (useful for multi-threaded applications).

```{note}
`ncu` is not compatible with MIG-enabled GPUs. Ensure you run `ncu` only on A100 nodes without MIG.
```

::::{dropdown} Click here to view the full `ncu` report
:icon: note
```
==PROF== Connected to process 3921697 
==PROF== Profiling "vectorAdd" - 0: 0%....50%....100% - 49 passes
==PROF== Disconnected from process 3921697
[3921697] vectorAdd@127.0.0.1
  vectorAdd(float *, float *, float *) (4, 1, 1)x(256, 1, 1), Context 1, Stream 7, Device 0, CC 8.0
    Section: GPU Speed Of Light Throughput
    ----------------------- ----------- ------------
    Metric Name             Metric Unit Metric Value
    ----------------------- ----------- ------------
    DRAM Frequency                  Ghz         1.20
    SM Frequency                    Mhz       756.09
    Elapsed Cycles                cycle        3,726
    Memory Throughput                 %         0.48
    DRAM Throughput                   %         0.14
    Duration                         us         4.93
    L1/TEX Cache Throughput           %        10.77
    L2 Cache Throughput               %         0.48
    SM Active Cycles              cycle        55.69
    Compute (SM) Throughput           %         0.04
    ----------------------- ----------- ------------

    OPT   This kernel grid is too small to fill the available resources on this device, resulting in only 0.0 full
          waves across all SMs. Look at Launch Statistics for more details.

    Section: GPU Speed Of Light Roofline Chart
    INF   The ratio of peak float (fp32) to double (fp64) performance on this device is 2:1. The workload achieved
          close to 0% of this device's fp32 peak performance and 0% of its fp64 peak performance. See the Kernel
          Profiling Guide (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#roofline) for more details
          on roofline analysis.

    Section: PM Sampling
    ------------------------- ----------- ------------
    Metric Name               Metric Unit Metric Value
    ------------------------- ----------- ------------
    Maximum Buffer Size             Kbyte       786.43
    Dropped Samples                sample            0
    Maximum Sampling Interval       cycle       20,000
    # Pass Groups                                    4
    ------------------------- ----------- ------------

    WRN   Sampling interval is 5.4x of the workload duration, which likely results in no or very few collected samples.

    Section: Compute Workload Analysis
    -------------------- ----------- ------------
    Metric Name          Metric Unit Metric Value
    -------------------- ----------- ------------
    Executed Ipc Active   inst/cycle         0.09
    Executed Ipc Elapsed  inst/cycle         0.00
    Issue Slots Busy               %         2.79
    Issued Ipc Active     inst/cycle         0.11
    SM Busy                        %         2.79
    -------------------- ----------- ------------

    OPT   Est. Local Speedup: 98.67%
          All compute pipelines are under-utilized. Either this workload is very small or it doesn't issue enough warps
          per scheduler. Check the Launch Statistics and Scheduler Statistics sections for further details.

    Section: Memory Workload Analysis
    ---------------------------- ----------- ------------
    Metric Name                  Metric Unit Metric Value
    ---------------------------- ----------- ------------
    Memory Throughput                Gbyte/s         2.21
    Mem Busy                               %         0.48
    Max Bandwidth                          %         0.41
    L1/TEX Hit Rate                        %            0
    L2 Compression Success Rate            %            0
    L2 Compression Ratio                                0
    L2 Compression Input Sectors      sector            0
    L2 Hit Rate                            %        86.18
    Mem Pipes Busy                         %         0.03
    ---------------------------- ----------- ------------

    Section: Scheduler Statistics
    ---------------------------- ----------- ------------
    Metric Name                  Metric Unit Metric Value
    ---------------------------- ----------- ------------
    One or More Eligible                   %         2.86
    Issued Warp Per Scheduler                        0.03
    No Eligible                            %        97.14
    Active Warps Per Scheduler          warp         1.98
    Eligible Warps Per Scheduler        warp         0.03
    ---------------------------- ----------- ------------

    OPT   Est. Local Speedup: 97.14%
          Every scheduler is capable of issuing one instruction per cycle, but for this workload each scheduler only
          issues an instruction every 34.9 cycles. This might leave hardware resources underutilized and may lead to
          less optimal performance. Out of the maximum of 16 warps per scheduler, this workload allocates an average
          of 1.98 active warps per scheduler, but only an average of 0.03 warps were eligible per cycle. Eligible
          warps are the subset of active warps that are ready to issue their next instruction. Every cycle with no
          eligible warp results in no instruction being issued and the issue slot remains unused. To increase the
          number of eligible warps, reduce the time the active warps are stalled by inspecting the top stall reasons
          on the Warp State Statistics and Source Counters sections.

    Section: Warp State Statistics
    ---------------------------------------- ----------- ------------
    Metric Name                              Metric Unit Metric Value
    ---------------------------------------- ----------- ------------
    Warp Cycles Per Issued Instruction             cycle        69.32
    Warp Cycles Per Executed Instruction           cycle        90.98
    Avg. Active Threads Per Warp                                   32
    Avg. Not Predicated Off Threads Per Warp                    30.00
    ---------------------------------------- ----------- ------------

    OPT   Est. Speedup: 49.63%
          On average, each warp of this workload spends 34.4 cycles being stalled waiting for an immediate constant
          cache (IMC) miss. A read from constant memory costs one memory read from device memory only on a cache miss;
          otherwise, it just costs one read from the constant cache. Immediate constants are encoded into the SASS
          instruction as 'c[bank][offset]'. Accesses to different addresses by threads within a warp are serialized,
          thus the cost scales linearly with the number of unique addresses read by all threads within a warp. As
          such, the constant cache is best when threads in the same warp access only a few distinct locations. If all
          threads of a warp access the same location, then constant memory can be as fast as a register access. This
          stall type represents about 49.6% of the total average of 69.3 cycles between issuing two instructions.
    ----- --------------------------------------------------------------------------------------------------------------
    OPT   Est. Speedup: 34.4%
          On average, each warp of this workload spends 23.8 cycles being stalled waiting for a scoreboard dependency
          on a L1TEX (local, global, surface, texture) operation. Find the instruction producing the data being waited
          upon to identify the culprit. To reduce the number of cycles waiting on L1TEX data accesses verify the
          memory access patterns are optimal for the target architecture, attempt to increase cache hit rates by
          increasing data locality (coalescing), or by changing the cache configuration. Consider moving frequently
          used data to shared memory. This stall type represents about 34.4% of the total average of 69.3 cycles
          between issuing two instructions.
    ----- --------------------------------------------------------------------------------------------------------------
    INF   Check the Warp Stall Sampling (All Samples) table for the top stall locations in your source based on
          sampling data. The Kernel Profiling Guide
          (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#metrics-reference) provides more details
          on each stall reason.

    Section: Instruction Statistics
    ---------------------------------------- ----------- ------------
    Metric Name                              Metric Unit Metric Value
    ---------------------------------------- ----------- ------------
    Avg. Executed Instructions Per Scheduler        inst         1.19
    Executed Instructions                           inst          512
    Avg. Issued Instructions Per Scheduler          inst         1.56
    Issued Instructions                             inst          672
    ---------------------------------------- ----------- ------------

    OPT   Est. Speedup: 0.665%
          This kernel executes 0 fused and 32 non-fused FP32 instructions. By converting pairs of non-fused
          instructions to their fused (https://docs.nvidia.com/cuda/floating-point/#cuda-and-floating-point),
          higher-throughput equivalent, the achieved FP32 performance could be increased by up to 50% (relative to its
          current performance). Check the Source page to identify where this kernel executes FP32 instructions.

    Section: Launch Statistics
    -------------------------------- --------------- ---------------
    Metric Name                          Metric Unit    Metric Value
    -------------------------------- --------------- ---------------
    Block Size                                                   256
    Function Cache Configuration                     CachePreferNone
    Grid Size                                                      4
    Registers Per Thread             register/thread              16
    Shared Memory Configuration Size           Kbyte           32.77
    Driver Shared Memory Per Block       Kbyte/block            1.02
    Dynamic Shared Memory Per Block       byte/block               0
    Static Shared Memory Per Block        byte/block               0
    # SMs                                         SM             108
    Stack Size                                                 1,024
    Threads                                   thread           1,024
    # TPCs                                                        54
    Enabled TPC IDs                                              all
    Uses Green Context                                             0
    Waves Per SM                                                0.00
    -------------------------------- --------------- ---------------

    OPT   Est. Speedup: 96.3%
          The grid for this launch is configured to execute only 4 blocks, which is less than the GPU's 108
          multiprocessors. This can underutilize some multiprocessors. If you do not intend to execute this kernel
          concurrently with other workloads, consider reducing the block size to have at least one block per
          multiprocessor or increase the size of the grid to fully utilize the available hardware resources. See the
          Hardware Model (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#metrics-hw-model)
          description for more details on launch configurations.

    Section: Occupancy
    ------------------------------- ----------- ------------
    Metric Name                     Metric Unit Metric Value
    ------------------------------- ----------- ------------
    Block Limit SM                        block           32
    Block Limit Registers                 block           16
    Block Limit Shared Mem                block           32
    Block Limit Warps                     block            8
    Theoretical Active Warps per SM        warp           64
    Theoretical Occupancy                     %          100
    Achieved Occupancy                        %        12.48
    Achieved Active Warps Per SM           warp         7.99
    ------------------------------- ----------- ------------

    OPT   Est. Speedup: 87.52%
          The difference between calculated theoretical (100.0%) and measured achieved occupancy (12.5%) can be the
          result of warp scheduling overheads or workload imbalances during the kernel execution. Load imbalances can
          occur between warps within a block as well as across blocks of the same kernel. See the CUDA Best Practices
          Guide (https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) for more details on
          optimizing occupancy.

    Section: GPU and Memory Workload Distribution
    -------------------------- ----------- ------------
    Metric Name                Metric Unit Metric Value
    -------------------------- ----------- ------------
    Average DRAM Active Cycles       cycle         8.50
    Total DRAM Elapsed Cycles        cycle      236,928
    Average L1 Active Cycles         cycle        55.69
    Total L1 Elapsed Cycles          cycle      402,408
    Average L2 Active Cycles         cycle       306.19
    Total L2 Elapsed Cycles          cycle      286,320
    Average SM Active Cycles         cycle        55.69
    Total SM Elapsed Cycles          cycle      402,408
    Average SMSP Active Cycles       cycle        54.32
    Total SMSP Elapsed Cycles        cycle    1,609,632
    -------------------------- ----------- ------------

    OPT   Est. Speedup: 6.458%
          One or more L2 Slices have a much higher number of active cycles than the average number of active cycles.
          Additionally, other L2 Slices have a much lower number of active cycles than the average number of active
          cycles. Maximum instance value is 75.49% above the average, while the minimum instance value is 75.51% below
          the average.

    Section: Source Counters
    ------------------------- ----------- ------------
    Metric Name               Metric Unit Metric Value
    ------------------------- ----------- ------------
    Branch Instructions Ratio           %         0.12
    Branch Instructions              inst           64
    Branch Efficiency                   %            0
    Avg. Divergent Branches                          0
    ------------------------- ----------- ------------

::::

Depending on the nature of the application, some CUDA kernels may be launched multiple times during a run (for example, a kernel called within a loop). For each kernel launch, the name of the kernel function (e.g., vectorAdd in the example above) and the progress of data collection is shown in the standard output (STDOUT). To collect all requested profile information for the many metrics that are included for profiling, you might need to replay the kernels multiple times. When the collection is completed, it will also show the number of replay passes of that kernel. 

```
For example:
==PROF== Profiling "vectorAdd" - 0: 0%....50%....100% - 49 passes
```

When profiling a CUDA application using `ncu`, two sections in the output are very important to pay attention to, GPU Speed Of Light Throughput and Launch Statistics. These sections provide essential insights into how well your code is utilizing the GPU's hardware. Thus, understanding these metrics helps identify performance bottlenecks and underutilization.

### GPU Speed Of Light Throughput

This section tells you how much of the GPU’s peak performance you’re using.
| Metric               | Description                          | What to Look For                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| SM Frequency	| Clock speed of compute cores	| Informational
| Compute (SM) Throughput	| % of max compute power used	| If low (<10%), GPU is underused
| Memory Throughput	| DRAM bandwidth usage	| Very low = memory underutilized
| SM Active Cycles	| Time SMs were actively executing	| Correlates with GPU load

### Launch Statistics
This section tells you how your kernel was launched and whether that configuration is effective.
| Metric               | Description                        | Why It Matters                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| Block Size    | Number of threads per block   | Affects occupancy and granularity of parallelism |
| Grid Size | Number of thread blocks launched  | Determines how many parallel blocks run; too few leads to idle SMs | 
| # SMs | Number of Streaming Multiprocessors (compute units)   | Helps evaluate if enough blocks are used |
| Waves Per SM  | Full sets of warps scheduled per SM   | Indicates how much parallel work is scheduled per compute unit. 0.00 means most SMs are idle | 

Here’s a simplified snippet from an `ncu` run on `vectorAdd` 
```
[rc_user@c3gpu-c2-u7 ]$ ncu --set full --target-processes all ./vectorAdd
==PROF== Connected to process 3921697
==PROF== Profiling "vectorAdd" - 0: 0%....50%....100% - 49 passes
==PROF== Disconnected from process 3921697
[3921697] vectorAdd@127.0.0.1
  vectorAdd(float *, float *, float *) (4, 1, 1)x(256, 1, 1), Context 1, Stream 7, Device 0, CC 8.0
    Section: GPU Speed Of Light Throughput
    ----------------------- ----------- ------------
    Metric Name             Metric Unit Metric Value
    ----------------------- ----------- ------------
    DRAM Frequency                  Ghz         1.20
    SM Frequency                    Mhz       756.09
    Elapsed Cycles                cycle        3,726
    Memory Throughput                 %         0.48
    DRAM Throughput                   %         0.14
    Duration                         us         4.93
    L1/TEX Cache Throughput           %        10.77
    L2 Cache Throughput               %         0.48
    SM Active Cycles              cycle        55.69
    Compute (SM) Throughput           %         0.04
    ----------------------- ----------- ------------

    OPT   This kernel grid is too small to fill the available resources on this device, resulting in only 0.0 full waves across all SMs. Look at Launch Statistics for more details.

    Section: Launch Statistics
    -------------------------------- --------------- ---------------
    Metric Name                          Metric Unit    Metric Value
    -------------------------------- --------------- ---------------
    Block Size                                                   256
    Function Cache Configuration                     CachePreferNone
    Grid Size                                                      4
    Registers Per Thread             register/thread              16
    Shared Memory Configuration Size           Kbyte           32.77
    Driver Shared Memory Per Block       Kbyte/block            1.02
    Dynamic Shared Memory Per Block       byte/block               0
    Static Shared Memory Per Block        byte/block               0
    # SMs                                         SM             108
    Stack Size                                                 1,024
    Threads                                   thread           1,024
    # TPCs                                                        54
    Enabled TPC IDs                                              all
    Uses Green Context                                             0
    Waves Per SM                                                0.00
    -------------------------------- --------------- ---------------

    OPT   Est. Speedup: 96.3%. The grid for this launch is configured to execute only 4 blocks, which is less than the GPU's 108 multiprocessors. This can underutilize some multiprocessors. If you do not intend to execute this kernel concurrently with other workloads, consider reducing the block size to have at least one block per multiprocessor or increase the size of the grid to fully utilize the available hardware resources. See the Hardware Model (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#metrics-hw-model)

```
From the output we can see:

- Block Size (256) × Grid Size (4) = 1024 total threads. This is the total parallel workload for the  kernel.
- 108 SMs: A100 GPU has 108 compute units available.
- Waves Per SM = 0.00: Each SM received less than one full wave of work, which is not enough to keep it busy.
- Compute Throughput = 0.04%: The GPU was virtually idle during the kernel execution.

These numbers clearly show that the kernel is too small to utilize the hardware effectively.

```{tip}

| Symptom               | Likely Cause                          | Recommended Fix                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| Grid size is smaller than #SMs	| Not enough blocks to occupy all compute units	| Increase the number of blocks by enlarging the problem size |
| SM throughput is very low (< 10%)	| GPU is mostly idle	| Optimize workload or parallelism granularity |
| Waves Per SM is 0	| Too little parallel work	| Increase N or restructure the launch configuration |
```

In the original kernel, the launch configuration was:
```
#define N 1024

dim3 block(256);
dim3 grid((N + block.x - 1) / block.x);  // → grid.x = 4 blocks
```
This launches just 4 blocks, causing underutilization.
To improve utilization, update the launch configuration to the following:
```
#define N (1 << 20)  // 1,048,576 elements

dim3 block(256);
dim3 grid((N + block.x - 1) / block.x);  // → grid.x = 4096 blocks
```
This updated configuration allows the GPU to schedule multiple waves of work across all SMs, leading to much better throughput and performance.

::::{dropdown} Click here to view the `ncu` report for the updated configuration
:icon: note
```
==PROF== Connected to process 4073944
==PROF== Profiling "vectorAdd" - 0: 0%....50%....100% - 43 passes
==PROF== Disconnected from process 4073944
[4073944] vect@127.0.0.1
  vectorAdd(float *, float *, float *) (4096, 1, 1)x(256, 1, 1), Context 1, Stream 7, Device 0, CC 8.0
    Section: GPU Speed Of Light Throughput
    ----------------------- ------------- ------------
    Metric Name               Metric Unit Metric Value
    ----------------------- ------------- ------------
    DRAM Frequency          cycle/nsecond         1.48
    SM Frequency            cycle/nsecond         1.01
    Elapsed Cycles                  cycle       10,295
    Memory Throughput                   %        43.61
    DRAM Throughput                     %        43.61
    Duration                      usecond        10.14
    L1/TEX Cache Throughput             %        21.78
    L2 Cache Throughput                 %        59.93
    SM Active Cycles                cycle     7,497.79
    Compute (SM) Throughput             %        12.38
    ----------------------- ------------- ------------

    WRN   This kernel exhibits low compute throughput and memory bandwidth utilization relative to the peak performance
          of this device. Achieved compute throughput and/or memory bandwidth below 60.0% of peak typically indicate
          latency issues. Look at Scheduler Statistics and Warp State Statistics for potential reasons.

    Section: GPU Speed Of Light Roofline Chart
    INF   The ratio of peak float (fp32) to double (fp64) performance on this device is 2:1. The kernel achieved  close
          to 1% of this device's fp32 peak performance and 0% of its fp64 peak performance. See the Kernel Profiling
          Guide (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#roofline) for more details on
          roofline analysis.

    Section: Compute Workload Analysis
    -------------------- ----------- ------------
    Metric Name          Metric Unit Metric Value
    -------------------- ----------- ------------
    Executed Ipc Active   inst/cycle         0.65
    Executed Ipc Elapsed  inst/cycle         0.47
    Issue Slots Busy               %        16.95
    Issued Ipc Active     inst/cycle         0.68
    SM Busy                        %        16.95
    -------------------- ----------- ------------

    WRN   All compute pipelines are under-utilized. Either this kernel is very small or it doesn't issue enough warps
          per scheduler. Check the Launch Statistics and Scheduler Statistics sections for further details.

    Section: Memory Workload Analysis
    --------------------------- ------------ ------------
    Metric Name                  Metric Unit Metric Value
    --------------------------- ------------ ------------
    Memory Throughput           Gbyte/second       826.98
    Mem Busy                               %        30.78
    Max Bandwidth                          %        43.61
    L1/TEX Hit Rate                        %            0
    L2 Compression Success Rate            %            0
    L2 Compression Ratio                                0
    L2 Hit Rate                            %        36.55
    Mem Pipes Busy                         %        11.82
    --------------------------- ------------ ------------

    Section: Scheduler Statistics
    ---------------------------- ----------- ------------
    Metric Name                  Metric Unit Metric Value
    ---------------------------- ----------- ------------
    One or More Eligible                   %        17.03
    Issued Warp Per Scheduler                        0.17
    No Eligible                            %        82.97
    Active Warps Per Scheduler          warp        11.67
    Eligible Warps Per Scheduler        warp         0.31
    ---------------------------- ----------- ------------

    WRN   Every scheduler is capable of issuing one instruction per cycle, but for this kernel each scheduler only
          issues an instruction every 5.9 cycles. This might leave hardware resources underutilized and may lead to
          less optimal performance. Out of the maximum of 16 warps per scheduler, this kernel allocates an average of
          11.67 active warps per scheduler, but only an average of 0.31 warps were eligible per cycle. Eligible warps
          are the subset of active warps that are ready to issue their next instruction. Every cycle with no eligible
          warp results in no instruction being issued and the issue slot remains unused. To increase the number of
          eligible warps, reduce the time the active warps are stalled by inspecting the top stall reasons on the Warp
          State Statistics and Source Counters sections.

    Section: Warp State Statistics
    ---------------------------------------- ----------- ------------
    Metric Name                              Metric Unit Metric Value
    ---------------------------------------- ----------- ------------
    Warp Cycles Per Issued Instruction             cycle        68.53
    Warp Cycles Per Executed Instruction           cycle        71.78
    Avg. Active Threads Per Warp                                   32
    Avg. Not Predicated Off Threads Per Warp                    30.00
    ---------------------------------------- ----------- ------------

    WRN   On average, each warp of this kernel spends 52.5 cycles being stalled waiting for a scoreboard dependency on
          a L1TEX (local, global, surface, texture) operation. Find the instruction producing the data being waited
          upon to identify the culprit. To reduce the number of cycles waiting on L1TEX data accesses verify the
          memory access patterns are optimal for the target architecture, attempt to increase cache hit rates by
          increasing data locality (coalescing), or by changing the cache configuration. Consider moving frequently
          used data to shared memory.. This stall type represents about 76.6% of the total average of 68.5 cycles
          between issuing two instructions.
    ----- --------------------------------------------------------------------------------------------------------------
    INF   Check the Warp Stall Sampling (All Cycles) table for the top stall locations in your source based on sampling
          data. The Kernel Profiling Guide
          (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#metrics-reference) provides more details
          on each stall reason.

    Section: Instruction Statistics
    ---------------------------------------- ----------- ------------
    Metric Name                              Metric Unit Metric Value
    ---------------------------------------- ----------- ------------
    Avg. Executed Instructions Per Scheduler        inst     1,213.63
    Executed Instructions                           inst      524,288
    Avg. Issued Instructions Per Scheduler          inst     1,271.12
    Issued Instructions                             inst      549,123
    ---------------------------------------- ----------- ------------

    WRN   This kernel executes 0 fused and 32768 non-fused FP32 instructions. By converting pairs of non-fused
          instructions to their fused (https://docs.nvidia.com/cuda/floating-point/#cuda-and-floating-point),
          higher-throughput equivalent, the achieved FP32 performance could be increased by up to 50% (relative to its
          current performance). Check the Source page to identify where this kernel executes FP32 instructions.

    Section: Launch Statistics
    -------------------------------- --------------- ---------------
    Metric Name                          Metric Unit    Metric Value
    -------------------------------- --------------- ---------------
    Block Size                                                   256
    Function Cache Configuration                     CachePreferNone
    Grid Size                                                  4,096
    Registers Per Thread             register/thread              16
    Shared Memory Configuration Size           Kbyte           32.77
    Driver Shared Memory Per Block       Kbyte/block            1.02
    Dynamic Shared Memory Per Block       byte/block               0
    Static Shared Memory Per Block        byte/block               0
    Threads                                   thread       1,048,576
    Waves Per SM                                                4.74
    -------------------------------- --------------- ---------------

    WRN   A wave of thread blocks is defined as the maximum number of blocks that can be executed in parallel on the
          target GPU. The number of blocks in a wave depends on the number of multiprocessors and the theoretical
          occupancy of the kernel. This kernel launch results in 4 full waves and a partial wave of 639 thread blocks.
          Under the assumption of a uniform execution duration of all thread blocks, the partial wave may account for
          up to 20.0% of the total kernel runtime with a lower occupancy of 26.5%. Try launching a grid with no
          partial wave. The overall impact of this tail effect also lessens with the number of full waves executed for
          a grid. See the Hardware Model
          (https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#metrics-hw-model) description for more
          details on launch configurations.

    Section: Occupancy
    ------------------------------- ----------- ------------
    Metric Name                     Metric Unit Metric Value
    ------------------------------- ----------- ------------
    Block Limit SM                        block           32
    Block Limit Registers                 block           16
    Block Limit Shared Mem                block           32
    Block Limit Warps                     block            8
    Theoretical Active Warps per SM        warp           64
    Theoretical Occupancy                     %          100
    Achieved Occupancy                        %        73.45
    Achieved Active Warps Per SM           warp        47.01
    ------------------------------- ----------- ------------

    WRN   This kernel's theoretical occupancy is not impacted by any block limit. The difference between calculated
          theoretical (100.0%) and measured achieved occupancy (73.5%) can be the result of warp scheduling overheads
          or workload imbalances during the kernel execution. Load imbalances can occur between warps within a block
          as well as across blocks of the same kernel. See the CUDA Best Practices Guide
          (https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) for more details on
          optimizing occupancy.

    Section: Source Counters
    ------------------------- ----------- ------------
    Metric Name               Metric Unit Metric Value
    ------------------------- ----------- ------------
    Branch Instructions Ratio           %         0.12
    Branch Instructions              inst       65,536
    Branch Efficiency                   %            0
    Avg. Divergent Branches                          0
    ------------------------- ----------- ------------

::::

## Nsight Systems (nsys)

Nsight Systems  is a system-wide profiler that traces the interactions between CPU and GPU, memory transfers, and OS-level activity. It’s useful for understanding:

- Launch latency of GPU kernels.

- Investigate host-device memory transfers.

- Identify CPU-side inefficiencies (e.g., blocking, thread stalls)

### Getting Started

To use `nsys`, first load the appropriate CUDA module. Then compile the CUDA code (`vectorAdd.cu`), available in the [Sample CUDA Code: Vector Addition](../programming/profiling-nvidia-gpu-performance.md#sample-cuda-code-vector-addition) section, using the `nvcc` compiler. Finally, run `nsys` by prefixing it to your compiled application.

```
$ module load cuda
$ nvcc -o vectorAdd vectorAdd.cu
$ nsys profile --trace=cuda,osrt ./vectorAdd
```
- `--trace=cuda`: Capture CUDA kernel launches and memory transfers.

- `--trace=osrt`: Trace OS runtime activity (threads, processes, etc.).

This generates a report file in binary format:
```
./report.nsys-rep
```
To view a quick CLI summary of the captured data:
```
$ nsys stats report.nsys-rep
```

::::{dropdown} Click here to view the full output 
:icon: note
```
Generating SQLite file report.sqlite from report.nsys-rep
Exporting 3120 events: [===================================================100%]

Processing [report.sqlite] with [/curc/sw/cuda/12.1.1/nsight-systems-2023.1.2/host-linux-x64/reports/osrt_sum.py]...

 ** OS Runtime Summary (osrt_sum):

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)     Med (ns)    Min (ns)   Max (ns)    StdDev (ns)            Name
 --------  ---------------  ---------  ------------  -----------  --------  -----------  ------------  ----------------------
     69.6      312,204,830         13  24,015,756.2  9,067,644.0     2,204  195,597,594  53,573,691.5  poll
     28.3      126,874,612        538     235,826.4     60,013.5       381   17,163,639     899,555.3  ioctl
      0.7        3,131,716         34      92,109.3      3,592.0       992    1,132,714     280,648.1  fopen
      0.5        2,302,570         65      35,424.2        411.0       161    1,484,407     206,847.3  fcntl
      0.3        1,383,989         10     138,398.9     19,297.0    10,229      854,150     277,116.1  sem_timedwait
      0.2          973,462         29      33,567.7      6,502.0     5,280      611,632     111,986.5  mmap64
      0.1          586,906          4     146,726.5    127,264.5    70,573      261,804      81,418.8  pthread_create
      0.1          464,767          7      66,395.3      4,860.0       100      437,154     163,564.5  fread
      0.1          267,273         56       4,772.7      3,677.0       661       22,081       3,837.3  open64
      0.0           95,541         13       7,349.3      3,677.0     1,283       32,712       8,725.4  mmap
      0.0           72,785         48       1,516.4         60.0        50       69,741      10,056.9  fgets
      0.0           47,535         28       1,697.7      1,177.0       601        7,244       1,481.4  fclose
      0.0           38,743          7       5,534.7      5,050.0     1,132       10,109       3,475.0  open
      0.0           36,150         12       3,012.5      2,585.0       702        6,853       1,977.1  write
      0.0           16,752          2       8,376.0      8,376.0     2,295       14,457       8,599.8  socket
      0.0           16,611          3       5,537.0      6,943.0     1,924        7,744       3,154.5  pipe2
      0.0           16,554         15       1,103.6        691.0       261        4,038       1,221.6  read
      0.0           11,190          3       3,730.0      3,566.0     3,226        4,398         603.0  munmap
      0.0           11,181          1      11,181.0     11,181.0    11,181       11,181           0.0  connect
      0.0            5,510         64          86.1         50.0        40          461          68.4  pthread_mutex_trylock
      0.0            5,481          2       2,740.5      2,740.5     1,102        4,379       2,317.2  fwrite
      0.0            3,176          2       1,588.0      1,588.0     1,072        2,104         729.7  pthread_cond_broadcast
      0.0            3,148          8         393.5        290.5       191          832         267.2  dup
      0.0            2,244          1       2,244.0      2,244.0     2,244        2,244           0.0  bind
      0.0              751          1         751.0        751.0       751          751           0.0  listen
      0.0              441          6          73.5         50.0        50          181          52.8  fflush

Processing [report.sqlite] with [/curc/sw/cuda/12.1.1/nsight-systems-2023.1.2/host-linux-x64/reports/cuda_api_sum.py]...

 ** CUDA API Summary (cuda_api_sum):

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)     Med (ns)    Min (ns)    Max (ns)    StdDev (ns)            Name
 --------  ---------------  ---------  ------------  -----------  ---------  -----------  ------------  ----------------------
     96.4      139,706,807          3  46,568,935.7      3,817.0      3,035  139,699,955  80,653,828.6  cudaMalloc
      3.5        5,038,894          1   5,038,894.0  5,038,894.0  5,038,894    5,038,894           0.0  cudaLaunchKernel
      0.1          160,483          3      53,494.3      7,274.0      2,966      150,243      83,814.5  cudaFree
      0.0           65,401          3      21,800.3     25,317.0      8,315       31,769      12,116.0  cudaMemcpy
      0.0            1,333          1       1,333.0      1,333.0      1,333        1,333           0.0  cuModuleGetLoadingMode

Processing [report.sqlite] with [/curc/sw/cuda/12.1.1/nsight-systems-2023.1.2/host-linux-x64/reports/cuda_gpu_kern_sum.py]...

 ** CUDA GPU Kernel Summary (cuda_gpu_kern_sum):

 Time (%)  Total Time (ns)  Instances  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)                  Name
 --------  ---------------  ---------  --------  --------  --------  --------  -----------  ------------------------------------
    100.0            2,112          1   2,112.0   2,112.0     2,112     2,112          0.0  vectorAdd(float *, float *, float *)

Processing [report.sqlite] with [/curc/sw/cuda/12.1.1/nsight-systems-2023.1.2/host-linux-x64/reports/cuda_gpu_mem_time_sum.py]...

 ** CUDA GPU MemOps Summary (by Time) (cuda_gpu_mem_time_sum):

 Time (%)  Total Time (ns)  Count  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)      Operation
 --------  ---------------  -----  --------  --------  --------  --------  -----------  ------------------
     52.2            2,656      2   1,328.0   1,328.0     1,216     1,440        158.4  [CUDA memcpy HtoD]
     47.8            2,432      1   2,432.0   2,432.0     2,432     2,432          0.0  [CUDA memcpy DtoH]

Processing [report.sqlite] with [/curc/sw/cuda/12.1.1/nsight-systems-2023.1.2/host-linux-x64/reports/cuda_gpu_mem_size_sum.py]...

 ** CUDA GPU MemOps Summary (by Size) (cuda_gpu_mem_size_sum):

 Total (MB)  Count  Avg (MB)  Med (MB)  Min (MB)  Max (MB)  StdDev (MB)      Operation
 ----------  -----  --------  --------  --------  --------  -----------  ------------------
      0.008      2     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy HtoD]
      0.004      1     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy DtoH]
 
```
::::

### Interpreting Key Outputs

####  CUDA API Summary
Shows how much time was spent in each CUDA API function.

```
 ** CUDA API Summary (cuda_api_sum):

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)     Med (ns)    Min (ns)    Max (ns)    StdDev (ns)            Name
 --------  ---------------  ---------  ------------  -----------  ---------  -----------  ------------  ----------------------
     96.4      139,706,807          3  46,568,935.7      3,817.0      3,035  139,699,955  80,653,828.6  cudaMalloc
      3.5        5,038,894          1   5,038,894.0  5,038,894.0  5,038,894    5,038,894           0.0  cudaLaunchKernel
      0.1          160,483          3      53,494.3      7,274.0      2,966      150,243      83,814.5  cudaFree
      0.0           65,401          3      21,800.3     25,317.0      8,315       31,769      12,116.0  cudaMemcpy
      0.0            1,333          1       1,333.0      1,333.0      1,333        1,333           0.0  cuModuleGetLoadingMode

```
| Function               | 	Time %                          | What It Means                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| `cudaMalloc`	  | 96.4% | 	This indicates that most runtime is spent allocating device memory instead of performing computations. If you're calling `cudaMalloc` inside loops or repeatedly, this adds significant overhead. The solution to this is to allocate once and reuse memory across iterations. |
| `cudaLaunchKernel`	 | 	3.5% | The kernel itself is extremely fast, but that may not be a good thing. A very short kernel runtime often means underutilization of GPU resources. |
| `cudaMemcpy`  | <0.1% | While it didn’t take long, combined with small memory size, this indicates the data being copied is too small to be efficient. |

####  CUDA GPU Kernel Summary
This summarizes execution of GPU kernels.

```
 ** CUDA GPU Kernel Summary (cuda_gpu_kern_sum):

 Time (%)  Total Time (ns)  Instances  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)                  Name
 --------  ---------------  ---------  --------  --------  --------  --------  -----------  ------------------------------------
    100.0            2,112          1   2,112.0   2,112.0     2,112     2,112          0.0  vectorAdd(float *, float *, float *)

```
The output shows that the kernel only ran once and took ~2 microseconds. That’s extremely fast, which may sound good, but for a powerful GPU, this often means underutilization. 

**Solution**: Increase the problem size (e.g., 1 million elements instead of 1,000) to give the GPU enough work to justify the overhead.

####  CUDA GPU MemOps Summary (by Time)

```
 ** CUDA GPU MemOps Summary (by Time) (cuda_gpu_mem_time_sum):

 Time (%)  Total Time (ns)  Count  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)      Operation
 --------  ---------------  -----  --------  --------  --------  --------  -----------  ------------------
     52.2            2,656      2   1,328.0   1,328.0     1,216     1,440        158.4  [CUDA memcpy HtoD]
     47.8            2,432      1   2,432.0   2,432.0     2,432     2,432          0.0  [CUDA memcpy DtoH]

```
| Memory Operation               | 	Time %                          | What It Means                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| `HtoD (Host to Device)`	  | 52.2% | Over half of your execution time is just moving data to the GPU. This is very inefficient for such a small computation. |
| `DtoH (Device to Host)`	 | 	47.8% | Combined with the HtoD, this suggests that nearly all the runtime is overhead, not actual GPU compute. |

Therefore, when working with small kernels, where data transfer overhead often outweighs compute time, it’s recommended to use asynchronous memory copies or unified memory to reduce latency and improve overlap.

####  CUDA GPU MemOps Summary (by Size)

```
 ** CUDA GPU MemOps Summary (by Size) (cuda_gpu_mem_size_sum):

 Total (MB)  Count  Avg (MB)  Med (MB)  Min (MB)  Max (MB)  StdDev (MB)      Operation
 ----------  -----  --------  --------  --------  --------  -----------  ------------------
      0.008      2     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy HtoD]
      0.004      1     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy DtoH]
```

The output shows that only ~12 KB of data moved to/from the GPU. This confirms the workload is too small to justify the overhead of GPU execution.

#### OS Runtime Summary
```
** OS Runtime Summary:

Time (%)  Total Time (ns)  Num Calls    Name
--------  ---------------  ---------  ----------------------
  69.6      312,204,830         13    poll
  28.3      126,874,612        538    ioctl
```

This output means that most of the runtime was spent in system calls like `poll` and `ioctl`, which are unrelated to the kernel execution. This suggests the application is not compute-bound, and system overhead is prominent due to the small workload.