# Projet Velou - Avrit, Prost, Revelli et Weydert

L'objectif est de prédire les tendances de remplissage des stations de VélÔ Toulouse. Pour ce faire, nous avons conçu et mis en place un pipeline ELT qui extrait les données de JCDecaux (données statiques et dynamiques) puis stocké ces données dans deux bases de données. 
Nous avont utilisé crontab pour récupérer les données dynamiques toutes les 15min et nous avons choisi PostgreSQL pour le stockage de notre base de données. 

Nous n'avons pas codé explicitement la transformation des données mais l'idée générale est expliquée dans le Compte Rendu


## Extraction  
La première étape de connection à l'API JCDecaux est codée dans le fichier *get_dynamic_data.py*. C'est l'extraction des données puis leur filtrage afin qu'elles correspondent au format de notre dictionnaire et enfin leur stockage dans un fichier JSON *dynamic_data.json*.

## Loading 
L'ajout de nos data dynamiques à la base de données se fait via le script *update_dynamic_data_velou_bd.py* . Ce script crée la table si elle n'existe pas déjà et vérifie avant l'insertion que chaque donnée n'est pas déjà existante afin de garantir l'unicité. 

L'ajout de nos data statiques à la base de données se fait via le script *update_static_data_velou_bd.py* . Ce script crée la table si elle n'existe pas déjà et vérifie avant l'insertion que chaque donnée n'est pas déjà existante afin de garantir l'unicité. 

Enfin, le fichier *update.py* execute les fichiers d'extraction et de Loading. Ce script est appelé par crontab toutes les 15mins.

LE NOM ET MDP PSQL A UTILISER SONT A RENSEIGNER DANS LE FICHIER *userVariables.py*

## Transforming - Demo

Le script *demo.py* a été réalisé pour présenter un exemple simple pour l'utilisation et la transformation des quelques datas collectées.
Pour pouvoir utiliser *demo.py* sans nécessairement récolter des datas au préalable le script *import_db.py* permet d'importer un dataset réaliser sur quatres jours du 13 au 17 octobre.



