

BCM="BCM"
OUT = "OUT"
LOW="LOW"
HIGH="HIGH"


def setmode(mode):
    print ("GPIO Mode Set: " + str(mode))
    return

def setwarnings(w):
    print ("GPIO Warnnig Set: " + str(w))
    return

def setup(pins,direction):
    print ("GPIO Setup. Pins " + str(pins) + " set to " + str(direction))
    return

def input(pin):
    return LOW
def output(pins,directions):
    print ("GPIO Output. Pins " + str(pins) + " set to " + str(directions))
    return
def cleanup():
    print ("GPIO Cleanup")
    return

