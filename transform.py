import psycopg2
import pandas as pd
import plotly.express as px
import plotly.offline as pyo

def demo():

    try:
        number = getStationNumber()
    except ValueError as e:
        print(e)
        return
    
    time = input("Pour quand souhaites-tu avoir des informations (dd/mm/yyyy hh:mm)? ")
    
    print(f"On a pas assez de data pour un faire un truc intéressant pour le momment")

    conn = psycopg2.connect(
        host="localhost",
        database="",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    # query = f"SELECT * FROM dynamic_datas WHERE number = {number};"
    # data = pd.read_sql_query(query, conn)
    cur.execute(f"""SELECT * FROM dynamic_datas WHERE number = {number};""")
    data = cur.fetchall()
    cur.close()
    conn.close()

    X = [row[5] for row in data] 
    Y = [row[3] for row in data] 

    # fig = px.scatter(data, x='last_update', y='available_bikes', title=f'Nombre de Vélouse à la station {number}')
    fig = px.scatter(x=X, y=Y, title=f'Nombre de Vélouse à la station {number}')
    fig.update_layout(xaxis_title='Date', yaxis_title='Nombre de vélos disponibles')
    fig.show()

    return None

def getStationNumber():

    conn = psycopg2.connect(
        host="localhost",
        database="",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    
    number = input("Quel est le numéro de la station ? ")

    cur.execute("""
        SELECT address FROM stations WHERE number = %s;
    """, (number,))

    address = cur.fetchone()

    if not address:
        raise ValueError("La station n'existe pas")

    cur.close()
    conn.close()

    check = input(f"C'est bien la station au {address[0]} ? ")

    if check.lower() == "oui":
        return number
    elif check.lower() == "non":
        print("Réessaye un autre numéro de station")
        return getStationNumber()
    else :
        raise ValueError("Réponse Invalide")


demo()