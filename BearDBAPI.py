from app import create_app
import os
import json
from werkzeug.routing import BaseConverter
import subprocess
from flask_cors import CORS,cross_origin







class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(super(ListConverter, self).to_url(value)
                        for value in values)
class BearDBAPI:
    def __init__(self):
        self.app = create_app('config.development')
        self.cors = CORS(self.app, resources={r"/foo": {"origins": "*"}})
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.host = 'localhost'
        self.port= 9000
        # check if users.json exists if not create it
        if not os.path.exists('users.json'):
            with open('users.json', 'w') as f:
                json.dump({}, f)
    def config(self, host, port):
        self.host = host
        self.port = port
    def host(self):
        return self.app
    def run(self):
        
        print('BearDB API started at http://{}:{}'.format(self.host, self.port))

        self.app.run(host=self.host, port=self.port, debug=True)
    def run_gunicorn(host, port):
        try:
    
            subprocess.check_output(['gunicorn', '--version'])
        except OSError:
    
            print('Gunicorn is not installed. Please install Gunicorn to run the app.')
            return

    
        subprocess.run(['gunicorn', '-b', f'{host}:{port}', 'run:api'])
        
     


