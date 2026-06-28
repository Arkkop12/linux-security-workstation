#!/usr/bin/env python3

import json
import os
import platform
import shutil
import socket
from datetime import datetime


def get_system_information():
    total, used, free = shutil.disk_usage("/")

    return {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Platform": platform.platform(),
        "Kernel": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Current User": os.getenv("USER"),
        "Disk Total (GB)": round(total / (1024**3), 2),
        "Disk Used (GB)": round(used / (1024**3), 2),
        "Disk Free (GB)": round(free / (1024**3), 2),
        "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def print_report(info):
    print("=" * 60)
    print("        BlueTeam System Inspector v1.0")
    print("=" * 60)

    for key, value in info.items():
        print(f"{key:<20}: {value}")

    print("=" * 60)


def save_txt(info):
    with open("reports/system_report.txt", "w") as file:
        file.write("BlueTeam System Inspector v1.0\n")
        file.write("=" * 60 + "\n")

        for key, value in info.items():
            file.write(f"{key:<20}: {value}\n")


def save_json(info):
    with open("reports/system_report.json", "w") as file:
        json.dump(info, file, indent=4)


def main():
    info = get_system_information()

    print_report(info)

    save_txt(info)

    save_json(info)

    print("\n[+] Report exported successfully.")
    print("[+] TXT  : reports/system_report.txt")
    print("[+] JSON : reports/system_report.json")


if __name__ == "__main__":
    main()