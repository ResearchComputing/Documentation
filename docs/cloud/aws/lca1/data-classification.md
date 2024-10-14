# Data Classification

```{important}
Before using your AWS account to store, process, or transmit data, you must determine its Internal and External classification and ensure the hosting environment is rated to manage that data type.
```

## Data Classification Levels

### Internal

The University classifies data in three levels:

* Public
* Confidential
* Highly Confidential

For information about what category your data falls in, see this [Data Governance documentation](https://www.cu.edu/data-governance/resources-support/data-classification).

### External

Along with CU data classifications, some data types, such as [HIPAA](https://www.hhs.gov/hipaa/index.html) and [PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard), are regulated by outside entities. This data must adhere to additional requirements and auditing above what CU requires internally.

Externally-regulated data also includes, but is not limited to: contracts with a [DFARS 7021 clause](https://www.acquisition.gov/dfars/252.204-7021-cybersecurity-maturity-model-certification-requirements.), requirements for [CMMC certification](https://dodcio.defense.gov/CMMC/Resources/), and all [Controlled Unclassified Information (CUI)](https://www.archives.gov/cui/about).

```{important}
**No External (regulated) data of any kind is supported on LCA1.** If you need to host regulated data, please contact the [Secure Research Computing team](https://www.colorado.edu/rc/secure-research-computing-resources). They run a separate platform specifically designed to handle highly-secure data.
```

## AWS LCA1 Data Classification Support

The table below outlines the level of support for the different data classifications in the AWS LCA1 landing zone.

```{list-table} LCA1 Data Support
:header-rows: 1

* - Data Classification
  - Supported on LCA1?
* - Internal - Public
  - Yes ✅
* - Internal - Confidential
  - Yes ✅
* - Internal - Highly Confidential
  - No ⛔️
* - External
  - No ⛔️
```

```{note}
Even for supported data classifications, **the LCA1 platform alone does not satisfy all required security controls** to protect that data. You must implement additional controls within your workload. Please see [Shared Responsibility Model](getting-started/shared-responsibility-model.md) for more information.
```
