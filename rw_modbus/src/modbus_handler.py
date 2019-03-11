import minimalmodbus
import random
import send_to_azureIoT
import time
import datetime
import send_to_ubidots

minimalmodbus.TIMEOUT=0.15
class Asset():
    asset_name=None
    asset_total_register=None
    asset_value=[]
    asset_registers=None
    asset_type= None
    modbus_asset=None
    last_data=[]

    def __init__(self,slave,modbus_asset):
        self.asset_name=slave.slave_id
        self.modbus_asset=modbus_asset
        self.asset_registers=slave.registers
        self.asset_total_register=len(slave.registers)

    def add_value(self,value):
        self.asset_value=value


    def show_asset(self):
        print (self.asset_name)
        print (self.asset_total_register)
        print (self.asset_registers)
        print(self.modbus_asset)

    def read_modbus_for_asset(self):
        list=[]
        print("This function reads the modbus value for the asset")
        for register_tuple in self.asset_registers:
            #print(register_tuple)
            if int(register_tuple[1])==3:
                val=self.modbus_asset.read_register(int(register_tuple[2]),int(register_tuple[4]),int(register_tuple[1]),register_tuple[5])
                print("VALUE OBTAINED {}".format(val))
                #print("this dude will now call read_register with following arguments {},{},{},{}".format(register_tuple[2],register_tuple[3],register_tuple[1],register_tuple[5]))
                #print("this dude now says he got canides from modbus and this is for {}, and will be divded by{}".format(register_tuple[0],register_tuple[4]))
                #result= random.randint(0,240)
                #print("this dude now packs the above in a list and adds it to his values")
                list.append((register_tuple[0],val))
        self.add_value(list)

    def generate_data(self):
        print("This function will be used to generate the data that needs to be send in a required format")
        #for item in self.asset_value:
        payload=dict(self.asset_value)
        payload['imei']= "python-script-pc"
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        payload['time']= str(st)
        payload['slave_id']= int(self.asset_name)
        return(payload)

    def send_data(self):
        print("This will the function to pack the data that needs to be send to server")
        payload=self.generate_data()
        print(payload)
        #send_to_azureIoT.send_data(self.generate_data(),self.asset_name)
        send_to_ubidots.send_data(self.generate_data(),self.asset_name)

#this will change in production
port ='COM1'

#function returns a list of all assets
def modbus(slave_device_list):
    assets=[]
    for slave in slave_device_list:
        this_modbus_asset=minimalmodbus.Instrument(port,int(slave.slave_id),mode='rtu')

        this_asset = Asset(slave,this_modbus_asset)
        assets.append(this_asset)

    return assets


