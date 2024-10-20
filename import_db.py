import psycopg2
import userVariables as user
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Exécution de la commande avec subprocess
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user=user.PSQL_USER_NAME,
    password=user.PSQL_USER_PASSWORD
)

# Définir le niveau d'isolation pour empêcher une transaction
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Créer un curseur pour exécuter des commandes SQL
cur = conn.cursor()

# Créer la base de données 'Velou'
try:
    cur.execute('CREATE DATABASE velou;')
    print("Base de données 'velou' créée avec succès.")
except psycopg2.errors.DuplicateDatabase:
    print("La base de données 'velou' existe déjà.")

# Fermer le curseur et la connexion
cur.close()
conn.close()

conn = psycopg2.connect(
    host="localhost",
    database="velou",
    user=user.PSQL_USER_NAME,
    password=user.PSQL_USER_PASSWORD
)
cur = conn.cursor()

with open('backup.sql', 'r') as f:
    sql_script = f.read()

cur.execute(sql_script)
conn.commit()
conn.close()

print("Base de données 'Velou' importée.")
