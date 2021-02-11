
import os, json

_db = {}


BCM = "BCM"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"

APP_PATH = os.path.dirname(os.path.abspath(__file__))

def setmode(mode):
    #print("GPIO Mode Set: " + str(mode))
    return


def setwarnings(w):
    #print("GPIO Warnnig Set: " + str(w))
    return


def setup(pins, mode):
    #print("GPIO Setup. Pins " + str(pins) + " set to " + str(mode))
    _load_db()
    for pin in pins:
        pin=str(pin)
        _db[pin]={"mode":mode, "state" : "LOW"}
    #print (_db)
    _save_db()
    return


def input(pin):
    _load_db()
    pin=str(pin)
    #print ("Input " + _db[pin]["state"])
    return _db[pin]["state"]


def output(pins, states):
    _load_db()
    #print("GPIO Output. Pins " + str(pins) + " set to " + str(states))

    # Set all pin to the same state
    if isinstance(states, str):
        for pin in pins:
            pin=str(pin)
            _db[pin] = {"state": states, "mode": _db[pin]["mode"]}
    # set each pin individually
    elif len(pins) == len(states):
        for i in range(len(pins)):
            pin=str(pins[i])
            _db[pin] = {"state": states[i], "mode": _db[pin]["mode"]}
    else:
        print("Invalid call. Pins list is not consistent with States list")

    #print(_db)
    _save_db()
    return


def cleanup():
    print("GPIO Cleanup")
    return

def _load_db():
    global _db
    if (os.path.exists(APP_PATH + "/pins.json")):
        with open(APP_PATH + '/pins.json', 'r') as db_file:
            _db = json.load(db_file)
    else:
        _db = {}
        _save_db()
    return

def _save_db():
    with open(APP_PATH + "/pins.json", "w+") as db_file:
        db_file.write(json.dumps(_db, indent=4))
    return

