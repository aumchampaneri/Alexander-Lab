import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
import seaborn as sns



#Load the CSV file into a DataFrame
file_path = '/Users/aumchampaneri/PycharmProjects/Alexander-Lab/20190927 NanoString Data/Normalized-data-counts.csv'
raw_data = pd.read_csv(file_path)


# Print the first 5 rows of the DataFrame
# print(raw_data.head())


#Extract the columns corresponding to the kidney samples
kidney_columns =['Probe Name', '20190927_RQ-016723_Control-K-1_07.RCC', '20190927_RQ-016723_Control-K-2_08.RCC', '20190927_RQ-016723_Control-K-3_09.RCC', '20190927_RQ-016723_FHKO-K-1_10.RCC', '20190927_RQ-016723_FHKO-K-2_11.RCC', '20190927_RQ-016723_FHKO-K-3_12.RCC']

#Extract the kidney data into a new DataFrame
kidney_data = raw_data[kidney_columns]

# Print the first 5 rows of the kidney data DataFrame
# print(kidney_data.head())



#Get rid of rows 0 and 1 -- Contains no data
kidney_data = kidney_data.drop([0, 1])

#Rename the 'Probe Name' column to 'Gene'
kidney_data = kidney_data.rename(columns = {'Probe Name':'Gene'})

#Rename the columns to remove the long file names
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_Control-K-1_07.RCC':'Control 1'})
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_Control-K-2_08.RCC':'Control 2'})
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_Control-K-3_09.RCC':'Control 3'})
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_FHKO-K-1_10.RCC':'FHKO 1'})
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_FHKO-K-2_11.RCC':'FHKO 2'})
kidney_data = kidney_data.rename(columns = {'20190927_RQ-016723_FHKO-K-3_12.RCC':'FHKO 3'})

#Reset the index of the DataFrame
kidney_data = kidney_data.reset_index(drop = True)

# Data is now cleaned and ready for analysis
# print(kidney_data.head())


#Change the data type of the columns to numeric
kidney_data['Control 1'] = pd.to_numeric(kidney_data['Control 1'])
kidney_data['Control 2'] = pd.to_numeric(kidney_data['Control 2'])
kidney_data['Control 3'] = pd.to_numeric(kidney_data['Control 3'])
kidney_data['FHKO 1'] = pd.to_numeric(kidney_data['FHKO 1'])
kidney_data['FHKO 2'] = pd.to_numeric(kidney_data['FHKO 2'])
kidney_data['FHKO 3'] = pd.to_numeric(kidney_data['FHKO 3'])

# Date types of the columns are fixed

# #Get the data types of the columns
# print(kidney_data.dtypes)

# Standard NanoString Analysis
# - Average of the Control and FHKO samples
# - Standard deviation of the Control and FHKO samples
# - Fold change of the FHKO samples compared to the Control samples
# - Log2 fold change of the FHKO samples compared to the Control samples
# - P - value of the FHKO samples compared to the Control samples
# - Adjusted p - value using the Benjamini - Hochberg procedure


#Calculate the mean of the FHKO and Control samples
kidney_data['Control Mean'] = kidney_data[['Control 1', 'Control 2', 'Control 3']].mean(axis = 1)
kidney_data['FHKO Mean'] = kidney_data[['FHKO 1', 'FHKO 2', 'FHKO 3']].mean(axis = 1)

#Calculate the standard deviation of the FHKO and Control samples
kidney_data['Control STD'] = kidney_data[['Control 1', 'Control 2', 'Control 3']].std(axis = 1)
kidney_data['FHKO STD'] = kidney_data[['FHKO 1', 'FHKO 2', 'FHKO 3']].std(axis = 1)

#Calculate the fold change of the FHKO samples compared to the Control samples
kidney_data['Fold Change'] = kidney_data['FHKO Mean'] / kidney_data['Control Mean']

