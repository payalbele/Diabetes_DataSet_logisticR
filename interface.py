from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import Diabetes
app = Flask(__name__)

########################################################################

@app.route('/') 
def hello_flask():
    return 'Hello Mock Group_06'

#########################################################################


@app.route('/predict')
def get_predicted():

    data = request.get_json()
    Glucose = eval(data['Glucose'])
    BloodPressure = eval(data['BloodPressure'])
    SkinThickness = eval(data['SkinThickness'])
    Insulin = eval(data['Insulin'])
    BMI = eval(data['BMI'])
    DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFunction'])
    Age = eval(data['Age'])
    
    
    
    dib = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = dib.get_predicted()
    
    return jsonify({"Result":f"Predicted Patient Having Diabetes : {result}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)