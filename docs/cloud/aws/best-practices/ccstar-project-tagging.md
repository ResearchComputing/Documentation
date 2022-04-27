## Project Tagging Requirement for ucboitrccumulus

<a href="url" target="_blank">LinkText</a>

### Document Purpose

This document describes the requirements that are expected of end users when using the **CUmulus** AWS Account.
The **CUmulus** AWS Account is a 'sandbox' like, shared AWS Account, that different Projects can use to consume an allocation of AWS Credits for prototyping and research activities.
The **CUmulus** AWS Account is not intended for long term production workloads.
In order to properly track the usage of your allocation, please be sure to follow the steps in this document to ensure that you are properly tagging your resources.

### AWS Resource Tagging

AWS resource tagging is critical for tracking actual costs (ie. credits), as well as forecasted costs.
As a user of the **CUmulus** environment, you are responsible for tagging all resources that are created in your Project.
The tag must be applied when (if possible), or immediately after, the resource is created.
For more information about how tags work, it's worth reading the <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html" target="_blank">AWS documentation describing Tags</a>.
If you are unfamiliar with the terms "tag key" and "tag value", please read and understand the <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html" target="_blank">AWS documentation describing Tags</a>.

### Project Tag

We are using the concept of a "Project" Tag to track different projects that will be using the shared **CUmulus** AWS Account.

When tagging resources, <u>there is only one tag that we require you to provide</u>.
This is the "**Project**" tag.
You are free to add more tags, as there are several other benefits of tagging discussed in the <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html" target="_blank">AWS documentation describing Tags</a>.

---
**IMPORTANT**: Note that the "tag **key**" is case sensitive.
This means that "<span style="color:green">**Project**"</span> is valid (must contain capital 'P').
Using "<span style="color:red">project</span>" (all lower case) as the key will generate an error, and this is the expected behavior.
---

The "tag **value**" will be the name of the Project that is given to you when your project was on-boarded by the Cloud Team (ie. argovis, flywheel).
The value must match exactly, and is case-sensitive.
You may not use any other value other than the one given to your Project.
Values that do not match a project will cause errors.
This is expected behavior.

There is no way to currently require the user to create the necessary Project tag when creating resources.
This is a current limitation with AWS.
This is why users need to be in the good habit of always adding the Project tag to all resources.

### Tag Examples

<table border=1>
<tr>
<td>
<b>( ! ) IMPORTANT: </b>
</td>
</tr>

<tr>
<td>
<span style="color:red">
The following examples show the Project Value = argovis.
<b>Use the name of your project instead</b> (ie. flywheel), and do not use the argovis value.
</span>
</td>
</tr>
</table>

For these examples, the tag value (or name of the Project) is "**argovis**" (all lower-case).
Almost every resource that you create in the AWS Console will have a 'Tags' section as described in the following examples.


#### Tag S3 Bucket in AWS Console


#### Tag EC2 Instance in AWS Console


#### Clustered Services


#### Tags Block in a CloudFormation Template


#### Add Tag using AWS CLI

