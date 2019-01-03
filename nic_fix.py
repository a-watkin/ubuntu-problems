import subprocess

subprocess.Popen(["sudo", "ifconfig", "eno1", "up"])


subprocess.Popen(["sudo", "ifconfig", "eno1", "192.168.0.15", "netmask", "255.255.255.0"])

subprocess.Popen(["sudo", "ifconfig", "eno1", "192.168.0.15", "netmask", "255.255.255.0"])

subprocess.Popen(["sudo", "route", "add", "default", "gw", "192.168.0.1", "eno1"])

# subprocess.Popen(["echo", '"nameserver 8.8.8.8"', ">", "/etc/resolv.conf"])

