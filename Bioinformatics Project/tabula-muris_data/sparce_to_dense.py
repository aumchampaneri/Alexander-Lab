# Converted Bash Sparce to Dense Matrix Conversion script using chatGPT
# This is the resultant script

# TODO
# Need to add a way to direct to easily call out which files are being converted
# Import the "raw_data-path.py" and use that for the file paths

# import the necessary libraries
import pandas as pd

# import file paths for the raw data
# Liver-10X_P4_2 ---- DROPLET

def liver_p42_barcodes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/barcodes.tsv"
def liver_p42_genes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/genes.tsv"
def liver_p42_matrix():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/matrix.mtx"


# assign file names to variables
barcodes_file = liver_p42_barcodes()
genes_file = liver_p42_genes()
matrix_file = liver_p42_matrix()

# Step 1: Read barcodes.tsv and genes.tsv, add line numbers, and save as CSV
# This section reads the barcodes and genes files, assigns line numbers to each entry,
# and saves the results to intermediate CSV files.
barcodes = pd.read_csv(barcodes_file, sep="\t", header=None, names=["Barcode"])
barcodes.index += 1  # Line numbers start from 1
barcodes["LineNumber"] = barcodes.index
numbered_barcodes = barcodes[["LineNumber", "Barcode"]]
numbered_barcodes.to_csv("numbered_barcodes.csv", index=False)

genes = pd.read_csv(genes_file, sep="\t", header=None, names=["GeneID", "GeneName"])
genes.index += 1
genes["LineNumber"] = genes.index
numbered_genes = genes[["LineNumber", "GeneID", "GeneName"]]
numbered_genes.to_csv("numbered_genes.csv", index=False)

# Step 2: Process matrix.mtx to sort by gene and barcode
# This section reads the matrix file, skips the header lines, and sorts the data
# by gene and barcode, saving the sorted results to intermediate CSV files.
matrix = pd.read_csv(matrix_file, sep=" ", skiprows=3, header=None, names=["Gene", "Barcode", "Value"])
gene_sorted_matrix = matrix.sort_values(by=["Gene"])
gene_sorted_matrix.to_csv("gene_sorted_matrix.csv", index=False)

barcode_sorted_matrix = matrix.sort_values(by=["Barcode"])
barcode_sorted_matrix.to_csv("barcode_sorted_matrix.csv", index=False)

# Step 3: Replace line numbers with barcodes and genes
# This section replaces the gene and barcode line numbers in the sorted matrix
# with the corresponding gene IDs, gene names, and barcodes. The final result
# is saved to a CSV file.
gene_joined = pd.merge(numbered_genes, gene_sorted_matrix, left_on="LineNumber", right_on="Gene")
gene_joined = gene_joined[["GeneID", "GeneName", "Barcode", "Value"]]

gene_joined_sorted = gene_joined.sort_values(by=["Barcode"])
final_matrix = pd.merge(numbered_barcodes, gene_joined_sorted, left_on="LineNumber", right_on="Barcode")
final_matrix = final_matrix[["Barcode_y", "GeneID", "GeneName", "Value"]]
final_matrix.columns = ["Barcode", "GeneID", "GeneName", "Value"]
final_matrix.to_csv("final_matrix.csv", index=False)

# Step 4: Clean up temporary files
# This section removes the intermediate temporary files created during processing.
import os
os.remove("numbered_barcodes.csv")
os.remove("numbered_genes.csv")
os.remove("gene_sorted_matrix.csv")
os.remove("barcode_sorted_matrix.csv")
