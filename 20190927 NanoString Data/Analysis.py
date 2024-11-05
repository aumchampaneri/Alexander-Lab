import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/Users/admin/Alexander-Lab/20190927 NanoString Data/Noramalized-data-counts.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(data.head())

# Calculate the average of the data in three columns
columns_to_average = ['20190927_RQ-016723_Control-K-1_07.RCC', '20190927_RQ-016723_Control-K-2_08.RCC', '20190927_RQ-016723_Control-K-3_09.RCC']
data['Average'] = data[columns_to_average].mean(axis=1)

# Display the first few rows of the DataFrame with the new 'Average' column
print(data.head())