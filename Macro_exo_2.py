import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# On charge la base
df_matches = pd.read_csv("WorldCupMatches.csv")
df_players = pd.read_csv("WorldCupPlayers.csv")

# ON enleve les doublons
df_matches = df_matches.drop_duplicates()
df_players = df_players.drop_duplicates()

# 1. Chargement des données
# On charge le fichier des matchs
df_matches = pd.read_csv('WorldCupMatches.csv')

# 2. Nettoyage des données
# La colonne 'Attendance' (Spectateurs) peut contenir des valeurs vides (NaN).
# On supprime les lignes où l'affluence est manquante.
df_matches = df_matches.dropna(subset=['Attendance'])

# 3. Création de l'histogramme
plt.figure(figsize=(10, 6))

# On utilise histplot de Seaborn (plus moderne et esthétique)
# kde=True ajoute la courbe de densité pour mieux voir la distribution
sns.histplot(df_matches['Attendance'], kde=True, bins=30, color='skyblue')

# 4. Titres et labels
plt.title('Distribution du nombre de spectateurs par match (Coupe du Monde)')
plt.xlabel('Nombre de spectateurs')
plt.ylabel('Nombre de matchs (Fréquence)')

# 5. Affichage

plt.show()
