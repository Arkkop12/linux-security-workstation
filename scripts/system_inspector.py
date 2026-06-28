#!/usr/bin/env python3

import os
import platform


def get_hostname():
    return platform.node()


def get_os():
    return platform.platform()


def get_kernel():
    return platform.release()


def get_architecture():
    return platform.machine()


def get_current_user():
    return os.getenv("USER")


def main():
    print("=" * 50)
    print("BlueTeam System Inspector")
    print("=" * 50)

    print(f"Hostname         : {get_hostname()}")
    print(f"Operating System : {get_os()}")
    print(f"Kernel           : {get_kernel()}")
    print(f"Architecture     : {get_architecture()}")
    print(f"Current User     : {get_current_user()}")

    print("=" * 50)


if __name__ == "__main__":
    main()