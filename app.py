from flask import Flask, render_template, request
from model import get_predictions, get_location_encode
import pandas as pd
import os


app = Flask(__name__)

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        Location = request.form['Location']
        Area = request.form['Area']
        No_of_bedrooms = request.form['No. of bedrooms']
        
        data = pd.DataFrame({'Area': [Area],'Location_encoded': [get_location_encode(Location, json_path = json_path)],'No. of Bedrooms': [No_of_bedrooms]})
        try:
            prediction = get_predictions(data)
            #print(prediction)
        except Exception as e:
            print(f"An error occurred: {e}")

    return render_template('index.html', prediction = prediction)


json_path = os.path.join(BASE_DIR, 'hash_map.json')
if __name__ == '__main__':
    app.run()