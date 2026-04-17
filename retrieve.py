import socket
import os
import subprocess

hostname = socket.gethostname()
print("Hostname: " + hostname)
output = None

if os.name == "nt":
    print("Windows system...")
    output = subprocess.check_output(['msinfo32', '/nfo', f'{hostname}.nfo'], text=True)
elif os.name == "posix":
    print("POSIX system...")
    subprocess.run(f"sudo lshw -xml > {hostname}.xml", shell=True, check=True)

print(output)