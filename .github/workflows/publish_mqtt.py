import os
import json
import paho.mqtt.client as mqtt

# Get config from environment variables
broker_host = os.environ.get('MQTT_HOST')
broker_user = os.environ.get('MQTT_USER')
broker_pass = os.environ.get('MQTT_PASS')
payload_str = os.environ.get('DESIRED_STATE_PAYLOAD')

# Parse the payload to get the topic
payload_json = json.loads(payload_str)
topic = payload_json['topic']

client = mqtt.Client()
client.username_pw_set(broker_user, broker_pass)
client.connect(broker_host, 1883, 60)

# The message payload is the 'value' part of the JSON
message_to_publish = json.dumps(payload_json['value'])

# Publish and disconnect
result = client.publish(topic, message_to_publish)
status = result.rc
if status == 0:
    print(f"Successfully sent message to topic `{topic}`")
else:
    print(f"Failed to send message to topic `{topic}`")
client.disconnect()