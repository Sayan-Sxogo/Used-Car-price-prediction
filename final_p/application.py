import pickle
# import joblib
from flask import Flask, render_template,request
import pandas as pd
import numpy as np
app=Flask(__name__)

# xgb_reg = pickle.load(open("finalized_model.pkl", "rb"))
# pickle.dump(xgb_reg, open("finalized_model.pkl", "wb"))
model=pickle.load(open('finalized_model.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    name = int(request.form.get("name"))
    location = int(request.form.get("location"))
    year = int(request.form.get("year"))
    kilometers_driven = int(request.form.get("kilometers_driven"))
    fuel_type = int(request.form.get("fuel_type"))
    transmission = int(request.form.get("transmission"))
    owner_type = int(request.form.get("owner_type"))
    mileage = float(request.form.get("mileage"))
    engine = float(request.form.get("engine"))
    power = float(request.form.get("power"))
    seats = float(request.form.get("seats"))
    print(name)
    print(location)
    print(seats)
    print(mileage)
    print(year)
    print(kilometers_driven)
    print(fuel_type)
    print(transmission)
    print(owner_type)
    print(engine)
    print(power)
    year=2023-year
    data = {"Name": name,
            "Location": location,
            "Year": year,
            "Kilometers_Driven": kilometers_driven,
            "Fuel_Type": fuel_type,
            "Transmission": transmission,
            "Owner_Type": owner_type,
            "Mileage": mileage,
            "Engine": engine,
            "Power": power,
            "Seats": seats}
    df = pd.DataFrame(data,index=[0])
    print(df)
    prediction = model.predict(df)
    # prediction = xgb_reg.predict(df)
    print(prediction)
    output = np.round(prediction[0],2)
    print(output)
    if output < 0:
        return render_template('result.html', prediction_texts="Sorry you cannot sell this car")
    else:
        return render_template('result.html', prediction_text="{:.2f}".format(output))

if __name__=="__main__":
    app.run(debug=True)