# Project Indexing with Solr

Ce projet est une application web développée en Python avec Flask pour la gestion des fichiers et l'indexation dans Apache Solr. L'objectif principal est de permettre aux utilisateurs d'uploader des fichiers, extraire leur contenu textuel, et les indexer dans Solr pour permettre des recherches efficaces.

## Fonctionnalités

- **Upload de fichiers :** Les utilisateurs peuvent uploader des fichiers au format PDF, DOC et DOCX.
- **Indexation dans Solr :** Les fichiers uploadés sont indexés dans Solr pour la recherche.
- **Recherche de fichiers :** Les utilisateurs peuvent effectuer des recherches par mots-clés dans le contenu des fichiers indexés.
- **Extraction de Texte :** Le contenu textuel des fichiers est extrait à l'aide d'Apache Tika, permettant une recherche efficace dans le texte des documents.
  
## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

- Python (version 3.6 ou supérieure)
- Flask (`pip install Flask`)
- Apache Solr (avec un core nommé `project`)

## Installation et Configuration

1. Clonez ce dépôt : `git clone https://github.com/votre-utilisateur/nom-du-projet.git`
2. Installez les dépendances : `pip install -r requirements.txt`
3. Configurez l'URL Solr dans `app.py` : `SOLR_URL = 'http://localhost:8983/solr/project'`

## Utilisation

1. Lancez l'application : `python app.py`
2. Accédez à l'URL : `http://localhost:5000` dans votre navigateur.

## Utilisation de Tika

Ce projet utilise Apache Tika pour extraire le texte des fichiers uploadés. Tika est une bibliothèque Java qui prend en charge de nombreux formats de fichiers, y compris les fichiers PDF, DOC et DOCX, et qui peut extraire le contenu textuel de ces fichiers de manière efficace.

### Installation de Tika

Pour utiliser Tika avec ce projet, suivez ces étapes :

1. Téléchargez le fichier JAR de Tika depuis le site officiel.
2. Placez le fichier JAR téléchargé dans un dossier de votre choix dans le projet, par exemple `libs/`.
3. Ajoutez le chemin du fichier JAR de Tika dans le script Python `app.py`, en utilisant la variable `TIKA_PATH` :

   ```python
   TIKA_PATH = 'chemin/vers/tika-app.jar'
