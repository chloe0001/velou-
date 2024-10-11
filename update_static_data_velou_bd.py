""" Script qui upload nos données statiques dans la base de données
"""
import psycopg2
import json

def update_static_data_velou_bd():
    # Charger le fichier JSON
    with open('static_data.json', 'r') as f:
        data = json.load(f)  # data est maintenant un dictionnaire Python


    # Connexion à la base de données
    conn = psycopg2.connect(
        host="localhost",
        database="",
        user="postgres",
        password="postgres"
    )

    # Créer un curseur pour exécuter des commandes SQL
    cur = conn.cursor()
    
    # Création de la table si elle n'existe pas déjà
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            number INT,
            name TEXT,
            address TEXT,
            latitude FLOAT,
            longitude FLOAT
        );
    """)

    conn.commit()  # Valider la création de la table

    # Ajout des données à la base de données si elles n'y sont pas déjà 
    for record in data:
        cur.execute("""SELECT COUNT(*) FROM stations WHERE number = %s """,(record['number'],) )
        exists = cur.fetchone()

        if (exists[0] == 0):
            cur.execute("""
                INSERT INTO stations (number, name, address, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s)
            """, (record['number'], record['name'], record['address'], record['latitude'], record['longitude']))

    conn.commit()  # Valider les insertions

    cur.close()
    conn.close()
    return

