from Bio import SeqIO
import numpy as np
import pandas as pd
import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from collections import Counter
from sklearn import model_selection, linear_model
import requests

# data_path = 'https://drive.google.com/uc?id=1f1CtRwSohB7uaAypn8iA4oqdXlD_xXL1'
def download_file(url, output_path):
    response = requests.get(url, stream=True)
    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

# URL of the file to download
file_url = 'https://storage.googleapis.com/inspirit-ai-data-bucket-1/Data/AI%20Scholars/Sessions%206%20-%2010%20(Projects)/Project%20-%20DNA%20Detectives/SARS_CoV_2_sequences_global.fasta'

# Output path where the file will be saved
output_path = 'SARS_CoV_2_sequences_global.fasta'

# Download the file
download_file(file_url, output_path)
cov2_sequences = 'SARS_CoV_2_sequences_global.fasta'

sequences = [r for r in SeqIO.parse(cov2_sequences, 'fasta')]

n_bases_in_seq = len(sequences[0])
columns = {}

# Iterate though all positions in this sequence.
for location in range(n_bases_in_seq): # tqdm is a nice library that prints our progress.
  bases_at_location = np.array([s[location] for s in sequences])
  # If there are no mutations at this position, move on.
  if len(set(bases_at_location))==1: continue
  for base in ['A', 'T', 'G', 'C', '-']:
    feature_values = (bases_at_location==base)

    # Set the values of any base that equals 'N' to np.nan.
    feature_values[bases_at_location==['N']] = np.nan

    # Convert from T/F to 0/1.
    feature_values  = feature_values*1

    # Make the column name look like <location>_<base> (1_A, 2_G, 3_A, etc.)
    column_name = str(location) + '_' + base

    # Add column to dict
    columns[column_name] = feature_values


mutation_df = pd.DataFrame(columns)
original_sequence = mutation_df.iloc[0]
st.write(original_sequence)

country = "USA" #@param dict_keys(['China', 'Kazakhstan', 'India', 'Sri Lanka', 'Taiwan', 'Hong Kong', 'Viet Nam', 'Thailand', 'Nepal', 'Israel', 'South Korea', 'Iran', 'Pakistan', 'Turkey', 'Australia', 'USA']
countries = [(s.description).split('|')[-1] for s in sequences]

countries_to_regions_dict = {
         'Australia': 'Oceania',
         'China': 'Asia',
         'Hong Kong': 'Asia',
         'India': 'Asia',
         'Nepal': 'Asia',
         'South Korea': 'Asia',
         'Sri Lanka': 'Asia',
         'Taiwan': 'Asia',
         'Thailand': 'Asia',
         'USA': 'North America',
         'Viet Nam': 'Asia'
}

regions = [countries_to_regions_dict[c] if c in
           countries_to_regions_dict else 'NA' for c in countries]
mutation_df['label'] = regions

balanced_df = mutation_df.copy()
balanced_df['label'] = regions
balanced_df = balanced_df[balanced_df.label!='NA']
balanced_df = balanced_df.drop_duplicates()
samples_north_america = balanced_df[balanced_df.label=='North America']
samples_oceania = balanced_df[balanced_df.label=='Oceania']
samples_asia = balanced_df[balanced_df.label=='Asia']

# Number of samples we will use from each region.
n = min(len(samples_north_america),
        len(samples_oceania),
        len(samples_asia))

balanced_df = pd.concat([samples_north_america[:n],
                    samples_asia[:n],
                    samples_oceania[:n]])

X = balanced_df.drop('label', axis=1)
Y = balanced_df.label
data = "Y (label)" 
start = 1 
stop =  10

if start>=stop:print("Start must be < stop!")
else:
  if data=='X (features)':
    print(X.iloc[start:stop])
  if data=='Y (label)':
    print(Y[start:stop])

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

lm = linear_model.LogisticRegression(
    multi_class="multinomial", max_iter=1000,
    fit_intercept=False, tol=0.001, solver='saga', random_state=42)

# Split into training/testing set.
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size = 0.2)

# Train/fit model.
lm.fit(X_train, y_train)
