
import json
import logging
import os
import time
import config
import threading
from save_as_csv import *
from send_to_ftp import *
from pymongo import MongoClient



from time import gmtime,strftime



fmt = "%Y-%m-%d %H:%M:%S"

# mongodb connection
myclient = MongoClient("mongodb+srv://admin:W1nd0ws87@cluster0-wkvwq.gcp.mongodb.net/test?retryWrites=true")
mydb = myclient["mydatabase"]
mycol = mydb["modbus"]

# the config json is loaded into cfg
cfg = config.get_config()






def processor():

    print("In the processor")

    # open serial port based on the configuration for the devices


