#!/usr/bin/env python3

from bs4 import BeautifulSoup
from colorama import init, Fore
import os
import questionary

init(autoreset=True)

def mettre_a_jour_url(fichier_html, nouvelle_url):
    try:
        with open(fichier_html, 'r', encoding='utf-8') as f:
            contenu = f.read()

        soup = BeautifulSoup(contenu, 'html.parser')

        meta_tags = soup.find_all('meta', attrs={'property': 'og:url'})

        for tag in meta_tags:
            tag['content'] = nouvelle_url

        with open(fichier_html, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print(Fore.GREEN + f"L'URL dans {fichier_html} a été mise à jour avec succès.")
    except FileNotFoundError:
        print(Fore.RED + f"Le fichier {fichier_html} n'a pas été trouvé.")

dossier_templates = "templates"
fichiers_html = [f for f in os.listdir(dossier_templates) if f.endswith(".html")]

selection = questionary.checkbox("Sélectionnez les fichiers à mettre à jour :", choices=fichiers_html).ask()

if not selection:
    print(Fore.YELLOW + "Aucun fichier sélectionné.")
else:
    nouvelle_url = input("Entrez la nouvelle URL : ")

    for fichier_html in selection:
        fichier_html_path = os.path.join(dossier_templates, fichier_html)
        mettre_a_jour_url(fichier_html_path, nouvelle_url)
