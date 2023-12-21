# Azure  - Network Cost Guide

## Document Purpose

This document gives some sample cost estimates for select network access methods and provides the URL's to find current pricing. 

## Network access methods 

1) Internet Gateway - used with public IP
2) NAT Gateway - used with private IP
3) CFS Transit Gateway (VPN) - used with private IP address, VPN connects back to CU Boulder

### Internet Gateway

**Important**
Always check [Microsoft documentation](https://azure.microsoft.com/en-us/pricing/details/bandwidth/) for current pricing.
 
**Network costs**

1) Downloads - no cost

2) Uploads - first 100GB/month is free, tiered cost per 1GB transferred after

**Sample Network Cost**

2 Servers will download 100GB and upload 500GB in a month.

	1) Download cost = $0
	2) Upload cost = (100GB = $0) + ($0.087 x 400GB) = $34.80

	Total Network Cost = $34.80/month

### NAT Gateway

**Important**
Always check [Microsoft documentation](https://azure.microsoft.com/en-us/pricing/details/virtual-network/) for current pricing.

**Network Costs**
1) Downloads - $0.045/GB
2) Uploads - $0.045/GB
3) NAT Gatway Resource - 0.045/hr

**Sample Network Cost**

2 Servers on the same subnet will download 100GB and upload 500GB in a month.  The NAT gateway will be on the entire month.

	1) Download cost = $0.045 x 100 = $4.50
	2) Upload cost = $0.045 x 500 = $22.50
	3) NAT Gateway Instance = $0.045 x (24hr x 30day= 720hr) = $32.40

	Total Network Cost = $59.40/month

### CFS VNET Peering (VPN)

**Important**
Always check [Microsoft documentation](https://azure.microsoft.com/en-us/pricing/details/virtual-network/) for current pricing.

**Network Costs**
1) Downloads - $0.01/GB
2) Uploads - $0.01/GB

**Sample Network Cost**

2 Servers will download 100GB and upload 500GB in a month.  The VPC attachment will be on the entire month.

	1) Download cost = $0.01 x 100 = $1
	2) Upload cost = $0.01 x 500 = $5

	Total Network Cost = $6/month

