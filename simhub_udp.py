import socket, json

def receive_force_value():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 20777))
    while True:
        data, _ = sock.recvfrom(2048)
        try:
            packet = json.loads(data.decode())
            angle = packet.get("SteeringAngle", 0)
            torque = -int(angle * 10)
            yield torque
        except:
            continue