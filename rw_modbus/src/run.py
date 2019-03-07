
import json
import logging
import os
import time
import config
import threading
from save_as_csv import *
from send_to_ftp import *
from pymongo import MongoClient
import config
from time import gmtime,strftime

secrets = config.get_secrets()

mongo_connection = str(secrets["mongo-string"])





fmt = "%Y-%m-%d %H:%M:%S"

# mongodb connection
myclient = MongoClient(mongo_connection)
mydb = myclient["mydatabase"]
mycol = mydb["modbus"]

# the config json is loaded into cfg
cfg = config.get_config()






def processor():

    print("In the processor")

    # open serial port based on the configuration for the devices


