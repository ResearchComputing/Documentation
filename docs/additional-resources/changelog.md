# CURC System Changelog

The following is a high-level list of notable changes made to CU Research Computing systems grouped by year.

## 2026

::::{dropdown} Show 
:icon: note


| **Date** | **Change** | **Impact** |
| ------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Feb | Arbiter2 added to login nodes | All users will receive warnings (and potentially have their session terminated) if running intensive proccesses on login nodes |
| Feb | Added Mines IP ranges to greenlist for passwordless SSH via CILogon | Enable Mines users to log in and transfer files via terminal-based ssh in addition to Open OnDemand |
| Feb | Added NVIDIA GPU and VRAM utilization to `seff` command | Users and support staff are better able to track GPU usage metrics on NVIDIA nodes; Slurm job emails will now include this data also |
| Mar | `amilan128c` partition removed (rolled into `amilan`) | The `amilan128c` partition is no longer valid, but nodes are still accessible via `amilan`+constraint |
| Apr | `amc`, `csu`, and `rmacc` partitions removed | Affects user job submission parameters |
| Apr | SDS production rollout at [sds.rc.colorado.edu](https://sds.rc.colorado.edu) | New CURC service providing detailed information on software available to users (caveat: some content is AI-generated) |
| Apr | RCAMP upgrade (including new Django interface) | New interface for adding/removing users from groups/projects; Safari may no longer render interface correctly |
| Jun | Retired `mem` QoS, introduced `mem-normal` and `mem-long` QoS | Affects user job submission parameters |
| Jul | Created the QoS `gpu-normal`, `gpu-long`, and `gpu-testing`. Replaced all GPU partition QoS with these new QoS. Removed the `atesting_a100` and `atesting_mi100` partitions. | Affects user job submission parameters and max GPU limits per user and QoS |
| Aug | Renamed the `amilan` partition to `acpu` and the `normal` and `long` QoS to `cpu-normal` and `cpu-long`, respectively. Added 17 CPU-only nodes to the `acpu` partition, 8 nodes with 4 RTX Pro 6000 GPUs each to the new `artxpro6000` partition, and 8 nodes with 4 H200 GPUs each to the new `ah200` partition. |  Increased availability of CPU and GPU resources and affects user job submission parameters |
| Sep | Added job submission checks that ensure the `--oversubscribe` Slurm directive is only used with the `acompile` and `ahub` partitions. | Affects user job submission parameters. |
::::
