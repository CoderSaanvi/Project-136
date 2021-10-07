from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route("/")
def index(): 
    return jsonify({
        "data":data,
        "message":"Success"
    }),200
@app.route("/star")
def star(): 
    name=request.args.get("name")
    starData=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":starData,
        "message":"Success"
    }),200

if __name__=="__main__":
    app.run()