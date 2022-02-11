from flask import Flask,jsonify,request
from API import recogniseNumber

app = Flask(__name__)

@app.route("/getNumber")
def getNumber():
    res = request.args.get("name")
    number = recogniseNumber(res)    
    return jsonify({ "predicted Number":number}),200
        
if __name__ == "__main__": 
    app.run(debug=True)
