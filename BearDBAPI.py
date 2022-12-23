from app import create_app
import os
import json
from werkzeug.routing import BaseConverter
import subprocess
from flask_cors import CORS,cross_origin
import datetime
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(super(ListConverter, self).to_url(value)
                        for value in values)
class BeardbAPI:
    def __init__(self):
        self.app = create_app('config.development')
        self.cors = CORS(self.app, resources={r"/foo": {"origins": "*"}})
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.host = 'localhost'
        self.port= 9000
        print(self.app.url_map)
 
        


    #  
    def storage(self,app_name:str, dir:str=''):     
            # if not os.path.isdir(dir):
            #     os.mkdir(dir)
            app_dir = os.path.join(dir, app_name)
            if not os.path.exists(app_dir):
                os.makedirs(app_dir)
                with open(os.path.join(app_dir, ".bdb"), "w") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d"))
                    f.write("\n")
                    f.write(app_name)
                open(os.path.join(app_dir, "ips.json"), "w").close()
              
            else:
                if not os.path.exists(os.path.join(app_dir, ".bdb")):
                    raise Exception(".bdb file does not exist in the directory")
            os.system(f"cd {app_dir}")
            os.chdir(app_dir)
            print(os.getcwd())
            if not os.path.exists('users.json'):
                with open('users.json', 'w') as f:
                    json.dump([], f)

    def service(self):
        return self.app                
    def host(self):
        return self.app
    def run(self,host:str,port:int):
        
        # print('BearDB API started at http://{}:{}'.format(self.host, self.port))

        self.app.run(host=self.host, port=self.port, debug=True)
    def run_gunicorn(host, port):
        try:
    
            subprocess.check_output(['gunicorn', '--version'])
        except OSError:
    
            print('Gunicorn is not installed. Please install Gunicorn to run the app.')
            return

    
        subprocess.run(['gunicorn', '-b', f'{host}:{port}', 'run:api'])
        
     


