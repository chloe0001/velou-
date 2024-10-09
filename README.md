# Projet Velou - Avrit, Prost, Revelli et Weydert

L'objectif est de prédire les tendances de remplissage des stations de VélÔ Toulouse. Pour ce faire, nous avons conçu et mis en place un pipeline ELT qui extrait les données de JCDecaux (données statiques et dynamiques) puis stocké ces données dans deux bases de données. 
Nous avont utilisé crontab pour récupérer les données dynamiques toutes les 15min et nous avons choisi PostgreSQL pour le stockage de notre base de données. 

Nous n'avons pas codé explicitement la transformation des données mais l'idée générale est expliquée dans le Compte Rendu


## Explications des fichiers 
La première étape de connection à l'API JCDecaux est codée dans le fichier *get_dynamic_data.py*. C'est l'extraction des données puis leur filtrage afin qu'elles correspondent au format de notre dictionnaire et enfin leur stockage dans un fichier JSON *dynamic_data.json*.




BDD 

Passage des .json créés en BDD PostgreSQL à l'aide de python et de l'outil psycopg2.
La BDD est divisée en 2 tables: "stations" (statique) et "dynamic_data" (dynamique).


Pour planifier une tache récurrente on va utiliser crontab. Cf message SLACK de christophe -> pour Typiquement, planifier une tâche qui se lance à chaque heure à 15 minutes, ça s'écrit:
15 * * * * 

ici : je vais dans conda puis velou. J'ai rendu mon script executable (avec la première ligne et le chmo +xà et maintenant je oeux faire crontab -e puis écrire : 15 * * * * python api_JCdecaux.py dans le vim qui s'ouvre. Puis apparemment faut accepter et la c'ezst bon ça executera toutes les 15min. 
vérifier les taches : faire crontab -l  
