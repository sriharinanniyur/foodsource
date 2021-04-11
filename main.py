from flask import *
import csv
from flask_googlemaps import *
from geopy.geocoders import Nominatim
import json

all_data = [
    { # test object
        "coordinates" : [37.314170, -121.773780],
        "name" : "John Smith",
        "income" : "Less than $20,000",
        "address" : "4053 Carraci Lane San Jose",
        "food" : "Bread, 1 loaf",
        "id": 0,
    }
]
index = 1

geolocator = Nominatim(user_agent="foodsource")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order', methods=['GET', 'POST'])
def order():
    if (request.method == "POST"):

        # getting data
        fname = request.form['fname']
        income = request.form["income"]
        faddress = request.form["first-address"]
        saddress = request.form["second-address"]
        full_address = faddress + " " + saddress
        location = geolocator.geocode(faddress)
        coords = [location.latitude, location.longitude]
        food = request.form["food"]
        data = {
            "coordinates" : coords,
            "name" : fname,
            "income" : income,
            "address" : faddress,
            "food" : food,
            "id" : index
        }
        index = index + 1
        print(data)
        all_data.append(data)

        # saving data
        with open('db/db.csv', 'a') as db_file:
            employee_writer = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(data)
        
    return render_template("order.html")

@app.route('/help/<index>')
def help_page(index):
    return all_data[int(index) - 1] # need to subtract 1 because JS gives us index+1
# Aadit do ur thing here

@app.route('/getdata')
def getdata():
    return json.dumps(all_data)

if __name__ == '__main__':
    app.run(debug=True)
