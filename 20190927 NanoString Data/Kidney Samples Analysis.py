from matplotlib import axis
import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/Users/admin/Alexander-Lab/20190927 NanoString Data/Noramalized-data-counts.csv'
raw_data = pd.read_csv(file_path)


""" #Print the first 5 rows of the DataFrame
print(raw_data.head())
"""

# Extract the columns corresponding to the kidney samples
kidney_columns = ['Probe Name', '20190927_RQ-016723_Control-K-1_07.RCC', '20190927_RQ-016723_Control-K-2_08.RCC', '20190927_RQ-016723_Control-K-3_09.RCC', '20190927_RQ-016723_FHKO-K-1_10.RCC', '20190927_RQ-016723_FHKO-K-2_11.RCC', '20190927_RQ-016723_FHKO-K-2_11.RCC']

# Extract the kidney data into a new DataFrame
kidney_data = raw_data[kidney_columns]

""" # Print the first 5 rows of the kidney data DataFrame
print(kidney_data.head())
"""

