# Shared Responsibility Model

The [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) delineates the parts of the cloud environment that are the responsibility of AWS vs. the responsibility of the customer. AWS manages the infrastructure that provides the cloud services, and customers manage their use of those services.

The Cloud Foundations (CFS) team extends the shared responsibility model by providing an additional layer of support between AWS and the customer. CFS manages the integration of the AWS cloud with CU standards and resources. CFS customers manage their applications, data, and use of cloud services.

```{image} lca1_images/shared-responsibility-model/shared-responsibility-model.png
:alt: Infographic of the Shared Responsibility Model for Cloud Security, split into three stacked horizontal sections (Customer, Cloud Foundations, AWS), each with a left label box and right detail blocks. Top Section (Light Blue - Customer: Responsibility for Security in the Cloud): Stacked top-to-bottom on the right: 1. Customer Data, 2. Platform, Applications, Access Management, 3. Operating System & Firewall Configuration, 4. Side-by-side: Data Encryption & Integrity | Network Traffic Protection. Middle Section (Black - Cloud Foundations: Responsibility for Security of Integrating the Cloud with CU): Three side-by-side blocks on the right: 1. Account Brokering, 2. Campus/Cloud Integration (Billing, Identity, Logging, Network, DNS, Firewall), 3. Security Framework & Assistance. Bottom Section (Orange - AWS: Responsibility for Security of the Cloud): Stacked top-to-bottom on the right: 1. Software & Cloud Services, 2. Side-by-side: Compute | Storage & Database | Networking, 3. Hardware & Global Infrastructure.
:align: center
```

## Security

The shared responsibility model means that AWS, CFS, and customers collectively share responsibility for the security of the entire stack. That doesn't mean they all share every item in the stack (e.g., CFS doesn't help AWS secure its global infrastructure).

```{important}
**Each team is responsible for the security of the components for which they are accountable (in the RACI matrix).** Resources provisioned by customers are their responsibility to secure.
```

```{note}
Here's a quick way to think about security:

* AWS manages security **of** the cloud.
* CFS manages security of **integrating** the cloud with CU.
* Customers manage security **in** the cloud.
```

### Security Plans

Each party involved in securing an AWS account is expected to produce and maintain their own System Security Plan (SSP). CFS can help customers get started with their SSP, target the appropriate standards, and contribute pre-configured resources to reduce time to compliance.

Please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) for further information.

### Acceptable Use

All usage of AWS cloud accounts must comply with [CU Information Technology Policies](https://www.colorado.edu/information-technology/policy) and [Acceptable Use](https://www.colorado.edu/compliance/policies/acceptable-use-cu-boulders-it-resources).

## RACI Matrix

A [RACI matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) outlines the roles and responsibilities associated with managing a set of items.

> **R = Responsible (also recommender)**
>
> Those who are responsible for the correct completion of the task. There is at least one role with a participation type of responsible, although others can be delegated to assist in the work required.
>
> **A = Accountable (also approver or final approving authority)**
>
> The one ultimately answerable for the correct and thorough completion of the deliverable or task, the one who ensures the prerequisites of the task are met and who delegates the work to those responsible. In other words, an accountable must sign off (approve) work that responsible provides. There must be only one accountable specified for each task or deliverable.
>
> **C = Consulted (sometimes consultant or counsel)**
>
> Those whose opinions are sought, typically subject-matter experts, and with whom there is two-way communication.
>
> **I = Informed (also informee)**
>
> Those who are kept up-to-date on progress, often only on completion of the task or deliverable, and with whom there is just one-way communication.

Source: [Wikipedia Responsibility Assignment Matrix Page](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)

### Cloud Foundations RACI Matrix

The table below defines the key roles and responsibilities among AWS, Central IT (CURC / OIT), and customers in a cloud account.

| Responsibility Domain | Customer | Central IT (CURC/OIT) | AWS |
| --- | --- | --- | --- |
| Customer Data | RA | C | |
| Applications | RA | C | |
| Operating Systems | RA | C | |
| Access Management | RA | C | |
| Network Traffic Protection | RA | C | |
| Data Encryption/Protection | RA | C | |
| Customer Workload Security | RA | C | |
| Border Network Protection | CI | RA | |
| CU Private DNS Integration | I | RA | |
| Network Configuration | I | RA | |
| CU Campus Network Connectivity | I | RA | |
| CU Security Logging Integration | I | RA | |
| CU IdentiKey Integration | I | RA | |
| CU Billing Integration | C | RA | |
| Account Brokering | C | RA | I |
| AWS Software/Services | I | I | RA |
| AWS Hardware/Global Infrastructure | | | RA |

## Identifying CFS-Managed Resources

Where feasible, CFS labels all resources under its management by naming convention and/or tag and crafts policy to prevent modification of those resources by customers. However, CFS also chooses to give customers broad permissions so they may effectively self-manage their cloud environments and applications. At times customers may have the unintended ability to modify resources under CFS management. If this occurs, CFS reserves the right to correct configuration of these resources at any time without notice. Customers are encouraged to avoid modifying resources they did not create or those with the names/tags listed below.

```{note}
CFS-managed resources may be identified by one or more of the following:

* Tag: `oit-cld:management:central = true`
* Naming Prefix: `oitcld`
* Naming Prefix: `oit-cld-lza`
```

If there are any questions about resource ownership, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form).