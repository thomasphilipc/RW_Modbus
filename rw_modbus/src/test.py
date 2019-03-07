import config
import modbus_handler
import asset_handler

# class to hold the  slave_device-type and the associated registers





# below are the slave devices from config
# print("number of slave types".format(len(slave_device_templates)))
#
# for index in range(len(slave_device_templates)):
#     item=slave_device_templates[index]
#     print(item)


slave_device_list = asset_handler.gather_slaves()
print(slave_device_list)
print("Going to read the modbus information")


for modbus_asset in modbus_handler.modbus(slave_device_list):
    modbus_asset.read_modbus_for_asset()
    modbus_asset.send_data()
