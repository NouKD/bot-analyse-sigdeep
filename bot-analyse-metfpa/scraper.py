import requests
from bs4 import BeautifulSoup
import csv

def main():
    # URL du site à analyser
    url = "https://metfpa-deep.ci/"

    # Récupérer la page
    response = requests.get(url)
    html_content = response.text

    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver tous les titres des articles
    titles = soup.find_all('h2')  # Ajustez la balise selon le contenu réel

    # Sauvegarder les titres dans un fichier CSV
    with open('titres.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titre"])
        for title in titles:
            writer.writerow([title.text])

    print("Scraping terminé et données sauvegardées dans 'titres.csv'.")
