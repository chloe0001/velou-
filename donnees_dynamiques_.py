#code pour récupérer les données dynamiques sans considérer les données statiques pour envoyer à la base de données

import requests
import json

DYNAMIC_DATA_URL = "https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}"

def get_dynamic_only_data(api_key, contract_name):
    url = DYNAMIC_DATA_URL.format(contract_name=contract_name, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        dynamic_data = response.json()
        
        filtered_data = []
        
        for station in dynamic_data:
            filtered_station = {
                "bike_stands": station["bike_stands"],
                "available_bike_stands": station["available_bike_stands"],
                "available_bikes": station["available_bikes"],
                "status": station["status"],
                "last_update": station["last_update"]
            }
            filtered_data.append(filtered_station)

      # Sauvegarder les données dans un fichier JSON
        with open('data_dynamique.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)
        
        print("Données enregistrées dans le fichier 'data_dynamique.json'.")
        print("Données dynamiques récupérées avec succès.")
        return filtered_data
    else:
        print(f"Erreur lors de la récupération des données dynamiques: {response.status_code}")
        return None


get_dynamic_only_data('c0796b53b9a70237cb401518444ba6078ddc107b', 'Toulouse')



