import pandas as pd

# Charger les données à partir du fichier CSV
data = pd.read_csv('titres.csv')

# Afficher les premières lignes des données
print(data.head())

# Analyser les données (par exemple, compter le nombre d'articles)
print(f"Nombre d'articles : {len(data)}")
