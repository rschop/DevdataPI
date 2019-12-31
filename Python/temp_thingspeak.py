# meet de temperatuur en luchtvochtheid en stuurt de gegevens naar Thingspeak.com
import http.client
import urllib.request, urllib.parse, urllib.error
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
INTERVAL = 30 # in seconden
key = "9FLM7WF1LW6R49BT"  # Put your API Key here

def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.parse.urlencode({'field1':temperature, 'field2':humidity, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print((response.status, response.reason))
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

if __name__ == "__main__":
        while True:
                thermometer()
                start = time.time()
                #print(time.time())
                while time.time() - start < INTERVAL:
                     pass