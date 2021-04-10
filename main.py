from flask import *
import csv
from flask_googlemaps import *

app = Flask(__name__)
GoogleMaps(app, key="AIzaSyAMIY4ozo4newtFCoD-7wno2dJlHvSDwFc") 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order', methods=['GET', 'POST'])
def order():
    if (request.method == "POST"):
        fname = request.form['fname']
        income = request.form["income"]
        faddress = request.form["first-address"]
        saddress = request.form["second-address"]
        full_address = faddress + ", " + saddress
        food = request.form["food"]
        data = [fname, income, full_address, food]
        print(data)

        with open('db/db.csv', 'a') as db_file:
            employee_writer = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(data)
        

    return render_template("order.html")



if __name__ == '__main__':
    app.run(debug=True)
