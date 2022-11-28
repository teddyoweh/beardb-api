from app import create_app
# from waitress import serve
from flask_cors import CORS
app = create_app('config.development')

if __name__ == '__main__':
    app.run(host='0:0:0:0', port=5000, debug=True)
