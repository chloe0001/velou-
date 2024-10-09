import update_dynamic_data_velou_bd
import update_static_data_velou_bd
import get_dynamic_data
import psycopg2
import json
from datetime import datetime

import os
import sys


script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

get_dynamic_data.get_dynamic_only_data('c0796b53b9a70237cb401518444ba6078ddc107b', 'Toulouse')
update_static_data_velou_bd.update_static_data_velou_bd() 
update_dynamic_data_velou_bd.update_dynamic_data_velou_bd()



with open("log_update.txt", "a") as log_file:
    log_file.write(f"Script exécuté à {datetime.now()}\n")


