import pandas as pd

chunks = []

# Read the CSV in chunks
for chunk in pd.read_csv('operable.csv', delimiter=',', encoding='utf-8',chunksize=100000):
    chunks.append(chunk)

# Concatenate all chunks into a single DataFrame
df = pd.concat(chunks, ignore_index=True)

# Check the DataFrame
print(f"El tamaño del dataframe es {df.shape} ")