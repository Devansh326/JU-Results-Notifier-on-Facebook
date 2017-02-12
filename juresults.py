from flask import Flask
from modules import scraper
import os
from time import sleep



app = Flask(__name__)

def checker():
    print("main checker starts")
    s = scraper()
    s.populate()
    s.navigate(setup=False)

@app.route('/loop/')
def loop():
    checker()
    sleep(900)

@app.route('/init/')
def startup():
    print("initializing")
    s = scraper()
    s.populate()
    s.navigate(setup=True)
    print("database created")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)