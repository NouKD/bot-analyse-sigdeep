import requests
from bs4 import BeautifulSoup
import csv

def main():
    # URL de la page des annonces de bourses
    url = "https://formation-professionnelle.gouv.ci/?page_id=376"

    # Récupérer la page
    response = requests.get(url)
    html_content = response.text

    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver toutes les annonces liées aux bourses
    # Inspectez le HTML pour trouver le bon sélecteur CSS, ici on suppose qu'il y a des liens dans des balises <a> avec une classe spécifique
    annonces = soup.find_all('a', class_='entry-title')  # Ajustez cette classe en fonction de la structure réelle du site

    # Sauvegarder les données dans un fichier CSV
    with open('bourses.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titre", "Lien"])
        for annonce in annonces:
            titre = annonce.text.strip()  # Récupérer le titre de l'annonce
            lien = annonce['href']  # Récupérer le lien vers la page de l'annonce
            writer.writerow([titre, lien])

    print("Scraping terminé et données sauvegardées dans 'bourses.csv'.")

