import requests
import json

# API URL
#DYNAMIC_DATA_URL = "https://api.jcdecaux.com/vls/v1/stations?contract='Toulouse'&apiKey='c0796b53b9a70237cb401518444ba6078ddc107b'"
DYNAMIC_DATA_URL = "https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}"

def get_dynamic_data(api_key, contract_name):
    url = DYNAMIC_DATA_URL.format(contract_name=contract_name, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        dynamic_data = response.json()
      # Sauvegarder les données dans un fichier JSON
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(dynamic_data, f, ensure_ascii=False, indent=4)
        
        print("Données enregistrées dans le fichier 'data.json'.")
        print("Données dynamiques récupérées avec succès.")
        return dynamic_data
    else:
        print(f"Erreur lors de la récupération des données dynamiques: {response.status_code}")
        return None


get_dynamic_data('c0796b53b9a70237cb401518444ba6078ddc107b', 'Toulouse')
