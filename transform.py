import psycopg2
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

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
    cur.execute(f"""SELECT last_update, available_bikes FROM dynamic_datas WHERE number = {number};""")
    data = cur.fetchall()
    cur.close()
    conn.close()

    X = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").hour for row in data] 
    Y = [row[1] for row in data]
    

    df = pd.DataFrame({'hour':X,'AB':Y})
    df = df.groupby('hour')['AB'].mean().reset_index()
    print(df)
 
    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Affluence',
        x=df['hour'],
        y=round(df['AB']),
        marker=dict(
            color='lightblue',
            line=dict(color='blue', width=1.5)
        )
    ))

    fig.update_layout(
        title=f"Graphique d'affluence de la station {number}",
        template='plotly_white',
    )

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