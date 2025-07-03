from simhub_udp import receive_force_value
from ctypes import CDLL
from input_report import send_position_report
import time

ecat = CDLL("./ethercat_motor/libethercat_motor.so")
ec_init = ecat.init_motor
send_torque = ecat.send_torque
ec_get_position = ecat.get_position

if __name__ == "__main__":
    if ec_init() == 0:
        print("Drive initialized.")
        while True:
            torque = next(receive_force_value())
            send_torque(1, torque)
            pos = ec_get_position(1)
            send_position_report(pos)
            time.sleep(0.01)
    else:
        print("Failed to init EtherCAT.")