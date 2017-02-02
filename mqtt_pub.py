import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('iot.eclipse.org',1883)
client.publish('iot/mad','Hi,Im Publisher')

