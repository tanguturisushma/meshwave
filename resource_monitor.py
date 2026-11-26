import psutil
def get_resource_status():    
    cpu = psutil.cpu_percent(interval=1)    
    ram = psutil.virtual_memory()    
    resources = {        
        "cpu_usage": cpu,        
        "ram_usage": ram.percent,       
        "available_memory": round(           
            ram.available / (1024**3), 2        
       )
    }
    return resources
status = get_resource_status()
print("Peer Resource Information:")
print(status)
# Information for Task Manager
task_manager_data = status
# Information for Gossip Protocol
gossip_data = status
print("\nTask Manager Data:", task_manager_data)
print("\nGossip Protocol Data:", gossip_data)
