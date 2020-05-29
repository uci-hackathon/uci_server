# UCI

Centralized backend

Workaround for account creation on blockchain (should be replaced for production)

## Prerequisites

* Python 3.8

## Installation

First, clone project on local machine.
```
git clone git@github.com:uci-hackathon/uci_server.git
```

Create virtual environment
```
python -m venv venv
```
and activate
```
source venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```

## Usage

### Environment

```
export CHAIN_API_URL=
export ACCOUNT_KEY=
export ACCOUNT_NAME=
export FLASK_ENV=
```

### Run

```
python run.py
```


### API Resources
Deployed HOST https://uci-hackathon.herokuapp.com

HOST http://localhost:5000

  - [POST /api/account]()

### POST /account

Example: http://localhost:5000/api/account

Request body:

    {
        "account_name": "accountname",
        "owner_key": "EOS...",
        "active_key": "EOS..."
    }

Response body:
    
    {
        "message": "Account created"
    }
    
## Built With

* [Flask](https://flask.palletsprojects.com/en/master/) - The web microframework
* [eospy](https://github.com/eosnewyork/eospy) - EOSIO Rest API wrapper    

## License

[MIT](https://github.com/uci-hackathon/uci_server/blob/master/LICENSE)