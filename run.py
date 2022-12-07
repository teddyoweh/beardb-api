from app import create_app
# from waitress import serve
from flask_cors import CORS,cross_origin
app = create_app('config.development')
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
