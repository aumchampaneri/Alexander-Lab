# Microglial Complement Expression

---
## Introduction
> Add stuff here

---
## Goals
Create a map of the complement expression in microglia across *Homo sapiens* and *Mus musculus* using publically available datasets.

---
## Specifications
Use _ScanPy_ package to visualize the data exported from CellXGene as _.h5ad_ files.

- [ ] Determine if the _.h5ad_ files need to have their data points normalized prior to visualization.
  - How to normalize data? Does _ScanPy_ include commands for this?

---
## Progress
- _Homo sapien_ data exported and visualized
  - Using the Human cell atlas colletion Human brain cell atlas v01
  - Specifically looking at the Microglia Supercluster
    - Data from this was polled for a list of complement associated proteins
    - Data was then visualized using scanpy as Microglial orgin tissue vs. complement protein as a function of expression.
    - This all can be found under the _h5ad Homo Query.ipynb_ file