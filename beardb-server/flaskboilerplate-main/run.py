from app import create_app
# from waitress import serve

app = create_app('config.development')

if __name__ == '__main__':
    app.run()
