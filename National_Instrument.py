import nidaqmx
from math import*
import time
while True:
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan('Dev1/ao0', 'mychannel', 0, 5)
        a = 0
        while True:
            if a>=0:
                while a <= 4.9:
                    a += 0.1
                    print(task.write(a))
                    time.sleep(0.2)
                while a>= 0.1:
                    a-=0.1
                    print(task.write(a))
                    time.sleep(0.5)
        task.stop()
        time.sleep(0.5)
