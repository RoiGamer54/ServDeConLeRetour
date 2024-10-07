import platform
import psutil
from django.http import JsonResponse

def MachineStatusView(request):
    system_info = get_system_info()
    system_info["cpu_info"] = get_cpu_info()
    system_info["ram_info"] = get_ram_info()
    system_info["os_info"] = get_os_info()
    system_info["disk_usage"] = get_disk_usage()
    return JsonResponse(system_info)

def get_system_info():
    """Récupération des informations système via psutil."""
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "architecture": platform.architecture(),
        "uptime": get_uptime(),
    }

def get_cpu_info():
    """Récupérer les informations sur le processeur avec psutil."""
    cpu_freq = psutil.cpu_freq(percpu=True)
    temps = psutil.sensors_temperatures() if hasattr(psutil, 'sensors_temperatures') else {}
    
    cpu_info = {
        "model": platform.uname(),
        "cores": psutil.cpu_count(logical=False),  # Nombre de cœurs physiques
        "logical_cores": psutil.cpu_count(logical=True),  # Nombre de cœurs logiques
        "usage_per_core": psutil.cpu_percent(percpu=True),  # Utilisation par cœur
        "total_usage": psutil.cpu_percent(),  # Utilisation totale du CPU
        "frequency_per_core": [freq.current for freq in cpu_freq] if cpu_freq else [],
        "temperature_per_core": temps.get('coretemp', [{"current": None}])[0]["current"] if temps else "N/A",
    }
    return cpu_info

def get_ram_info():
    """Récupérer les informations de la RAM via psutil."""
    virtual_memory = psutil.virtual_memory()
    return {
        "total_installed": virtual_memory.total / (1024 ** 3),  # Convertir en Go
        "used": virtual_memory.used / (1024 ** 3),  # Utilisé en Go
        "free": virtual_memory.free / (1024 ** 3),  # Libre en Go
        "percent_used": virtual_memory.percent,
    }

def get_os_info():
    """Récupérer les informations sur le système d'exploitation et le modèle."""
    return {
        "os_type": platform.system(),
        "machine_model": platform.machine(),
        "node_name": platform.node(),
        "uptime": get_uptime(),
    }

def get_uptime():
    """Récupérer le temps d'activité (uptime) en heures."""
    boot_time_timestamp = psutil.boot_time()
    uptime_seconds = (psutil.time.time() - boot_time_timestamp)
    uptime_hours = uptime_seconds / 3600
    return uptime_hours

def get_disk_usage():
    """Récupérer les informations d'utilisation des disques avec psutil."""
    disk_usage_info = {}
    partitions = psutil.disk_partitions()

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage_info[partition.device] = {
            "total": usage.total / (1024 ** 3),  # Convertir en Go
            "used": usage.used / (1024 ** 3),
            "free": usage.free / (1024 ** 3),
            "percent": usage.percent,
        }
    return disk_usage_info