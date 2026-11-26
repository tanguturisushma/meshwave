import socket
import cloudpickle
task = {    "task_id": 101,    "task_name": "Data Processing",    "priority": "High"}
# Convert Python data into bytes
data = cloudpickle.dumps(task)
client = socket.socket()
client.connect(("127.0.0.1", 500))
# Send bytes to Peer B
client.sendall(data)
print("Task sent successfully!")
client.close()
