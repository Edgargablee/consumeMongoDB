from flask import Flask, render_template, make_response, jsonify, request
import pymongo
import pymongo.errors
import secrets

app = Flask(__name__)

@app.route("/")
def instruccion():
    return render_template('index.html')

def get_db():
    client = pymongo.MongoClient("mongodb+srv://edgargablee:nsPhhHLupyoi8xJd@cluster1.q6ifsnf.mongodb.net/?retryWrites=true&w=majority")
    db = client.user

@app.route("/user/newUser")
def createUser():
    if request.args:
        req = request.args
        name = req.get('name')
        age = req.get('age')
        tocken = secrets.token_hex(10)
    user={"name":name,
        "age":age,
        "tocken":tocken}
    id_Insert = insertUser(user)
    #return "<h1>"+id_Insert+"</h1>"
    return "<h1>Insercion</h1>"

def insertUser(user):
    db = get_db()
    result = db.user.insert_one(user)
    return result.inserted_id

@app.route("/user/consult")
def consultUser():
    if request.args:
        req = request.args
        name = req.get('name')
        age = req.get('age')
    user={"name":name,
        "age":age}
    result = consultUser(user)
    #return "<h1>"+result+"</h1>"
    return "<h1>Consulta</h1>"

def consultUser(user):
    try:
        db = get_db()
        result = db.user.find(user).limit(10)
    except:
        res = make_response(jsonify({"error": "No Query String"}), 404)
        return res
    return result


app.run(host="0.0.0.0")