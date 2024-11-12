# System Security Plan (SSP) Information

Systems that fall under the [CU Data Classification](https://www.cu.edu/data-governance/resources-support/data-classification) of **Confidential Information** or
**Highly Confidential Information** are required to provide a System Security Plan (SSP).
An SSP is a document that outlines how an organization protects the security of a system.
An SSP is a critical document that helps organizations meet compliance requirements.

The [OIT IT Security](https://oit.colorado.edu/services/it-security) group is responsible for guiding, evaluating and approving your SSP.
[OIT IT Security](https://oit.colorado.edu/services/it-security) prescribes the [NIST SP 800-171 Rev. 2](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final)
control set as the official standard to meet compliance requirements for **Confidential Information** and **Highly Confidential Information**.

Getting your SSP completed and approved is not only necessary, but can be a rigorous process.
The good news is that by using the OIT Research Computing [Cloud Foundations Service](https://www.colorado.edu/rc/cloudfoundations) (CFS)
**LCA1** solution, some of your security burden is handled by our service.

The CFS **LCA1** solution is an [AWS Landing Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html)
that is certified to support both **Confidential Information** and **Highly Confidential Information**.

The rest of this document will discuss how the CFS service can help you meet some of your security requirements.
We also have a quickstart guide to help you get started on your SSP journey.

## Contents
* Shared Responsibility Model
* CFS **LCA1** Features
* SSP Quickstart Process

### Shared Responsibility Model
Start with understanding the [Shared Responsibility Model](../getting-started/shared-responsibility-model.md).
It is important to know that the cloud provider, our service and you as the cloud customer all share the burden of securing systems.

### CFS **LCA1** Features
The OIT Research Computing [Cloud Foundations Service](https://www.colorado.edu/rc/cloudfoundations)
(CFS) team owns and manages an [AWS Landing Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html)
specifically designed to support the [NIST SP 800-171 Rev. 2](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final)
control set.  By using the CFS **LCA1** service, we help you meet some of your security controls.
Below is a list of features we offer that can help you with your SSP.

**Federated Identity and Access Management (IAM)**

When using the CSF **LCA1** landing zone, role access is integrated with the CU Boulder
[OIT Identity and Access Management](https://oit.colorado.edu/services/identity-access-management)
(IAM) offering.  This offering gives you:
* Single Sign On (SSO) using your [CU Boulder IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey)
* [Duo Multi-factor Authentication](https://oit.colorado.edu/services/identity-access-management/duo-multi-factor-authentication)
* Access management via [Enterprise Access Management (Grouper)](https://oit.colorado.edu/services/identity-access-management/enterprise-access-management)

You have full control of who can access your systems.

**Central Logging**

When using the CFS **LCA1** landing zone all user, role and service actions are centrally recorded
and stored with the proper data retention and audit policies.
This includes actions in the AWS Console, the AWS CLI, and AWS SDKs and APIs.
For more information, see [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) documentation.
This feature allows you to focus on your application logging without the need to build and maintain an extra logging layer.

**Managed Network and Firewall**

When using the CFS managed [AWS VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html),
you have a secure encrypted connection to the Internet with the ability to connection back to CU Boulder campus.
All traffic using the CFS managed AWS VPC is routed to a firewall to inspect both inbound and outbound traffic.
The firewall and campus connection are managed with a partnership with
[OIT Network and Internet Services](https://oit.colorado.edu/services/network-internet-services).


**Training and Support**

The OIT [Research Computing Support Team](https://curc.readthedocs.io/en/latest/#meet-the-rc-user-support-team)
is eager and ready to assist with training for you and your team in public cloud usage.
RC User Support also provides support services to help give advice and troubleshoot various cloud services.
RC User Support can also help with billing and cost optimization.

Not sure where to start with your cloud journey?  RC User Support is here to guide and assist!
Reach out to us at [rc-help@colorado.edu](rc-help@colorado.edu).

### SSP Quickstart Process
1. Determine your [Data Classification](https://www.cu.edu/data-governance/resources-support/data-classification)
2. Reach out to [rc-help@colorado.edu](rc-help@colorado.edu) so that we can gather basic questionnaire information about your workload.  This will include your data classification.  We can assist with your data classification if you are unsure.
2. Read and understand the [Shared Responsibility Model](../getting-started/shared-responsibility-model.md)
3. Work with [OIT IT Security](https://oit.colorado.edu/services/it-security) to get your SSP approved.
4. Once approved, request your CFS **LCA1** accounts.  We recommend a separate account for each environment (Prod, Dev, Test, etc.).  Simply email [rc-help@colorado.edu](rc-help@colorado.edu) and we are happy to assist.
