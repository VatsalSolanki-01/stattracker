import psutil
import time
import platform
from datetime import datetime

def get_system_stats():
    # System information
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
    }

    # CPU stats
    cpu_stats = {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "cpu_cores": psutil.cpu_count(logical=True),
    }

    # Memory stats
    memory = psutil.virtual_memory()
    memory_stats = {
        "total_memory_gb": round(memory.total / (1024 ** 3), 2),
        "used_memory_gb": round(memory.used / (1024 ** 3), 2),
        "memory_usage_percent": memory.percent,
    }

    # Disk stats
    disk = psutil.disk_usage('/')
    disk_stats = {
        "total_disk_gb": round(disk.total / (1024 ** 3), 2),
        "used_disk_gb": round(disk.used / (1024 ** 3), 2),
        "disk_usage_percent": disk.percent,
    }

    # Boot time
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = round(uptime_seconds / 3600, 2)

    uptime_stats = {
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": uptime_hours,
    }

    # Combine all
    stats = {
        "system": system_info,
        "cpu": cpu_stats,
        "memory": memory_stats,
        "disk": disk_stats,
        "uptime": uptime_stats,
    }

    return stats
