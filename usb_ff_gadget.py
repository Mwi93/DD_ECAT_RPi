import os

def setup_usb_ff():
    os.system("modprobe libcomposite")
    os.makedirs("/sys/kernel/config/usb_gadget/g1", exist_ok=True)
    with open("/sys/kernel/config/usb_gadget/g1/idVendor", "w") as f:
        f.write("0x1d6b")
    with open("/sys/kernel/config/usb_gadget/g1/idProduct", "w") as f:
        f.write("0x0104")
    # Additional descriptor and function setup omitted for brevity