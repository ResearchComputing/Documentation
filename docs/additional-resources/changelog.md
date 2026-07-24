# CURC System Changelog

The following is a high-level list of notable changes made to CU Research Computing systems grouped by year.

## 2026

::::{dropdown} Show 
:icon: note


| **Date** | **Change** | **Impact** |
| ------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Feb-26 | Arbiter2 added to login nodes | All users will receive warnings (and potentially be booted) if running intensive proccesses on login nodes |
| Feb-26 | Added Mines IP ranges to greenlist for passwordless SSH via CILogon | Enable Mines users to log in via SSH instead of Open OnDemand-only |
| Feb-26 | Added NVIDIA GPU and VRAM utilization to `seff` command | Users and support staff are better able to track GPU usage metrics on NVIDIA nodes; Slurm job emails will now include this data also |
| Mar-26 | `amilan128c` partition removed (rolled into `amilan`) | Users need to be aware that the `amilan128c` partition is no longer valid, but nodes are still accessible via `amilan`+constraint |
| Apr-26 | `amc`, `csu`, and `rmacc` partitions removed | Affects user job submission parameters |
| Apr-26 | SDS production rollout at [sds.rc.colorado.edu](https://sds.rc.colorado.edu) | New CURC service that affects software information available to users (caveat: some content is AI-generated) |
| Apr-26 | RCAMP upgrade (including new Django interface) | New interface for adding/removing users from groups/projects; Safari may no longer render interface correctly |
| Jun-26 | Retired `mem` QoS, introduced `mem-normal` and `mem-long` QoSes | Affects user job submission parameters |

::::
