# Setting up a Load Balancer

Setup a load balancer to publicly expose services running on the internal Virtual Private Cloud(VPC). This is to be used when you have a service running on the internal campus network (CFS VPC private subnets) and want to expose it to the outside internet. To accomplish this we must put a load balancer in front of the VPC. There are many different ways to accomplish this goal. Below is an example of one way that you can set this up.

## Network Load Balancer Example

In this example we assume the prerequisite of an Amazon Elastic Compute Cloud (EC2) instance using the CFS VPC on the private subnet. The EC2 instance is running nginx on port 443 and has an inbound security group rule allowing access to port 443 on the EC2 instance. We are going to expose it to the outside internet on port 443 using a network load balancer.

```{note}
This example does not include setting up a domain name or certificates. Ensure that you are creating resources in the same region as your EC2 instance.
```

1. Navigate to Load Balancers by searching for "Load Balancers" in the main search box.

```{image} load_balancer_images/search.png
:alt: AWS Management Console search results for load balancers, with the EC2 Load balancers feature highlighted. Described under Network Load Balancer Example.
:align: center
```
2. Select "Create load balancer"

```{image} load_balancer_images/create-lb.png
:alt: AWS EC2 Load balancers page with a Create load balancer button. Described under Network Load Balancer Example.
:align: center
```

3. Select "Network Load Balancer"

```{image} load_balancer_images/select-lb-type.png
:alt: AWS Create load balancer page listing Application, Network, and Gateway load balancer types, with Network Load Balancer as the choice for this example. Described under Network Load Balancer Example.
:align: center
```

4. Under the Basic configuration section, name the load balancer and leave the rest of the settings as defaults

```{image} load_balancer_images/name-nlb.png
:alt: AWS Network Load Balancer basic configuration section with a name field. Described under Network Load Balancer Example.
:align: center
```

5. Under the Network mapping section, select "cfs-vpc". Then check the availability zones you would like to use. Make sure to select the public subnet.

```{image} load_balancer_images/select-subnet.png
:alt: AWS Network mapping section with cfs-vpc selected and public subnets checked for the chosen Availability Zones. Described under Network Load Balancer Example.
:align: center
```

6. Scroll down to the "Security groups" section. Click the link to "create a new security group". This will open a new tab with the security group wizard.

7. For this example we will allow inbound traffic on port 443 from anywhere. Give your security group a name and description. Then click add inbound rule, select "HTTPS" as type, and choose "anywhere" as source. Then click "Create security group". Now go back to the Load balancer wizard tab.

```{image} load_balancer_images/security-group-wizard.png
:alt: AWS Create security group wizard with an inbound HTTPS rule from anywhere on port 443. Described under Network Load Balancer Example.
:align: center
```

8. Under the Security group section, click the refresh icon next to the select security group box. Then remove the default security group and select the security group that was just created.

```{image} load_balancer_images/security-group.png
:alt: AWS load balancer Security groups section with the newly created security group selected. Described under Network Load Balancer Example.
:align: center
```

9. Under the Listeners and routing section, select the "Create target group" link. This will open a new tab with the target group wizard.

10. In this example we will select "Instances" target type. Give your target group a name.

```{image} load_balancer_images/target-group-type.png
:alt: AWS Create target group page with Instances selected as the target type and a name field. Described under Network Load Balancer Example.
:align: center
```

11. In this example we will use port 443. Make sure to select the "cfs-vpc"

```{image} load_balancer_images/target-group-port-443.png
:alt: AWS Create target group protocol and port settings with TCP port 443 and cfs-vpc selected. Described under Network Load Balancer Example.
:align: center
```

12. Select your EC2 target(s) and then select "Include as pending below". Then select "Create target group" to complete the target group creation.

```{image} load_balancer_images/select-target-443.png
:alt: AWS Register targets page with an EC2 instance selected and Include as pending below available. Described under Network Load Balancer Example.
:align: center
```

13. The target group is now created and the tab can be closed. Now go back to the Load balancer wizard, click the little refresh icon and then select the target group that was just created. Enter the load balancer listening port (443 in this example) and type of traffic (TCP in this example). Then scroll down and "Create load balancer" to complete the setup.

```{image} load_balancer_images/listeners443.png
:alt: AWS Listeners and routing section with TCP port 443 forwarding to the new target group. Described under Network Load Balancer Example.
:align: center
```

14. Once your load balancer state changes from provisioning to active you will be able to access your service at https:// followed by the load balancer DNS name. Please note there can be a few minute delay for the load balancer to be reachable.

```{image} load_balancer_images/load-balancer-dns.png
:alt: AWS Network Load Balancer details page showing Active status, DNS name, internet-facing scheme, and a TCP 443 listener. Described under Network Load Balancer Example.
:align: center
```