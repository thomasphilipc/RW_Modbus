from threading import Timer,Thread,Event
from time import sleep
import datetime
import Queue
import sys

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

    q = Queue()
    t = perpetualTimer(5, task1)
    t1 = perpetualTimer(10, task2)
    t.start(q)
    t1.start(q)

    while True:
        global now
        now = datetime.datetime.now()
        print(" {}:{}:{} : 1 sec timer".format(now.hour,now.minute,now.second))
        sleep(1)
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
    logconfig('info')	#set log level，such as"info"
    #instantiates a startWork object and start event loop or invoke start_app() directly
    start_app()

if __name__=='__main__':
    main()
