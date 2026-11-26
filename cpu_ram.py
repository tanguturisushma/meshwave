import psutil


def get_resource_usage():
    """Collect CPU and RAM usage information."""

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()

    resources = {
        "CPU Usage": cpu,
        "RAM Usage": ram.percent,
        "Total RAM": round(ram.total / (1024 ** 3), 2),
        "Available RAM": round(ram.available / (1024 ** 3), 2),
        "Used RAM": round(ram.used / (1024 ** 3), 2)
    }

    return resources


def display_resource_usage(resources):
    """Display system resource information."""

    print("\n===== SYSTEM RESOURCE MONITOR =====")

    for name, value in resources.items():
        unit = " GB" if "RAM" in name and name != "RAM Usage" else "%"
        print(f"{name}: {value}{unit}")

    print("===================================")


if __name__ == "__main__":
    try:
        resource_data = get_resource_usage()
        display_resource_usage(resource_data)

    except Exception as error:
        print("Error monitoring system resources:", error)