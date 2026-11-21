import psutil
# CPU Monitoring
cpu = psutil.cpu_percent(interval=1)
# RAM Monitoring
ram = psutil.virtual_memory()
print("CPU Usage:", cpu, "%")
print("RAM Usage:", ram.percent, "%")
print("Total RAM:",      round(ram.total / (1024**3), 2), "GB")
print("Available RAM:",      round(ram.available / (1024**3), 2), "GB")
print("Used RAM:",      round(ram.used / (1024**3), 2), "GB")
