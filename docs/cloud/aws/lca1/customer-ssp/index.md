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
We also have a quickstart guide to help you get started on your SSP journey.

## Contents
* [Shared Responsibility Model](#shared-responsibility-model)
* [CFS **LCA1** Features](#cfs-lca1-features)
* [SSP Quickstart Process](#ssp-quickstart-process)

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

### SSP Quickstart Process

1. Determine the [Data Classification](https://www.cu.edu/data-governance/resources-support/data-classification).
2. Read and understand the [Shared Responsibility Model](../getting-started/shared-responsibility-model.md).
3. Get an account on **LCA1**.  Reach out to [rc-help@colorado.edu](mailto:rc-help@colorado.edu) so that we can gather basic questionnaire information about your workload.  This will include your data classification.  We can assist with your data classification if you are unsure.
4. Secure your workload and create the SSP.  Work with [IT Security](https://oit.colorado.edu/services/it-security) to get the SSP submitted and reviewed.
5. After OIT Security review and Product Owner approval, start operating your secure workload.
