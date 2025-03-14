# System Security Plan (SSP) Information

Systems that fall under the [CU Data Classification](https://www.cu.edu/data-governance/resources-support/data-classification) of **Confidential Information** or
**Highly Confidential Information** are required to provide a System Security Plan (SSP).
An SSP is a document that outlines how an organization protects the security of a system.
An SSP is a critical document that helps organizations meet compliance requirements.

Look here for more information about [Data Classification](../data-classification.md).

OIT's [IT Security](https://oit.colorado.edu/services/it-security) group is responsible for guiding and evaluating your SSP.
[IT Security](https://oit.colorado.edu/services/it-security) prescribes the [NIST SP 800-171 Rev. 2](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final)
control set as the official standard to meet compliance requirements for **Confidential Information** and **Highly Confidential Information**.

Getting your SSP completed and approved is not only necessary, but can be a rigorous process.
The good news is that by using the OIT Research Computing [Cloud Foundations Service](https://www.colorado.edu/rc/cloudfoundations) (CFS)
**LCA1** solution, some of your security burden is handled by our service.

The CFS **LCA1** solution is an [AWS Landing Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html)
that is approved to support **Confidential Information**.  Support for **Highly Confidential Information**
is on the horizon.

The rest of this document will discuss how the CFS service can help you meet some of your security requirements.
We also have a guide to help you get started on your SSP journey.

## Contents
* [Shared Responsibility Model](#shared-responsibility-model)
* [CFS **LCA1** Features](#cfs-lca1-features)
* [Getting Started](#getting-started)

### Shared Responsibility Model
Start with understanding the [Shared Responsibility Model](../getting-started/shared-responsibility-model.md).
It is important to know that the cloud provider, our service and you as the cloud customer all share the burden of securing systems.

### CFS **LCA1** Features
The OIT Research Computing [Cloud Foundations Service](https://www.colorado.edu/rc/cloudfoundations)
(CFS) team owns and manages an [AWS Landing Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html)
specifically designed to enable support of the [NIST SP 800-171 Rev. 2](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final)
control set.  By using the CFS **LCA1** service, we help you meet some of your security controls.
Below is a list of features we offer that can help you with your SSP.

```{important}
Using the CFS **LCA1** service does not automatically make your system compliant.  Our system is a foundation that enables you to be compliant.
```
```{note}
As a best practice, we recommend a separate **LCA1** account for each workload environment (prod, dev, test, etc.)
```

**Federated Identity and Access Management (IAM)**

When using the CFS **LCA1** landing zone, role access is integrated with the CU Boulder
[OIT Identity and Access Management](https://oit.colorado.edu/services/identity-access-management)
(IAM) offering.  This offering gives you:
* Single Sign On (SSO) using your [CU Boulder IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).  The role we provide you is set up with temporary short-term credentials to help you meet compliance and best practices.
* [Duo Multi-factor Authentication](https://oit.colorado.edu/services/identity-access-management/duo-multi-factor-authentication).
* Access management via [Enterprise Access Management (Grouper)](https://oit.colorado.edu/services/identity-access-management/enterprise-access-management).  Audit logging for federated access is handled by the Grouper service.

You have full control over who can access your AWS accounts.

**AWS Root Account User Protection**

CFS secures the [AWS Root Account User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
for all your **LCA1** accounts. We add MFA to the Root User.  We securely store and rotate the password.
We have alarms set up to detect any usage of this important and powerful admin user.  Our internal
procedures ensure that the root user is only used for approved use, requires approval, and is only
used for very rare cases.  For a list of things that only the root user can do,
[see this page](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks).
In the rare event that any of these actions are needed, [rc-support@colorado.edu](mailto:rc-support@colorado)
can assist with submitting a ticket with the CFS team.

**Centralized Audit Logging**

When using the CFS **LCA1** landing zone all user, role and service actions are centrally recorded
and stored with the proper data retention and audit policies.
This includes actions in the AWS Console, the AWS CLI, and AWS SDKs and APIs.
For more information, see [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) documentation.
This feature allows you to focus on your application logging without the need to build and maintain an extra audit logging layer.

As an added bonus, any [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
you create will be centrally logged with the proper data retention and audit policies.
See the AWS [Centralized Logging](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/centralized-logging.html)
documentation for more details.

**Managed Network and Firewall**

When using the CFS managed [AWS VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html),
you have a private subnet with an encrypted connection to the CU Boulder campus.
You also get a internet subnet that we manage.  Both subnets are inspected by a firewall.
Both inbound and outbound traffic are inspected.
The firewall and campus connection are managed by a partnership with
[OIT Network and Internet Services](https://oit.colorado.edu/services/network-internet-services).

For more information about this feature, see the **LCA1** [Network Information](../networking.md) page.

**Training and Support**

The OIT [Research Computing Support Team](https://curc.readthedocs.io/en/latest/#meet-the-rc-user-support-team)
is eager and ready to assist with training for you and your team in public cloud usage.
RC User Support also provides support services to help give advice and troubleshoot various cloud services.
RC User Support can also help with billing and cost optimization.

Not sure where to start with your cloud journey?  RC User Support is here to guide and assist!
Reach out to us at [rc-help@colorado.edu](mailto:rc-help@colorado.edu).

### Getting Started
Beginning your SSP can be intimidating, but there are strategies your can take to set yourself up for success and streamline the process. These are the steps we recommend for working through your SSP.

#### Prepare for the SSP
Before you begin, make sure you have the necessary technical infrastructure and social processes defined to act as a consistent, coordinated team.

1. **Identify a service owner.** Your service needs a single person to be accountable for implementing and operating the service. This person will ensure security work is actually implemented and make the final decision about when to move forward after IT Security review.
2. **Define your service.** You need to nail down exactly what you will be securing. What are all of its features? Who consumes it? What other services does it integrate with? You need to detail precisely what the services does so you can secure each of those aspects.
3. **Determine the [Data Classification](https://www.cu.edu/data-governance/resources-support/data-classification) for your service.** This informs what security controls will apply to your SSP.
4. **Select an internal documentation platform.** You will need to generate lots of process documentation that IT Security can review, and that your team will use for securely operating your service. Make sure this is in one standardized location.
5. **Select an external documentation platform.** You will need to publish documentation for your customers about how to securely use your service and what's expected of them.
6. **Select a work tracking system.** You will need to coordinate on numerous tasks as a team and be able to reliably complete recurring work.
7. **Select a monitoring and alerting system.** You will need to make sure your service is operating as intended in an ongoing manner and scan it against standard security baselines. Make sure your alerting is flexible enough to handle different tiers of alerts and different sets of recipients.
8. **Select an events management system.** Alerts from your monitoring system need to end up somewhere that the entire team can see but enforces accountability for dealing with them. Make sure the team has a process for selecting who handles notifications and how that is tracked.
9. **Select a configuration management system.** Reviewers of your SSP will want to see evidence of how all aspects of your system are configured. If you can manage changes and tracking in a central configuration system, it will be much easier than trying to document and enforce manual processes.
10. **Select a change management system.** Establish practices as a team for how you will track changes to your service and the infrastructure that supports it. You will need to ensure changes can be audited and rationalized.
11. **Select a system for tracking your SSP.** You'll need to keep track of each control and how that is met by your team. The SSP will need to be updated periodically as part of ongoing reviews and service changes. Choose something that supports sorting and filtering, not a Word document.

```{note}
##### Example Preparation Tools
Here are some tools you might consider for implementing the systems above. Think about what your team already owns or has access to. Think about what data you plan to store in each tool and make sure that follows the appropriate security guidelines. **These are examples, not endorsements.**

* **Internal documentation platform:**
  * [Markdown in GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
  * [Confluence](https://www.atlassian.com/software/confluence)
  * [Microsoft Teams Files](https://support.microsoft.com/en-us/office/file-storage-in-microsoft-teams-df5cc0a5-d1bb-414c-8870-46c6eb76686a)
* **External documentation platform:**
  * [GitHub Pages](https://pages.github.com/)
  * [Read the Docs](https://about.readthedocs.com/)
  * Your existing public website
* **Work tracking system:**
  * [Jira](https://www.atlassian.com/software/jira)
  * [Microsoft Planner](https://www.microsoft.com/en-us/microsoft-365/planner/microsoft-planner)
  * [Trello](https://trello.com/)
* **Monitoring and Alerting system:**
  * [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)
  * [Prometheus](https://prometheus.io/)
  * [Icinga](https://icinga.com/)
  * [Zabbix](https://www.zabbix.com/)
  * [Naemon](https://www.naemon.io/)
* **Events management system:**
  * [Opsgenie](https://www.atlassian.com/software/opsgenie)
  * [ServiceNow](https://www.servicenow.com/products/event-management.html)
  * [GitHub Issues](https://github.com/features/issues)
  * A shared email inbox with manual accountability processes
* **Configuration management system:**
  * [Terraform](https://www.terraform.io/)
  * [OpenTofu](https://opentofu.org/)
  * [Ansible](https://www.redhat.com/en/ansible-collaborative)
  * [Pulumi](https://www.pulumi.com/)
* **Change management system:**
  * [GitHub Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models)
  * [ServiceNow](https://www.servicenow.com/products/change-management.html)
  * A manual change log with an established process
* **System for tracking your SSP:**
  * A spreadsheet
  * A database
  * [Airtable](https://www.airtable.com/)
```
#### Implement the SSP
The next step is to stand up your service, creating the necessary security control implementations and documentation.

1. **Get the latest controls.** Reach out to [IT Security](https://oit.colorado.edu/services/it-security) to get the latest official list of required controls. Import this into your SSP tracking system. Confirm which subset of the controls apply to your service (usually based on data classification and service criticality).
2. **Learn about shared responsibility.** Read and understand the [Shared Responsibility Model](../getting-started/shared-responsibility-model.md).
3. **Stand up your service.** Get an account on **LCA1**. Reach out to [rc-help@colorado.edu](mailto:rc-help@colorado.edu) so that we can gather basic questionnaire information about your workload. Build out your service on AWS, but _do not put any non-public data in yet._
4. **Secure your service.** Implement each of the required security controls by appropriately configuring your infrastructure, establishing team processes, and documenting everything. Ensure your documentation provides enough detail an auditor can use for evidence of proper implementation. Consider using references to your configuration management system and screenshots where appropriate.

#### Review the SSP
Finally, review your SSP implementation with IT Security. After they have reviewed, the service owner can decide if it's appropriate for non-public data to be introduced to the service.

1. **Review.** Request an SSP review from [IT Security](https://oit.colorado.edu/services/it-security). Work with them to fix any gaps in the plan. If there are gaps that can't be addressed, work with IT Security to draft a [Plan of Action and Milestones (POA&M)](https://csrc.nist.gov/glossary/term/POAM) for those items or document the additional risk that gap creates.
2. **Approve.** After IT Security has reviewed the SSP, they will make a recommendation to the service owner. At that time, the service owner should weigh the SSP status with the outstanding risks to decide if the service should proceed with hosting non-public data.
3. **Operate.** Once the service owner has approved the SSP, the service can begin operating with non-public data. Regular tasks, as outlined by the SSP, should be integrated into ongoing service operations.

```{important}
A POA&M is essentially a promise to address a security gap in the future. It must have a plan and a **due date**. IT Security should be notified about completed POA&Ms, and they should be updated in your SSP.
```
