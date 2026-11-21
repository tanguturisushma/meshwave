import cloudpickle
# Original task
task = {    "task_id": 101,    "task_name": "Data Processing",    "priority": "High",    "status": "Pending"}
# # Serialization
data = cloudpickle.dumps(task)
print("Original Task:", task)
print("\nSerialized Bytes:", data)
# Deserialization
received_task = cloudpickle.loads(data)
print("\nDeserialized Task:", received_task)

