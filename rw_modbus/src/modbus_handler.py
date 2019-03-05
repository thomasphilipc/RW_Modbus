import minimalmodbus
import random


class Asset():
    asset_name=None
    asset_total_register=None
    asset_value=[]
    asset_registers=None
    modbus_asset=None

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
                result= random.randint(0,240)
                #print("this dude now packs the above in a list and adds it to his values")
                list.append((register_tuple[0],result))
        self.add_value(list)


    def send_data(self):
        print("This will the function to pack the data that needs to be send to server")
        print(self.asset_value)


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


