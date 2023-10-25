import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET']

CORS(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = PyMongo(app).db

@app.route('/jobss',methods=["POST","GET"])
def job():
    name=db.users.find_one({"email":"sid@gmail.com"})
    return jsonify({"email": name["email"], "isDoctor":name["isDoctor"]}) 

@app.route("/page",methods=["POST","GET"])
@jwt_required()
def pages():
     ans=request.get_json()
     print(ans)
     db.ans.insert_one(ans)
     return jsonify("hello")


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = request.get_json()
    # if response['userType'] == 'USER':
    user = db.users.find_one({'email': response['email']})
    if user:
        if bcrypt.check_password_hash(user['password'], response['password']):
            access_token = create_access_token(identity=user['email'])
            return jsonify({'login': True, 'token': access_token})
        return jsonify({'login': False, 'error': 'Incorrect Password'})
    return jsonify({'login': False, 'error': 'EmailId not registered'})
    # elif response['userType'] == 'ORG':
    #     org = db.organisations.find_one({'email': response['email']})
    #     if org:
    #         if bcrypt.check_password_hash(org['password'], response['password']):
    #             access_token = create_access_token(identity=org['email'])
    #             return jsonify({'login': True, 'token': access_token})
    #         return jsonify({'login': False, 'error': 'Incorrect Password'})
    #     return jsonify({'login': False, 'error': 'EmailId not registered'})


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    response = request.get_json()
    if response['userType'] == 'USER':
        isUser = db.users.find_one({'email': response['email']})
        if isUser is None:
            hashed_pass = bcrypt.generate_password_hash(response['password']).decode('utf-8')
            db.users.insert_one({
                'name': response['name'],
                'email': response['email'],
                'password': hashed_pass,
                'nfts': []
            })
            return jsonify({'signup': True})
        return jsonify({'signup': False, 'error': 'EmailId already registered'})

    elif response['userType'] == 'ORG':
        isOrg = db.organisations.find_one({'email': response['email']})
        if isOrg is None:
            hashed_pass = bcrypt.generate_password_hash(response['password']).decode('utf-8')
            db.organisations.insert_one({
                'name': response['name'],
                'email': response['email'],
                'gstin': response['gstin'],
                'password': hashed_pass,
                'nfts': []
            })
            return jsonify({'signup': True})
        return jsonify({'signup': False, 'error': 'EmailId already registered'})


@app.route('/buyNFT', methods=['POST', 'GET'])
def buyNFT():
    response = request.get_json()
    db.users.find_one_and_update({'email': response['email']},
    {'$push': {'nfts':{
        'image': response['image'],
        'title': response['title'],
        'price': response['price'],
        'description': response['description']
    }}})
    return jsonify({'nft': True})


@app.route('/addNFT', methods=['POST', 'GET'])
def addNFT():
    response = request.get_json()
    db.organisations.find_one_and_update({'email': response['email']},
    {'$push': {'nfts': {
        'image': response['image'],
        'title': response['title'],
        'price': response['price'],
        'description': response['description']
    }}})
    return jsonify({'nft': True})


@app.route('/getNFTs', methods=['POST', 'GET'])
@jwt_required()
def getNFTs():
    user = get_jwt_identity()
    print(user)
    nfts = db.users.find_one({'email': user}, {'nfts': 1})
    return jsonify(nfts['nfts'])


# @app.route("/getChat", methods=['POST', 'GET'])
# def chatAPI():
#     response = request.get_json()
#     response = getChat(response['prompt'])
#     return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)