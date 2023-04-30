import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('gene.csv')

# Count the number of markers on each chromosome
chromosome_counts = df['Chromosome'].value_counts().reset_index()
chromosome_counts.columns = ['Chromosome', 'Gene Count']

# Count the number of each Type on each chromosome
type_counts = df.groupby(['Chromosome', 'Type']).size().unstack(fill_value=0).reset_index()

# Export the results as a new CSV file
results = pd.merge(chromosome_counts, type_counts, on='Chromosome', how='left')
results.to_csv('results.csv', index=False)
