"""Script qui insert les données d'un fichier JSON dans la table SQL dynamic_datas. 
"""

import psycopg2
import json
from datetime import datetime
import userVariables as user

def update_dynamic_data_velou_bd():
    # Charger le fichier JSON
    with open('dynamic_data.json', 'r') as f:
        data = json.load(f)  # data est maintenant un dictionnaire Python


    # Connexion à la base de données
    conn = psycopg2.connect(
        host="localhost",
        database="Velou",
        user=user.PSQL_USER_NAME,
        password=user.PSQL_USER_PASSWORD
    )

    # Créer un curseur pour exécuter des commandes SQL
    cur = conn.cursor()
    
    # Création de la table si elle n'existe pas déjà 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dynamic_datas (
            number INT,
            bike_stands INT,
            available_bike_stands INT,
            available_bikes INT,
            status TEXT,
            last_update TEXT
        );
    """)

    conn.commit()

    #Insertion des données dans la BDD si et seulement si elles n'existent pas déjà 
    for record in data:
        ts = record['last_update']
        if ts is None:
            time = 'Invalid'
        else:
            time = datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')

        cur.execute("""SELECT COUNT(*) FROM dynamic_datas WHERE number = %s AND last_update = %s """, (record['number'] , time))

        exists = cur.fetchone()

        if (exists[0] == 0):
            cur.execute("""
                INSERT INTO dynamic_datas ( number, bike_stands, available_bike_stands, available_bikes, status, last_update)
                VALUES (%s, %s, %s, %s, %s, %s) 
            """, ( record['number'], record['bike_stands'], record['available_bike_stands'], record['available_bikes'], record['status'], time))
    conn.commit()  # Valider les insertions

    cur.close()
    conn.close()
    return
