import psycopg2
import json

def update_static_data_velou_bd():
    # Charger le fichier JSON
    with open('toulouse.json', 'r') as f:
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

    cur.execute("""
        DROP TABLE IF EXISTS stations;
    """)

    conn.commit()

    cur.execute("""
        CREATE TABLE stations (
            number INT,
            name TEXT,
            address TEXT,
            latitude FLOAT,
            longitude FLOAT
        );
    """)

    conn.commit()  # Valider la création de la table

    for record in data:
        cur.execute("""
            INSERT INTO stations (number, name, address, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s)
        """, (record['number'], record['name'], record['address'], record['latitude'], record['longitude']))

    conn.commit()  # Valider les insertions

    cur.close()
    conn.close()
    return

update_static_data_velou_bd()