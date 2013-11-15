HOST = '127.0.0.1'
PORT = 5000

DEBUG = True
TESTING = True

API_VERSION = '1'

SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

CLIENTS = {
  'silver': {
    'client_key': 'lhHZ+epiTvWApo/+vmv/w',
    'client_id' : '78ce8a9d-e7e6-42f8-bc10-ac15580eb1c1',
    'host'      : 'silver.presslabs.com'
  },
  'plutonium': {
    'client_key': 'ekuc+xvVRMClIbjLmEFLJ',
    'client_id' : '7a4b9cfb-1bd5-44c0-a521-b8cb98414b27',
    'host'      : 'plutonium.presslabs.com'
  }
}
