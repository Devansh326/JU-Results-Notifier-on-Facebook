from time import sleep
from modules import scraper, clear

def checker():
    print("main checker starts")
    s = scraper()
    s.populate()
    s.navigate(setup=False)
    return

def startup():
    print("initializing")
    clear()
    s = scraper()
    s.populate()
    s.navigate(setup=True)
    print("database created")
    return



if __name__ == '__main__':
    startup()
    i=0
    while True:
        print("loop {}".format(i))
        checker()
        sleep(900)
        i += 1
