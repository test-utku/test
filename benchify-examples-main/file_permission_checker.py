
import os
import stat

def check_world_writable_files(start_path="/app"):
    findings = []
    for root, dirs, files in os.walk(start_path):
        for name in files:
            full_path = os.path.join(root, name)
            try:
                mode = os.stat(full_path).st_mode
                if mode & stat.S_IWOTH:
                    findings.append(full_path)
            except Exception:
                continue
    return findings

if __name__ == "__main__":
    results = check_world_writable_files()
    for path in results:
        print(f"[!] World-writable file: {path}")
