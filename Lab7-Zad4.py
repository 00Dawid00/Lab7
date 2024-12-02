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


