
from flask import Flask
from flask import jsonify
from flask import request
import pymongo

app = Flask(__name__)

config = {
    "username": "root",
    "password": "Secret",
    "server": "mongo",
}

connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = pymongo.MongoClient(connector)

#app.config['MONGO_DBNAME'] = 'flaskdb'
#app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/flaskdb'


#app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = client["demo"]

@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/star/', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
