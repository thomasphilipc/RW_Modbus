import json
import os

APP_PATH = ""
MYAPP_NAME = "rw_modbus"
CONFIG_PATH ="C:\Users\\thomas.philip\PycharmProjects\RW_Modbus\\rw_modbus"


def get_config():
    try:

        path=os.chdir(CONFIG_PATH)
        print (os.getcwd())

        #with open(APP_PATH + MYAPP_NAME + "/temp_config.json", "r") as f:
        with open(CONFIG_PATH + "/temp_config.json", "r") as f:
            config = json.loads("".join(f.readlines()))
    except Exception:
        raise
    return config


def get_secrets():
    try:

        path=os.chdir(CONFIG_PATH)
        print (os.getcwd())

        #with open(APP_PATH + MYAPP_NAME + "/temp_config.json", "r") as f:
        with open(CONFIG_PATH + "/secrets.hide", "r") as f:
            config = json.loads("".join(f.readlines()))
    except Exception:
        raise
    return config
