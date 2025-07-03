from fcntl import ioctl
import struct
import time

HID_REPORT_PATH = "/dev/hidg0"

def encode_position(raw_pos):
    norm = int((raw_pos / 32768.0) * 127)
    return max(min(norm, 127), -127) & 0xFF

def send_position_report(pos):
    try:
        with open(HID_REPORT_PATH, "wb") as f:
            report = struct.pack("BB", 0x01, encode_position(pos))
            f.write(report)
    except Exception as e:
        print("USB HID write error:", e)