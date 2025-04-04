import os
import platform
import time
import getpass
import subprocess

def get_os_type():
    os_type = platform.system().lower()
    if "linux" in os_type or "darwin" in os_type:
        return "unix"
    elif "windows" in os_type:
        return "windows"
    else:
        return "unknown"

def confirm_shutdown():
    print("=== SYSTEM SHUTDOWN REQUEST ===")
    print(f"User: {getpass.getuser()}")
    print("Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
    confirm = input("Do you really want to shut down this machine? (yes/no): ")
    return confirm.lower() == "yes"

def perform_shutdown():
    os_type = get_os_type()
    print(f"[INFO] Detected OS type: {os_type}")

    if os_type == "unix":
        command = ["/sbin/shutdown", "-h", "now"]
    elif os_type == "windows":
        command = ["shutdown", "/s", "/t", "0"]
    else:
        print("[ERROR] Unsupported OS. Cannot proceed with shutdown.")
        return

    try:
        print("[INFO] Executing shutdown command...")
        subprocess.run(command, check=True)
    except PermissionError:
        print("[ERROR] You need elevated privileges to shut down the system.")
    except Exception as e:
        print(f"[ERROR] An error occurred while trying to shut down: {e}")

def main():
    print("Initializing shutdown procedure...")
    time.sleep(1)

    if confirm_shutdown():
        print("[OK] Confirmation received. Preparing to shut down.")
        time.sleep(2)
        perform_shutdown()
    else:
        print("[CANCELLED] Shutdown aborted by user.")

if __name__ == "__main__":
    main()