#Calculate the log2 fold change of the FHKO samples compared to the Control samples
kidney_data['Log2 Fold Change'] = np.log2(kidney_data['Fold Change'])

#Calculate the p-value of the FHKO samples compared to the Control samples
kidney_data['P-Value'] = ttest_ind(kidney_data[['Control 1', 'Control 2', 'Control 3']], kidney_data[['FHKO 1', 'FHKO 2', 'FHKO 3']], axis = 1)[1]

#Calculate the adjusted p-value using the Benjamini-Hochberg procedure
kidney_data['Adjusted P-Value'] = multipletests(kidney_data['P-Value'], method = 'fdr_bh')[1]

# Isolate the Calculated Data
# New DataFrame containing only the gene names and the calculated data
# Sorted by log2 fold change and then filtered to only include genes with a p - value less than 0.05

#Create a new data frame with the new columns and the gene column
kidney_analysis_data = kidney_data[['Gene', 'Control Mean', 'FHKO Mean', 'Control STD', 'FHKO STD', 'Fold Change', 'Log2 Fold Change', 'P-Value', 'Adjusted P-Value']]

#Sort the kidney_analysis_data by the log2 fold change
kidney_analysis_data = kidney_analysis_data.sort_values(by = 'Log2 Fold Change', ascending = False)

#Remove any rows with p values greater than 0.05
kidney_analysis_data = kidney_analysis_data[kidney_analysis_data['P-Value'] < 0.05]

#Reset the index of the DataFrame
kidney_analysis_data = kidney_analysis_data.reset_index(drop = True)

# Ready to use the kidney_analysis_data DataFrame for visualization
# Dataframe only contains the significant genes (where the gene meets the 95% confidence interval) and is sorted (Log 2 Change) and reindexed

############# DEFINE CRITERIA FOR SIGNIFICANT GENES #############

# Filtered Data to only significant genes
# - Genes within the 95% confidence interval and with a log2 fold change greater than 0.585 (1.5-fold change)
significant_genes = kidney_data[(kidney_data['P-Value'] < 0.05) & (np.abs(kidney_data['Log2 Fold Change']) > 0.585)]

############# HEAT MAP #############

# Generate heatmap label the y-axis with the gene names
heatmap_data = significant_genes[['Gene', 'Control 1', 'Control 2', 'Control 3', 'FHKO 1', 'FHKO 2', 'FHKO 3']]
# use column 'Gene' as index for the heatmap data
heatmap_data = heatmap_data.set_index('Gene')
sns.clustermap(heatmap_data,
               standard_scale=0,
               figsize=(4, 10),
               dendrogram_ratio=(0.1, 0.1),
               cmap='seismic',
               yticklabels=True,
               col_cluster=True,
               cbar_pos=(0.905, .065, .015, .35)
               )
plt.show()


############# VOLCANO PLOT #############

#Create a volcano plot of the log2 fold change vs. the -log10 of the p-value
plt.figure(figsize = (8, 6))
plt.xlabel('Log2 Fold Change')
plt.ylabel('-log10(P-Value)')
plt.title('Volcano Plot of Kidney Samples')
plt.axvline(x = 0, color = 'black', linestyle = '--')
plt.axhline(y = -np.log10(0.05), color = 'black', linestyle = '--')
#Color/plot the points using the adjusted p-value
plt.scatter(kidney_analysis_data['Log2 Fold Change'], -np.log10(kidney_analysis_data['P-Value']), c = kidney_analysis_data['Adjusted P-Value'], cmap = 'coolwarm', s = 10)
plt.colorbar(label = 'Benjamini-Hochberg Adjusted P-Value')
# use the annotate function to add the gene names which exist in the significant genes dataframe
for i in range(len(significant_genes)):
    plt.annotate(significant_genes['Gene'].iloc[i], (significant_genes['Log2 Fold Change'].iloc[i], -np.log10(significant_genes['P-Value'].iloc[i])),
                 textcoords='offset points',
                 xytext=(1.5,3)
                 )
plt.show()







