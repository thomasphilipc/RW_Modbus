from threading import Timer,Thread,Event
from time import sleep
import datetime
import Queue
import sys
import asset_handler
import modbus_handler

# repeated timer
class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()


def start_app():


    slave_device_list = asset_handler.gather_slaves()
    print(slave_device_list)
    print("Going to read the modbus information")

    modbus_to_poll=modbus_handler.modbus(slave_device_list)



    q = Queue.Queue()

    while True:
        global now
        now = datetime.datetime.now()
        for modbus_asset in modbus_to_poll:
            modbus_asset.read_modbus_for_asset()
            modbus_asset.send_data()
        sleep(10)
        if not q.empty():
            item = q.get()
            print(item)
            q.task_done()




def task1(q):
    q.put(" {}:{}:{} : 5 sec timer".format(now.hour,now.minute,now.second))


def task2(q):
    q.put(" {}:{}:{} : 10 sec timer".format(now.hour,now.minute,now.second))





def usage():
    print 'Please contact Thomas on thomas.philip@roamworks.com'
    sys.exit(255)

def main(argv=sys.argv):
    import getopt

    short_args="h:"
    long_args=[
        "help",
    ]
    arguments = argv[1:]
    try:
        opts, args = getopt.getopt(arguments, short_args, long_args)
    except:
        usage()

    for option, value in opts:
        if option in ('-h', '--help'):
            usage()

    start_app()

if __name__=='__main__':
    main()
