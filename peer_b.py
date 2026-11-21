import socket
import cloudpickle
server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(1)
print("Peer B waiting for connection...")
conn, address = server.accept()
print("Connected with:", address)
data = conn.recv(100000)
task = cloudpickle.loads(data)
print("Received Task:", task)
conn.close()
server.close()
