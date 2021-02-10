import random
DHT22="DHT22"

def read_retry(sensor,pin):

    humidity = round(random.uniform(5.0, 100.0),2)
    temperature = round(random.uniform(0.1, 40.1),2)

    return humidity, temperature