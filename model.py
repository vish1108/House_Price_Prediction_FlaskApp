import pandas as pd
import numpy as numpy
import json
import pickle
from sklearn.ensemble import RandomForestRegressor
import os
from difflib import get_close_matches

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_location_encode(location, json_path):
    with open(json_path) as user_file:
        data = json.load(user_file)

    if location in data:
        return data[location]
    
    close_matches = get_close_matches(location, data.keys(), n=1, cutoff=0.6)
    if close_matches:
        closest_location = close_matches[0]
        print("Closes match---->", closest_location)
        return data[closest_location]
        
    # print("Location---->", data.get(location, "Location not found"))
    # return data.get(location, "Location not found")

def get_predictions(data):
    model_path = os.path.join(BASE_DIR, 'random_forest_model.pkl')
    with open(model_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
        predictions = loaded_model.predict(data)
    
    #print(f"The prediction is: ", predictions[0])
    return int(predictions[0])
    
    

json_path = os.path.join(BASE_DIR, 'hash_map.json')