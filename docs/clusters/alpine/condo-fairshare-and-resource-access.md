This purpose of this document is to provide a detailed overview of 
Alpine's FairShare and resource access policies. The intended audience is 
Alpine's insitutional-level condo contributors.

Updated November 4, 2022 

### Goals and philosophy 

The Alpine supercomputer hosted at CU Boulder and administered by Research 
Computing at CU Boulder (CURC) supports institutional condo purchases, the 
first two of which come online in the fall of 2022. This document outlines 
how jobs affiliated with condo contributors will be assigned priority and 
billing weight on the system. It does not aim to address FairShare scoring 
for individual users and allocations, as these involve more detail and 
complexity than this document intends to cover. 

The goals of this policy are to maximize overall system utilization, 
assign appropriate priority and billing weights proportional to 
contribution, and maintain a straightforward and accountable 
configuration. This document describes the initial policy, but changes to 
any or all of it are possible based on contributor feedback, user issues, 
CURC’s own data-gathering and monitoring, and other factors. 

### Node, partition, and FairShare policies 

#### Overview 

All nodes, whether contributed by CU Boulder or by another institution, 
will be added to a shared partition to which all Alpine users will have 
access. This does not preclude adding nodes to one or more additional 
partitions with different settings and attributes. At minimum, CURC will 
create one dedicated partition and QOS per contributor. 

By configuring all nodes into a common pool by default, CURC intends to 
better maximize system utilization and ensure that users are not locked 
out of Alpine due to (for example) power or networking issues that only 
affect their institution’s nodes. Users will always have the option to 
request specific node attributes for their jobs – for example, presence of 
GPUs, InfiniBand, or high clock speeds – and those requests will remain 
part of all scheduling calculations. 

Through a combination of QOS’s, trackable resources, partitions, and other 
Slurm settings, users will receive some preference for running jobs on 
their own nodes. However, preemption of jobs will not be supported. 

As one of several determinants of job priority, CURC will assign a 
FairShare score in the Slurm database for each condo buy-in on Alpine 
based on the institution’s total contribution to the system. This will 
account for total cores, clock speeds, cores on nodes with high memory 
(>=1TB), and GPUs. All resources will be billed back accordingly at the 
time of job submission. 

#### GPU calculations 

To compute the GPU term in the FairShare equation, CURC will multiply 
total contributed GPUs by an "acceleration factor". This factor is derived 
from the MATLAB GPU benchmark series, which CURC has used to measure 
computational performance on a variety of tasks on a representative GPU 
against the equivalent on a CPU. 
As of November 2022, the acceleration factor of an NVIDIA A100 or AMD 
MI100 GPU will be 108.6, meaning that our benchmarks indicate a GPU will 
provide 108.6x speedup (on average) over a CPU. Scaling this to a typical 
Alpine node, the number of SUs allocated for a 64-core node with 3 GPUs 
and 64 cores would be a factor of 5-6 higher than a 64-core CPU-only node. 
This figure and the choice of benchmarking software are subject to change 
in the future based on new information. 

#### Complete equation 

The exact score will be derived from the following equation: 

```
FairShare = floor ( (standard node CPU core hours contributed 
* average clock speed / minimum clock speed on Alpine) 
+ (GPUs contributed * GPU acceleration factor) # changed in this version 
+ (high-memory node CPU core hours contributed 
* average clock speed in MHz / minimum clock speed available 
* mem-per-core_high-mem / mem-per-core_standard=256GB)) 
```

To distribute the FairShare score, each institutional contributor will 
receive an account (containing all its affiliated users) that will hold 
the full score. In turn, each of those accounts will contain a "general" 
subaccount that will have 20% of the FairShare pool and a "projects" 
subaccount with 80%. (The general/projects pattern is already in place on 
Alpine and is a pattern CURC initially set up on Summit.) Contributors 
wishing for a different accounting arrangement from "general/projects" 
should reach out to CURC with specific requests. 

This crediting and billing system is intended to balance contributions and 
utilization. 

#### Example and comment on FairShare and billing 

Suppose the lowest rated clock speed available on any Alpine node is 
2.2GHz. Acme University contributes the following order: 

- 16x 64-core 3.2GHz CPU nodes with 256 GB RAM 
- 2x GPU node with 3 A100 GPUs, same CPU 
- 4x 1TB high-memory nodes, same CPU 

For this order, Acme would receive the following score: 

```
Acme University FairShare = floor ( 
  16 * (64+2) * 3200MHz / 2200MHz           # 1536 
  + 2 * 3 GPUs * 108.6/GPU                  #  651.6 
  + 4 * 64 * (1028 GB RAM / 256 GB RAM))    # 1028 
  = 3,215 
```

Note that prior to the change described in this policy, the GPU term was 2 
x 3 x 6912 = 41,472. 

These scores will be revised upon new nodes being contributed. 

GPU, CPU, and memory (along with potentially other resources in the 
future) will be billed to users in proportion to their weight in the 
fairshare calculation. For example, a partition might be configured with 
any of the following resource billing weights: 

```
TRESBillingWeights="CPU=1.0,GRES/gpu:a100=108.6" 
TRESBillingWeights="CPU=1.0,GRES/gpu:mi100=108.6" 
TRESBillingWeights="CPU=1.0,Mem=4.0" 
```

Additionally, CURC reserves the authority to modify this policy or 
specific jobs if users abuse it – if, for example, a contributor purchases 
many GPU cores and uses their share of "credit" from those GPUs to exploit 
another contributor’s CPU-only contributions. 

### Reporting 

CURC will provide regular reports to institutional Alpine partners to 
demonstrate they are receiving appropriate value for their contributions. 
The full content of these reports is beyond the scope of this document, 
but it will include measurements of resource utilization, statistics 
useful for quality assurance, and the number and size of jobs run. 

CURC will generate automated reports monthly and share them through 
appropriate channels, either written or in-person. CURC will also produce 
more detailed reports examining the overall value of the system to condo 
contributors once per quarter. Reports may be addressed to the institution 
or, if applicable, to the condo buyer within the institution (for example, 
a PI or department). 

Note that some Slurm usage querying tools are also available for general 
systems users, including `sinfo`, `sshare`, `sreport`, and `squeue`. 
Public-facing reports and dashboards are available online through RC’s 
instance of XDMoD. 

### Key details 

Please note the following about the way Slurm calculates priority: 

- A job’s priority is based on multiple factors in addition to the 
FairShare score, including (but not limited to) job age, resources 
requested, job size, and QOS. 
- The FairShare component of the final priority calculation is determined 
by normalizing the institution’s FairShare against the highest FairShare 
on the system. 
- FairShare scores for sub-accounts (e.g., acme-projects and acme-general) 
are normalized against each other. These sub-accounts will be assigned 
scores at an appropriate 80/20 ratio, which will not need to be changed to 
accommodate expansions or new contributions. 

In most but not all cases, changes to FairShare scores, QOSs, and other 
Slurm settings are straightforward to implement. Systems administrators 
can apply these changes quickly once CURC and the contributor(s) agree 
upon them. 

For additional details about how Slurm implements this score, please 
consult the official Slurm documentation (in particular, docs pertaining 
to the "Multifactor Priority Plugin") or follow up with CURC with specific 
questions. This policy is now in effect and is subject to change at any 
time. 


Alpine is jointly funded by the University of Colorado Boulder, the 
University of Colorado Anschutz, Colorado State University, and the National Science 
Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these 
docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
