#!/usr/bin/env python3

import json
import os
import platform
import shutil
import socket
from datetime import datetime


def collect_system_information():
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
        "Disk Total (GB)": round(total / (1024 ** 3), 2),
        "Disk Used (GB)": round(used / (1024 ** 3), 2),
        "Disk Free (GB)": round(free / (1024 ** 3), 2),
        "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def display_report(info):
    print("=" * 65)
    print("              BlueTeam System Inspector v1.0")
    print("=" * 65)

    print("\n[ SYSTEM INFORMATION ]\n")

    for key in [
        "Hostname",
        "Operating System",
        "OS Version",
        "Platform",
        "Kernel",
        "Architecture",
        "Processor",
        "Python Version",
        "Current User"
    ]:
        print(f"{key:<20}: {info[key]}")

    print("\n[ STORAGE ]\n")

    for key in [
        "Disk Total (GB)",
        "Disk Used (GB)",
        "Disk Free (GB)"
    ]:
        print(f"{key:<20}: {info[key]}")

    print("\n[ REPORT ]\n")

    print(f"{'Generated At':<20}: {info['Generated At']}")

    print("\n" + "=" * 65)


def export_txt(info):
    with open("reports/system_report.txt", "w") as file:

        file.write("BlueTeam System Inspector v1.0\n")
        file.write("Linux Security Workstation Project\n")
        file.write("=" * 65 + "\n\n")

        for key, value in info.items():
            file.write(f"{key:<20}: {value}\n")


def export_json(info):
    with open("reports/system_report.json", "w") as file:
        json.dump(info, file, indent=4)


def main():

    info = collect_system_information()

    display_report(info)

    export_txt(info)

    export_json(info)

    print("\nReports generated successfully.")
    print("TXT  : reports/system_report.txt")
    print("JSON : reports/system_report.json")


if __name__ == "__main__":
    main()