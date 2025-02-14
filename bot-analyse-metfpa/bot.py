import schedule
import time
from scraper import main  # Nous allons supposer que scraper.py a une fonction `main()`

def job():
    print("Lancement du scraping...")
    main()  # Appelle la fonction de scraping

# Planifier l'exécution toutes les heures
schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
