from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    age = 30
    price = 19.54
    patient = "John Smith"
    patient_age = 20
    new_patient = True
    print(age, price, patient, patient_age, new_patient)
    return "Hello World!"

if __name__ == "__main__":
    server.run(host='0.0.0.0')
 
