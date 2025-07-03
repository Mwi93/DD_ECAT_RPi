# Direct Drive Sim Racing Wheel with Raspberry Pi 4, SimHub, EtherCAT, and USB FFB

## Features
- Real-time motor control using EtherCAT (SOEM)
- USB HID gadget presenting wheel axis + FFB
- Game telemetry from SimHub (UDP)
- Sends torque commands, receives encoder position

## Setup
1. Build EtherCAT driver:
    cd ethercat_motor
    make
2. Setup USB gadget:
    sudo python3 usb_ff_gadget.py
3. Start integration:
    python3 main.py

Make sure you have SOEM installed and an RT kernel.
