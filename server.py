from flask import Flask, request
from eospy.cleos import Cleos
import eospy.keys
import os
from config import config_by_name

app = Flask(__name__)
app.config.from_object(config_by_name[os.getenv('FLASK_ENV') or 'development'])

ce = Cleos(url=app.config['CHAIN_API_URL'])


@app.route('/api/account', methods=['POST'])
def create_account():
    try:
        account_name = request.json['account_name']
        active_key = request.json['active_key']
        owner_key = request.json['owner_key']

        ce.create_account(app.config['ACCOUNT_NAME'], eospy.keys.EOSKey(app.config['ACCOUNT_KEY']), account_name,
                          owner_key, active_key,
                          stake_net='1.0000 TLOS', stake_cpu='1.0000 TLOS')
    except Exception as e:
        return {'message': 'Failed to create account'}, 400

    return {'message': 'Account created'}, 200
