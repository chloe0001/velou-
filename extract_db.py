import subprocess
import userVariables as user

subprocess.run([f"pg_dump",
                f"--dbname=postgresql://{user.PSQL_USER_NAME}:{user.PSQL_USER_PASSWORD}@localhost:5432/postgres",
                f"--file=backup.sql",
                "--inserts"])

print("Base de données exportée dans 'backup.sql'.")
