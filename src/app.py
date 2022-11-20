from cProfile import run
from flask import Flask
from decouple import config

from config import config
from routes import products, users

app=Flask(__name__)

def page_not_found(error):
    return "<h1>Not found Page</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(products.main, url_prefix='/api/products/')
    app.register_blueprint(users.main, url_prefix='/api/users/')
    app.run(host='0.0.0.0', debug=True)