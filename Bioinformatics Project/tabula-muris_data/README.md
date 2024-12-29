# Tabula-Muris Dataset Analysis

## Goals
1. Use the Tabula-Muris dataset to map the expression of various complement genes across different cell types
2. Use the methods from this project to analyze larger datasets

## Current Problems
- Data is stored in a format which is not easily accessible
  - Must be converted to a format which can be parsed using python
    - Three files must be converted: barcodes.tsv, genes.tsv, and matrix.mtx into a single .csv file
    - The data is stored in a sparse matrix format, which must be converted to a dense matrix format
  - Resultant file will be very large, and may not be able to be stored in memory
    - May need to use a database to store the data instead (SQL?)
- Once the data is in a usable format, we can begin to filter for complement genes and analyze the data
  - At this point, we can begin to use the data to map the expression of complement genes across different cell types

## Current Objective
- [x] Convert the CellRanger outfiles (.mtx, .tsv, .csv) into a single .csv file
- [x] Convert the sparse matrix into a dense matrix
- [ ] Check the validity of the converted file
  - Make sure the data is correct post conversion

### Notes:
 - The data is downloaded from the Tabula-Muris figshare page https://figshare.com/projects/Tabula_Muris_Transcriptomic_characterization_of_20_organs_and_tissues_from_Mus_musculus_at_single_cell_resolution/27733



## Scripts
### raw_data-path.py
- This script defines all the raw data paths and creates a variable to call for instead of typing the path each time
- Also contains a script to check the file paths and make sure they are correct

### sparse_to_dense.py
- This script converts the sparse matrix into a dense matrix
- Used a bash shell script which was then converted to python using ChatGPT
- Script worked; not sure if the conversion of the files was valid yet

# References
 - Use the following link as a reference for the shell commands to convert the three (.mtx and .tsv) files to a single .csv file
	- https://kb.10xgenomics.com/hc/en-us/articles/360006779712-How-can-I-convert-the-gene-barcode-matrix-from-Cell-Ranger-1-x-and-2-x-to-a-CSV-file
	- Not sure if this will work yet
