# CURC System Changelog

The following is a high-level list of notable changes made to CU Research Computing systems grouped by year.

## 2026

::::{dropdown} Show 
:icon: note


| **Date** | **Change** | **Impact** |
| ------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Feb-26 | Arbiter2 added to login nodes | All users will receive warnings (and potentially have their session terminated) if running intensive proccesses on login nodes |
| Feb-26 | Added Mines IP ranges to greenlist for passwordless SSH via CILogon | Enable Mines users to log in and transfer files via terminal-based ssh in addition to Open OnDemand |
| Feb-26 | Added NVIDIA GPU and VRAM utilization to `seff` command | Users and support staff are better able to track GPU usage metrics on NVIDIA nodes; Slurm job emails will now include this data also |
| Mar-26 | `amilan128c` partition removed (rolled into `amilan`) | The `amilan128c` partition is no longer valid, but nodes are still accessible via `amilan`+constraint |
| Apr-26 | `amc`, `csu`, and `rmacc` partitions removed | Affects user job submission parameters |
| Apr-26 | SDS production rollout at [sds.rc.colorado.edu](https://sds.rc.colorado.edu) | New CURC service providing detailed information on software available to users (caveat: some content is AI-generated) |
| Apr-26 | RCAMP upgrade (including new Django interface) | New interface for adding/removing users from groups/projects; Safari may no longer render interface correctly |
| Jun-26 | Retired `mem` QoS, introduced `mem-normal` and `mem-long` QoSes | Affects user job submission parameters |
| Jul-26 | Created the QoSes `gpu-normal`, `gpu-long`, and `gpu-testing`. Replaced all GPU partition QoSes with these new QoSes. Removed the `atesting_a100` and `atesting_mi100` partitions. | Affects user job submission parameters and max GPU limits per user and QoS |
| Aug-26 | Renamed the `amilan` partition to `acpu` and the `normal` and `long` QoSes to `cpu-normal` and `cpu-long`, respectively. Added 17 CPU-only nodes to the `acpu` partition, 8 nodes with 4 RTX Pro 6000 GPUs each to the new `artxpro6000` partition, and 8 nodes with 4 H200 GPUs each to the new `ah200` partition. |  Increased availability of CPU and GPU resources and affects user job submission parameters |
::::
