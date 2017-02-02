import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('iot.eclipse.org',1883)
client.subscribe('iot/mad')


def on_message(client, userdata, msg):
    print(msg)
    print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
    
client.on_message = on_message
client.loop_forever()
