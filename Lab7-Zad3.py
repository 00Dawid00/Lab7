import pandas as pd

dane = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])

dane_bez_kraj = dane.drop(columns=['KRAJE'])

maks_przyrost = dane_bez_kraj.max().max()

rok_maks_przyrost = dane_bez_kraj.max().idxmax()

indeks_maks_przyrost = dane_bez_kraj[rok_maks_przyrost].idxmax()
kraj_maks_przyrost = dane.loc[indeks_maks_przyrost, 'KRAJE']

print(f"Największy przyrost ludności wynosi {maks_przyrost} i wystąpił w roku {rok_maks_przyrost}.")
print(f"Kraj, który miał największy przyrost w tym roku, to: {kraj_maks_przyrost}.")

