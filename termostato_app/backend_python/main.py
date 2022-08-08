from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import redis

app = Flask(__name__)
CORS(app)

@app.route("/redis/keys", methods=['GET'])
def redis_keys():
    r = redis.Redis(host='localhost', port=6379, db=0, password='root')
    chiavi = r.keys('*')
    chiavi = [ k.decode('utf-8') for k in chiavi]
    r.close()
    return jsonify(chiavi)

@app.route("/redis/set/<key>/<value>", methods=['GET'])
def redis_set(key,value):
    r = redis.Redis(host='localhost', port=6379, db=0, password='root')
    r.set(key, str(value))
    r.close()
    return 'Ok'

@app.route("/redis/get/<key>", methods=['GET'])
def redis_get(key):
    r = redis.Redis(host='localhost', port=6379, db=0, password='root')
    outcome = r.get(key)
    r.close()
    return outcome


@app.route("/saveGradi", methods=['POST','GET'])
def saveGradi():
    data = json.loads(request.data.decode('utf-8'))
    user_name = data['user_name']
    gradi = data['gradi']
    #f = open(f'storage/{user_name}.txt', 'w')
    #f.write(str(gradi))
    #f.close()

    r = redis.Redis(host='localhost', port=6379, db=0, password='root')
    r.set('gradi', str(gradi) )
    r.close()

    #client = MongoClient('mongodb://root:byte21@localhost:27017')
    #db = client.termostati
    #col = db['gradi']
    #col.insert_one(dict(user_name=user_name, gradi=gradi))

    return "Ho Salvato"

@app.route("/getGradi", methods=['GET','POST'])
def getGradi():
    data = json.loads(request.data.decode('utf-8'))
    user_name = data['user_name']
    #f = open(f'storage/{user_name}.txt', 'r')
    #gradi = f.read()
    #f.close()
    r = redis.Redis(host='localhost', port=6379, db=0, password='root')
    gradi = r.get('gradi' )
    r.close()
    return gradi


app.run(
    debug=True,
    port=5050
)