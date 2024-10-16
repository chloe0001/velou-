import dash
from dash import dcc, html, Input, Output
import psycopg2
import pandas as pd
import dash_leaflet as dl
import dash_leaflet.express as dlx
import plotly.express as px

# Charger les données des stations de vélos
# Assurez-vous que votre fichier CSV contient les colonnes 'latitude', 'longitude', 'nom_station', et 'valeur'

conn = psycopg2.connect(
    host="localhost",
    database="",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()
cur.execute(f"""SELECT
    stations.number,
    stations.longitude,
    stations.latitude,
    EXTRACT(HOUR FROM TO_TIMESTAMP(dynamic_datas.last_update, 'YYYY-MM-DD HH24:MI:SS' )) AS heure,
    AVG(dynamic_datas.available_bikes) AS nb_velos_moyen
FROM
    stations
JOIN
    dynamic_datas ON dynamic_datas.number = stations.number
GROUP BY
    stations.number, heure, stations.longitude, stations.latitude
ORDER BY
    stations.number, heure;""")
response = cur.fetchall()
cur.close()
conn.close()

Num = [row[0] for row in response]
Lon = [row[1] for row in response]
Lat = [row[2] for row in response]
Hou = [row[3] for row in response]
Ava = [row[4] for row in response]

data = pd.DataFrame({'number':Num,
                     'longitude':Lon,
                     'latitude':Lat,
                     'hour':Hou,
                     'available':Ava})

# Initialise l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='map-graph'),
    dcc.Graph(id='station-graph'),
])

# Callback pour mettre à jour la carte
@app.callback(
    Output('map-graph', 'figure'),
    Input('map-graph', 'clickData')  # On écoute les clics sur la carte
)
def update_map(clickData):
    # Crée la carte interactive avec Plotly (Mapbox)
    fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_name="number",
                            hover_data=["available"],
                            zoom=13, height=400)
    fig.update_layout(mapbox_style="open-street-map")
    return fig

# Callback pour mettre à jour le graphique en fonction du clic sur une station
@app.callback(
    Output('station-graph', 'figure'),
    Input('map-graph', 'clickData')  # On écoute les clics sur les stations
)
def update_station_graph(clickData):
    if clickData is None:
        return {}  # Si aucun clic, ne rien afficher
    station_id = clickData['points'][0]['hovertext']  # Récupère le nom de la station cliquée
    station_data = data[data['number'] == station_id].sort_values(by='hour')  # Filtre les données pour la station sélectionnée

    # Crée un graphique simple (par exemple, histogramme ou autre)
    fig = px.bar(station_data, x='hour', y='available', orientation='v')
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)

