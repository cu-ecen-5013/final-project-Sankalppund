
from max30102 import MAX30102
import hrcalc
import threading
import time
import numpy as np

print("Script initiated")

try:
    class HeartRateMonitor(object):
        """
        A class that encapsulates the max30102 device into a thread
        """
        print("In Class")
        LOOP_TIME = 0.01
        print(time)
        def __init__(self):
            self.bpm = 0
            print(time)    
        def run_sensor(self):
            sensor = MAX30102()
            ir_data = []
            red_data = []
            bpms = []
            xyz = 1
            print(time)
    	    if xyz == 1:
                print("In While 1")
                print(time)
                num_bytes = sensor.get_data_present()
                print(num_bytes)

            # run until told to stop
            while not self._thread.stopped:
                # check if any data is available
                num_bytes = sensor.get_data_present()
    	    print(num_bytes)
                if num_bytes > 0:
                    # grab all the data and stash it into arrays
                    while num_bytes > 0:
                        red, ir = sensor.read_fifo()
                        num_bytes -= 1
                        ir_data.append(ir)
                        red_data.append(red)
                        print("IR: {0}, Red: {1}".format(ir, red))

                    while len(ir_data) > 100:
                        ir_data.pop(0)
                        red_data.pop(0)

                    if len(ir_data) == 100:
                        bpm, valid_bpm, spo2, valid_spo2 = hrcalc.calc_hr_and_spo2(ir_data, red_data)
                        if valid_bpm:
                            bpms.append(bpm)
                            while len(bpms) > 4:
                                bpms.pop(0)
                            self.bpm = np.mean(bpms)
                            if (np.mean(ir_data) < 50000 and np.mean(red_data) < 50000):
                                self.bpm = 0
                                print("Finger not detected")
                            print("BPM: {0}, SpO2: {1}".format(self.bpm, spo2))

                time.sleep(self.LOOP_TIME)

            sensor.shutdown()

        def start_sensor(self):
            self._thread = threading.Thread(target=self.run_sensor)
            self._thread.stopped = False
            self._thread.start()

        def stop_sensor(self, timeout=2.0):
            self._thread.stopped = True
            self.bpm = 0
            self._thread.join(timeout)

except Exception as e:
    print(e)