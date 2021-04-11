from flask import *
import csv
from flask_googlemaps import *
from geopy.geocoders import Nominatim
import json
# import twilio_verify

index = 1
all_data = [
    { # test object
        "coordinates" : [37.314170, -121.773780],
        "name" : "John Smith",
        "income" : "Less than $20,000",
        "address" : "4055 Carraci Lane San Jose",
        "food" : "Bread (1 loaf), 4 Bananas, 3 Apples",
        "id": 0,
    },
    { # test object
        "coordinates" : [37.320812, -121.779586],
        "name" : "Raymond White",
        "income" : "Less than $20,000",
        "address" : "4058 Amarado Street San Jose",
        "food" : "Pizza, broccoli, onions",
        "id": 1,
    }
]

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
        phone_num = request.form["phone-number"]
        twilio_code = request.form["twilio-code"]

        # this doesn't work for some reason, so we finna ignore it for now
        # if twilio_verify.check_verification(phone_num, twilio_code) != "approved":
            # return render_template("order.html", errmsg="Unrecognized verification code.")
        global index
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


        
    return render_template("order.html", errmsg="")

@app.route('/help/<index>')
def help_page(index):
    data = all_data[int(index) - 1] # need to subtract 1 because JS gives us index+1
    return render_template("help.html", data=data)

@app.route('/getdata')
def getdata():
    return json.dumps(all_data)

@app.route('/send_twilio_code/<number>/<new_code>')
def send_twilio_code(number):
    twilio_verify.send_verification(str(number))
    return number

if __name__ == '__main__':
    app.run(debug=True)
