import pandas as pd

data = {
    'Numer ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(data)

print("Dane o pracownikach:")
print(df)

#A
pracownicy_pensja_over_5000 = df[df['Pensja'] > 5000]
print("\nPracownicy z pensją większą niż 5000 PLN:")
print(pracownicy_pensja_over_5000)

#B
pracownicy_posortowani_wiek = df.sort_values(by='Wiek')
print("\nPracownicy posortowani według wieku:")
print(pracownicy_posortowani_wiek)

#C
srednia_pensja_stanowisko = df.groupby('Stanowisko')['Pensja'].mean()
print("\nŚrednia pensja w zależności od stanowiska:")
print(srednia_pensja_stanowisko)

#D
awans_data = {
    'Numer ID': [1, 4],
    'Imię': ['Anna', 'Tomasz'],
    'Nazwisko': ['Kowalska', 'Kaczmarek'],
    'Stanowisko': ['Dyrektor', 'Konsultant Senior'],
    'Wiek': [35, 30],
    'Pensja': [10000, 8000]
}

df_awans = pd.DataFrame(awans_data)

df_polaczone = pd.merge(df, df_awans, on='Numer ID', how='outer', suffixes=('_przed', '_po'))
print("\nPracownicy przed i po awansie:")
print(df_polaczone)

#E
df.to_csv('pracownicy.csv', index=False)

#F
df_wczytane = pd.read_csv('pracownicy.csv')

print("\nWczytane dane z pliku CSV:")
print(df_wczytane)
