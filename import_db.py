import psycopg2
import userVariables as user
# Exécution de la commande avec subprocess
conn = psycopg2.connect(
    host="localhost",
    database="",
    user=user.PSQL_USER_NAME,
    password=user.PSQL_USER_PASSWORD
)

with open('backup.sql', 'r') as f:
    sql_script = f.read()

cur = conn.cursor()
cur.execute(sql_script)
conn.commit()
conn.close()

print("Base de données Veloù importée.")
