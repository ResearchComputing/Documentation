# NVIDIA Performance Counters

The NVIDIA Performance Counters provide low-level metrics on GPU usage, enabling users to understand how efficiently their code uses the GPU. This is especially important for optimizing workloads on Alpine’s A100 GPU nodes, where GPU time is a valuable and shared resource.

Available Tools
The following tools are available for interacting with performance counters:

- nvidia-smi: For basic monitoring of GPU resource usage.

- Nsight Compute (ncu): For detailed GPU kernel performance analysis.

## nvidia-smi

```nvidia-smi``` (System Management Interface) is a command-line utility that provides real-time information about GPU utilization, memory usage, temperature, and running processes.

Usage:

```
nvidia-smi
```
Example output of ```nvidia-smi``` on NVIDIA's ```aa100```
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
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

```
The output of nvidia-smi is divided into two major sections:

- GPU Hardware Overview Table

- Process Table (running processes using the GPU)

1. GPU Hardware Overview
This section provides real-time information about the GPU(s) installed in the system, including utilization, memory usage, temperature, power, and other performance-related statistics.

| Column               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| GPU |	The GPU index (starting from 0). In this case, GPU 0 is being shown. |
| Name | Full name of the GPU model. Here, it's NVIDIA A100-PCIE-40GB. |
| Persistence-M	| Shows whether Persistence Mode is enabled (helps reduce driver load time). It is Off here. |
| Bus-Id |	PCIe Bus ID of the GPU. Useful for identifying GPUs in multi-GPU systems. |
| Disp.A | Whether the GPU is attached to a display (usually Off on HPC systems). |
| Volatile Uncorr. ECC |	Reports single-bit error corrections that could indicate hardware instability (shows 0 here, which is good). |

Sensor and Resource Usage Metrics:

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

2. Processes Table
This section lists all processes currently using the GPU, along with how much memory each is using.

| Column               | Description                                         | 
| :----------------- | :-------------------------------------------------- | 
| GPU | Index of the GPU the process is using.| 
| GI/CI	| GPU Instance / Compute Instance — used only when MIG mode is enabled (both N/A here).| 
| PID	| Process ID of the application using the GPU.| 
| Type	| Type of process: C (Compute), G (Graphics), etc.| 
| Process Name	| Name of the executable or command using the GPU.| 
| GPU Memory Usage	| Amount of GPU memory the process is using.| 

```{note}
- Run nvidia-smi inside your allocated job session (e.g., after using sinteractive) to check whether your job is using the GPU.
- If no processes appear in the list but you expect your application to be running, it likely means the GPU is not being utilized. Please verify that your code is GPU-enabled and that CUDA is properly initialized.

```

## Nsight Compute (ncu)

NVIDIA Nsight Compute (ncu) is a command-line CUDA kernel profiler that provides detailed performance metrics for GPU kernels, helping users identify and resolve bottlenecks in CUDA applications. It is particularly well-suited for low-level kernel analysis and optimization.

Key Features:
- Collects performance data on SM utilization, memory throughput, warp execution efficiency, and more.

- Offers optimization guidance through diagnostic messages.

- Allows deep inspection into stall reasons, occupancy, and instruction efficiency

### Getting Started

To use ncu, first load the appropriate CUDA module:

```
module load cuda
```
You can then invoke ncu by prefixing it to your CUDA application:

```
ncu --set full --target-processes all ./sample_code
```
- ```--set full```: Collects a comprehensive set of performance metrics.

- ```--target-processes all```: Profiles all child processes (useful for multi-threaded applications).

```{note}
```ncu``` does not work on MIG-enabled nodes.
```

### Example CUDA code: Vector Addition
Here’s a simple CUDA program that adds two vectors of floats, compiled as vectorAdd.
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

Depending on the nature of the application, some CUDA kernels may be launched multiple times during a run (for example, a kernel called within a loop). For each kernel launch, the name of the kernel function (e.g., vectorAdd in the example above) and the progress of data collection is shown in the standard output (STDOUT). To collect all requested profile information for the many metrics that are included for profiling, you might need to replay the kernels multiple times. When the collection is completed, it will also show the number of replay passes of that kernel. For example:

``` 
==PROF== Profiling "vectorAdd" - 0: 0%....50%....100% - 49 passes
```

```{!WARNING}
Collecting performance data using ncu can incur significant runtime overhead on the application, as discussed here[https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#overhead].
```
When profiling a CUDA application using ncu, two sections in the output—GPU Speed Of Light Throughput and Launch Statistics, as they provide essential insights into how well your code is utilizing the GPU's hardware. Understanding these metrics helps identify performance bottlenecks and underutilization.

Why These Metrics Matter

Modern GPUs, such as the NVIDIA AA100, have hundreds of compute units (Streaming Multiprocessors or SMs). To fully exploit this parallel architecture, your kernel must be configured to launch enough threads and blocks to keep these units busy.

Key metrics to pay attention to include:

| Metric               | What It Measures                           | What It Matters                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| Block Size	| Threads per block	| Affects occupancy and granularity of parallelism |
| Grid Size	| Number of thread blocks	| Determines how many parallel blocks run; too few leads to idle SMs | 
| # SMs	| Number of Streaming Multiprocessors	| Shows total compute resources available
| Waves Per SM	| How many full waves of warps per SM	| Indicates how much parallel work is scheduled per compute unit | 
| Compute (SM) Throughput	| Percentage of peak compute capacity used	| Helps assess if the kernel is efficiently using the GPU's computational power | 

Here’s a simplified snippet from an ncu run on vectorAdd  
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
- 108 SMs: AA100 GPU has 108 compute units available.
- Waves Per SM = 0.00: Each SM received less than one full wave of work, which is not enough to keep it busy.
- Compute Throughput = 0.04%: The GPU was virtually idle during the kernel execution.

These numbers clearly show that the kernel is too small to utilize the hardware effectively.

| Symptom               | Likely Cause                          | Recommended Fix                           | 
| :----------------- | :------------------------------------------- |:-------------------------------------------------- |
| Grid size is smaller than #SMs	| Not enough blocks to occupy all compute units	| Increase the number of blocks by enlarging the problem size |
| SM throughput is very low (< 10%)	| GPU is mostly idle	| Optimize workload or parallelism granularity |
| Waves Per SM is 0	| Too little parallel work	| Increase N or restructure the launch configuration |

In the original kernel:
```
#define N 1024
dim3 block(256);
dim3 grid((N + block.x - 1) / block.x);  // → grid.x = 4 blocks
```
This launches just 4 blocks, causing underutilization.
To improve utilization:
```
#define N (1 << 20)  // 1,048,576 elements
dim3 block(256);
dim3 grid((N + block.x - 1) / block.x);  // → grid.x = 4096 blocks
```
This updated configuration allows the GPU to schedule multiple waves of work across all SMs, leading to much better throughput and performance.