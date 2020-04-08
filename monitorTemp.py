import paho.mqtt.client as mqtt
import ast

tempSlaap = 0
tempBad = 0

def printAll():
    print("Slaapkamer:" + str(tempSlaap) + " Badkamer: " + str(tempBad))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tele/+/SENSOR/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global tempSlaap
    global tempBad

    byte_str = msg.payload
    dict_str = byte_str.decode("UTF-8")
    dmsg = ast.literal_eval(dict_str)

    if "DS18B20" in dmsg:
        tempSlaap = dmsg['DS18B20']['Temperature']
    if "SI7021" in dmsg:
        tempBad = dmsg['SI7021']['Temperature']

    printAll()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("udoo", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
