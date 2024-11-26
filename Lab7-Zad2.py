import pandas as pd

df = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])

print(df.head())

kraj_max_przyrost = df['Przyrost_ludnosci_2022'].idxmax()
kraj = df.loc[kraj_max_przyrost, 'Kraj']

print(f"Kraj z największym przyrostem ludności w 2022 roku to: {kraj}")
