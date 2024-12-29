# Define raw data paths for Tabula Muris data to be used in other scripts
# Prevents errors related to finding files
# Centralizes file paths for easy access and modification
import os

"""
Usage:
Change the file paths to the location of the raw data on your local machine
Then run to check if the paths are correct

Then for any file using these paths, import the file and use the function to get the path
This is achieved by:
    import raw_data_path 
    
    OR 
    
    from raw_data_path import liver_p42_barcodes, liver_p42_genes, liver_p42_matrix
"""




# Liver-10X_P4_2 ---- DROPLET

def liver_p42_barcodes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/barcodes.tsv"
def liver_p42_genes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/genes.tsv"
def liver_p42_matrix():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P4_2/matrix.mtx"

# Liver-10X_P7_0 ---- DROPLET

def liver_p70_barcodes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_0/barcodes.tsv"
def liver_p70_genes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_0/genes.tsv"
def liver_p70_matrix():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_0/matrix.mtx"

# Liver-10X_P7_1 ---- DROPLET

def liver_p71_barcodes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_1/barcodes.tsv"
def liver_p71_genes():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_1/genes.tsv"
def liver_p71_matrix():
    return "/Users/aumchampaneri/Tabula-Muris Data/5968960/droplet/Liver-10X_P7_1/matrix.mtx"




#### Check if the paths are correct function ####

def check_paths(file_path):
    """
    Check if the paths are correct

    Args:
    file_paths (str): The file path to check

    Returns:
    bool: True if the file path is correct and readable, False otherwise
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)

file_paths = [
    liver_p42_barcodes(), liver_p42_genes(), liver_p42_matrix(),
    liver_p70_barcodes(), liver_p70_genes(), liver_p70_matrix(),
    liver_p71_barcodes(), liver_p71_genes(), liver_p71_matrix(),
            ]
for path in file_paths:
    if check_paths(path):
        print(f"{path} is correct")
    else:
        print(f"{path} is incorrect")