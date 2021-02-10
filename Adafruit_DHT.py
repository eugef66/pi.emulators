import random
DHT22="DHT22"

def read_retry(sensor,pin):

    humidity = round(random.uniform(5.0, 100.0),2)
    temperature = round(random.uniform(40.1, 105.1),2)

    return humidity, temperature