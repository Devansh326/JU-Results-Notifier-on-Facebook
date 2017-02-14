from flask import Flask
from modules import scraper
import os
import atexit
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger




app = Flask(__name__)

def checker():
    print("main checker starts")
    s = scraper()
    s.populate()
    s.navigate(setup=False)

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=checker,
    trigger=IntervalTrigger(seconds=900),
    id='printing_job',
    name='the scheduler job',
    replace_existing=True)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/loop/')
def route_loop():
    checker()
    sleep(900)

@app.route('/init/')
def route_startup():
    print("initializing")
    s = scraper()
    s.populate()
    s.navigate(setup=True)
    print("database created")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)


"""

if __name__ == '__main__':
    startup()
    i=0
    while True:
        print("loop {}".format(i))
        checker()
        sleep(900)
        i += 1
"""
