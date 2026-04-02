import json, platform

### psutil check
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
    print("Warning: psutil not installed.")

### get info via platform
platform = {
    "system": platform.system(),
    "node": platform.node(),
    "release": platform.release(),
    "version": platform.version(),
    "machine": platform.machine(),
    "processor": platform.processor(),
}


data = {
    "cores": psutil.cpu_count(),
    "ram": psutil.virtual_memory().total
}


platform = platform | data
print(json.dumps(platform, indent=2))
