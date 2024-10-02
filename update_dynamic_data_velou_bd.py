import psycopg2
import json
from datetime import datetime

def update_dynamic_data_velou_bd():
    # Charger le fichier JSON
    with open('data_dynamique.json', 'r') as f:
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
        DROP TABLE IF EXISTS dynamic_datas;
    """)

    conn.commit()


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

    for record in data:
        ts = record['last_update']
        if ts is None:
            time = 'Invalid'
        else:
            time = datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')
            
        cur.execute("""
            INSERT INTO dynamic_datas ( number, bike_stands, available_bike_stands, available_bikes, status, last_update)
            VALUES ( %s, %s, %s, %s, %s, %s)
        """, ( record['number'], record['bike_stands'], record['available_bike_stands'], record['available_bikes'], record['status'], time))

    conn.commit()  # Valider les insertions

    cur.close()
    conn.close()
    return

update_dynamic_data_velou_bd()
