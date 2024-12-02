import pandas as pd

df = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])


kraj_max_przyrost = df['2022'].idxmax()
kraj = df.loc[kraj_max_przyrost, 'KRAJE']

print(f"Kraj z największym przyrostem ludności w 2022 roku to: {kraj}")

