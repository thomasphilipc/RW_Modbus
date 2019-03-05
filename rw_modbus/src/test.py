import config
import modbus_handler


cfg =config.get_config()




class slave_device_template:
    slave_template_type = None
    poll_list = []

    def __init__(self,slave_template_type):
        self.slave_template_type = slave_template_type

    def initialize_poll_list(self,poll_list):
        self.poll_list=poll_list

    def show_slave_device_template(self):
        print(self.slave_template_type)
        print(self.poll_list)


    def get_slave_id(self):
        return (self.slave_template_type)



# class to hold the slave-id, device-type and registers
class slave_device:
    slave_id= None
    slave_id_template=None
    registers = []


    def __init__(self,slave_id,slave_id_template):
        self.slave_id = slave_id
        self.slave_id_template=slave_id_template


    def gather_registers(self,slave_device_template):
        self.registers=slave_device_template.poll_list

    def modbus_register(self):
        modbus_register_list=[]
        for item in self.registers:
            (description,function_code,register_address,register_multiplier,num_of_decimals,signed,register_type)=(item[0],item[1],item[2],item[3],item[4],item[5],item[6])
            this=(function_code,register_address,register_multiplier,register_type)
            modbus_register_list.append(this)
        return(modbus_register_list)

    def show_slave_device(self):
        print("Slave id is {}".format(self.slave_id))
        print("Slave template id is {}".format(self.slave_id_template))
        print("Slaves registers are {}".format(self.registers))
        print(self.modbus_register())

# class to hold the  slave_device-type and the associated registers


# this list holds all the slave device types
slave_device_templates=[]

# below is the 2 templates that are read
for k in range(len(cfg["slave_template"])):
    print ("There are {} registers configured to be read in this {} template".format(len(cfg["slave_template"][k]["commands"]),cfg["slave_template"][k]["description"]))
    register_list=[]
    for i in range(len(cfg["slave_template"][k]["commands"])):
        current_tag = 'tag_'+str(i+1)
        print("{} - {} {} {} {} {} {}".format((cfg["slave_template"][k]["commands"][current_tag]["description"]),(cfg["slave_template"][k]["commands"][current_tag]["function_code"]),
                                              (cfg["slave_template"][k]["commands"][current_tag]["register_address"]),(cfg["slave_template"][k]["commands"][current_tag]["register_multiplier"]),
                                              (cfg["slave_template"][k]["commands"][current_tag]["num_of_decimals"]),(cfg["slave_template"][k]["commands"][current_tag]["signed"]),
                                              (cfg["slave_template"][k]["commands"][current_tag]["register_type"])))
        current_register_tuple=(cfg["slave_template"][k]["commands"][current_tag]["description"],cfg["slave_template"][k]["commands"][current_tag]["function_code"],
                                cfg["slave_template"][k]["commands"][current_tag]["register_address"],cfg["slave_template"][k]["commands"][current_tag]["register_multiplier"],
                                cfg["slave_template"][k]["commands"][current_tag]["num_of_decimals"],cfg["slave_template"][k]["commands"][current_tag]["signed"],
                                cfg["slave_template"][k]["commands"][current_tag]["register_type"])
        register_list.append(current_register_tuple)
    print("--------------------------------------------")
    current_slave=slave_device_template(cfg["slave_template"][k]["slave_template_id"])
    current_slave.initialize_poll_list(register_list)
    slave_device_templates.append(current_slave)


# below are the slave devices from config
# print("number of slave types".format(len(slave_device_templates)))
#
# for index in range(len(slave_device_templates)):
#     item=slave_device_templates[index]
#     print(item)

slave_device_list=[]
print("Total number of salves is {}".format(len(cfg["slaves"])))
# iterate through all the slaves in config

for index in range(len(cfg["slaves"])):
    #creating a slave
    this_slave = slave_device(cfg["slaves"][index]["slave_id"],cfg["slaves"][index]["slave_template_id"])
    # iterate through each device template
    for slave_type in slave_device_templates:
        slave_template_id=slave_type.get_slave_id()
        if (slave_template_id==cfg["slaves"][index]["slave_template_id"]):
            this_slave.gather_registers(slave_type)
    slave_device_list.append(this_slave)

for item in slave_device_list:
    item.show_slave_device()

for modbus_asset in modbus_handler.modbus(slave_device_list):
    modbus_asset.read_modbus_for_asset()
    modbus_asset.send_data()
