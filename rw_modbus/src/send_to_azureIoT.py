# library to send to azure IoT 
from iothub_client import IoTHubClient, IoTHubTransportProvider, IoTHubMessage
import time
import json
import threading
import config

secrets = config.get_secrets()

CONNECTION_STRING = str(secrets["azure-string"])
PROTOCOL = IoTHubTransportProvider.MQTT


def send_confirmation_callback(message, result, user_context):
        print("Confirmation received for message with result = %s" % (result))
        print (user_context)



def send_data(message_data,asset_name):
    print("data to be send")
    print(message_data)
    my_json_string =  json.dumps(message_data)
    print(my_json_string)
    message = str(my_json_string).encode()
    print("encoded data is {}".format(message))
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    message = IoTHubMessage(message)
    client.send_event_async(message, send_confirmation_callback,asset_name)
    print("Message transmitted to IoT Hub")
    time.sleep(3)








