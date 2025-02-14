# Bot Python pour récupérer et analyser des données depuis metfpa-deep.ci

## Description

Ce projet vise à créer un bot Python qui récupère et analyse des données depuis le site [metfpa-deep.ci](http://metfpa-deep.ci). Le bot automatise l'extraction des informations et permet de réaliser des analyses adaptées aux besoins spécifiques du projet.

## Fonctionnalités

- Récupération des données depuis le site metfpa-deep.ci.
- Analyse et traitement des données extraites (filtrage, agrégation, etc.).
- Export des résultats sous format CSV ou JSON.
- Personnalisation du bot pour récupérer des informations spécifiques selon les besoins.

## Prérequis

Avant de commencer, assurez-vous que Python 3.x est installé sur votre machine ainsi que les bibliothèques suivantes :

- `requests` : Pour effectuer des requêtes HTTP et récupérer les pages web.
- `beautifulsoup4` : Pour analyser le contenu HTML des pages web.
- `pandas` : Pour traiter les données et les exporter sous différents formats.
- `json` : Pour exporter les résultats sous format JSON.

Vous pouvez installer les dépendances nécessaires avec la commande suivante :

```bash
pip install -r requirements.txt
