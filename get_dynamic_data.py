""" Ce script récupère les données dynamiques des stations en utilisant l'API JCDecaux. 
Si la requète est réussie, les données sont stockées dans un fichier JSON
"""


import requests
import json

DYNAMIC_DATA_URL = "https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}"

def get_dynamic_only_data(api_key, contract_name):
    """Args : 
            contract_name (str) : Ville où l'on souhaite récupérer les données
            api_key (str) : clé d'API
        Returns : 
            Dict | None : le fichier JSON contenant les données si la requète réussit. None sinon. 
    """
    url = DYNAMIC_DATA_URL.format(contract_name=contract_name, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        dynamic_data = response.json()
        
        filtered_data = []
        
        for station in dynamic_data:
            filtered_station = {
                "number" : station["number"],
                "bike_stands": station["bike_stands"],
                "available_bike_stands": station["available_bike_stands"],
                "available_bikes": station["available_bikes"],
                "status": station["status"],
                "last_update": station["last_update"]
            }
            filtered_data.append(filtered_station)

      # Sauvegarder les données dans un fichier JSON
        with open('dynamic_data.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)
        
        print("Données enregistrées dans le fichier 'dynamic_data.json'.")
        print("Données dynamiques récupérées avec succès.")
        return filtered_data
    else:
        print(f"Erreur lors de la récupération des données dynamiques: {response.status_code}")
        return None





