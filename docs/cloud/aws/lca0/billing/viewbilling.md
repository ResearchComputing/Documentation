# AWS - View Billing Data

```{note}
For all billing periods beginning after 6/30/2025, you should refer directly to [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and your invoices in the [CU Marketplace](https://www.cu.edu/uis/service-catalog/cu-marketplace). CloudCheckr is no longer used for billing information.
```

## How AWS billing works

Four Points Technology (FPT) is our AWS reseller. They invoice you for your AWS usage monthly via the [CU Marketplace](https://www.cu.edu/uis/service-catalog/cu-marketplace).

## Discounts

FPT provides us with the following discounts:

* Contract Discount on most AWS resources, excluding AWS Marketplace, S3 Glacier Deep Archive, and AWS Storage Deep Archive charges
* Egress waiver for some traffic ([contact us](mailto:rc-help@colorado.edu) for additional details)

```{important}
Due to this discount, what you see in the default AWS Cost Explorer will not match what's on your invoices. See below for how to calculate your actual costs from AWS Cost Explorer.
```

## Viewing your invoices

Your invoices and associated purchase orders (PO) can be viewed in the [CU Marketplace](https://www.cu.edu/uis/service-catalog/cu-marketplace).

```{note}
FPT combines the charges for all AWS accounts paid by the same PO into a single invoice for each month.
```

## Calculating your costs with AWS Cost Explorer

Here's how to use AWS Cost Explorer to represent the charges you will see on an invoice from FPT. We'll use an example from May 2025.

1. [Log into your AWS account](../getting-started/aws-console-access) and navigate to the Billing and Cost Management service. Choose Cost Explorer from the menu on the left.
   ```{image} images/billing-and-cost-management.png
   :alt: Search for "Billing and Cost Management" in the AWS console.
   ```
   ```{image} images/cost-explorer-menu.png
   :alt: Click on "Cost Explorer" in the menu on the left.
   ```

1. Filter on the billing month.
   ```{image} images/cost-explorer-billing-month.png
   :alt: Filter the date range to July 2025.
   ```

1. You’ll see the unfiltered cost at the top of the report. **This is NOT what you will be billed!**
   ```{image} images/cost-explorer-unfiltered.png
   :alt: Unfiltered costs are $21,675.23.
   ```

1. Remove automatically applied refunds by adding the filter `Charge Type → Excludes → Refund, Enterprise Discount Program Discount and Solutions Provider Program Discount ` under `More Filters`.
   ```{image} images/cost-explorer-exclude-refunds.png
   :alt: Set the Charge Type filter to exclude refunds, enterprise discount program discount and solution provider program discounts.
   ```

1. Now you’ll see the raw costs for that billing period.
   ```{image} images/cost-explorer-raw.png
   :alt: Raw costs are $22,669.03.
   ```

1. Add a filter to remove AWS Marketplace costs. Set `Billing Entity → Excludes → AWS Marketplace`.
   ```{image} images/cost-explorer-exclude-marketplace.png
   :alt: Set the Billing entity filter to exclude AWS Marketplace.
   ```

1. Add a filter to remove S3: Storage - Glacier Deep Archive. Set `Usage type group → Excludes → S3: Storage - Glacier Deep Archive`.
   ```{image} images/cost-explorer-exclude-deeparchive.png
   :alt: Set the Usage type group filter to exclude S3: Storage - Glacier Deep Archive.
   ```
1. Add a filter to remove OCBLateFee and Support (Enterprise). Set `Service-> Excludes →  OCBLateFee and Support (Enterprise)`.
   ```{image} images/cost-explorer-exclude-ocblatefee.png
   :alt: Set the Service filter to exclude OCBLateFee and Support (Enterprise).
   ```

1. Add a filter to remove all items matching "Xfer-Out-Bytes" and "Transfer-Out-Bytes". Set `Usage type → Excludes → all items matching “Xfer-Out-Bytes” and “Transfer-Out-Bytes”`.
   ```{image} images/cost-explorer-exclude-xferoutbytes.png
   :alt: Set the Usage type filter to exclude all items matching “Xfer-Out-Bytes” and “Transfer-Out-Bytes”.
   ```
  ```{image} images/cost-explorer-exclude-transferoutbytes.png
   :alt: Set the Usage type filter to exclude all items “Transfer-Out-Bytes”.
   ```
1. Now your total will show the AWS resources eligible for discount.
   ```{image} images/cost-explorer-discount-eligible.png
   :alt: Costs eligible for discount are $22,001.87.
   ```

1. Manually apply the discount in the contract(here we are considering a 1%) on the eligible costs from the previous step. In this example, the total discounted AWS resource costs are $1,944.62.
   ```{math}
   Discounted AWS Resource Costs = Discount Eligible Costs \times (100\% - 1\%)
   ```
   ```{math}
   $21,781.85 = $22,001.87 \times 0.99
   ```
   ```{note}
   Note this number as `Discounted AWS Resource Costs` for future use below.
   ```

1. Next we need to add AWS Marketplace and Deep Archive costs that are **NOT** eligible for discounts. Remove both the `Billing Entity` and `Usage type group` filters. Your total should again show the raw costs ($3,381.06).
   ```{important}
   Do not remove the `Charge Type` filter.
   ```

1. Determine AWS Marketplace costs. Set `Billing Entity → Includes → AWS Marketplace`.
   ```{image} images/cost-explorer-include-marketplace.png
   :alt: Set the Billing entity filter to include only AWS Marketplace.
   ```

1. Your total should now show just AWS Marketplace costs.
   ```{image} images/cost-explorer-marketplace.png
   :alt: AWS Marketplace costs are $83.20.
   ```
   ```{note}
   Note this number as `AWS Marketplace Costs` for future use below.
   ```

1. Remove the `Billing Entity` filter.

1. Determine Deep Archive costs. Add a filter for `Usage Type group → Includes → S3: Storage - Glacier Deep Archive`.
   ```{image} images/cost-explorer-include-deeparchive.png
   :alt: Set the Usage Type group filter to include only S3: Storage - Glacier Deep Archive.
   ```

1. You’ll see the total of just the Deep Archive costs.
   ```{image} images/cost-explorer-deeparchive.png
   :alt: AWS Deep Archive costs are $52.62.
   ```
   ```{note}
   Note this number as `AWS Deep Archive Costs` for future use below.
   ```

1. Sum the `Discounted AWS Resource Costs`, `AWS Marketplace Costs`, and `AWS Deep Archive Costs`. This is the total charge for this account, `Account Total`.
   ```{math}
   Account Total = Discounted AWS Resource Costs + AWS Marketplace Costs + AWS Deep Archive Costs
   ```
   ```{math}
   $21,917.67 = $21,781.85 + $83.20 + $52.62
   ```

1. Repeat this process for each of your accounts. The total across all accounts that use the same PO should match the invoice you receive in the [CU Marketplace](https://www.cu.edu/uis/service-catalog/cu-marketplace).
   ```{math}
   Invoice Total = \sum_{i \in Accounts} Account Total_i
   ```

```{note}
If you have any questions about your bill or need help calculating your costs, please [contact us](mailto:rc-help@colorado.edu).
```
