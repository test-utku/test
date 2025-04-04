
import os
import datetime
import socket
import platform

def get_system_info():
    info = {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "platform-release": platform.release(),
        "platform-version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "time": datetime.datetime.now().isoformat()
    }
    return info

def list_directory_contents(target_path="/app/repo/"):
    file_count = 0
    dir_count = 0
    summary = []

    print("=" * 60)
    print(f"Scanning directory structure under: {target_path}")
    print("=" * 60)

    for root, dirs, files in os.walk(target_path):
        level = root.replace(target_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}[DIR] {os.path.basename(root)}/")
        dir_count += 1

        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            file_path = os.path.join(root, f)
            try:
                size = os.path.getsize(file_path)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                print(f"{sub_indent}- {f} ({size} bytes, modified: {mtime})")
                summary.append((file_path, size, mtime))
                file_count += 1
            except Exception as e:
                print(f"{sub_indent}- {f} (error reading file: {e})")

    print("\nSummary:")
    print(f"Total directories: {dir_count}")
    print(f"Total files: {file_count}")
    return summary

def save_summary_to_file(summary, output_file="/tmp/listing_summary.txt"):
    with open(output_file, "w") as f:
        for path, size, mtime in summary:
            f.write(f"{path}, {size} bytes, modified: {mtime}\n")
    print(f"\n[INFO] Summary saved to: {output_file}")

def main():
    system_info = get_system_info()
    print("[INFO] System Information:")
    for k, v in system_info.items():
        print(f"  {k}: {v}")
    print("\n")

    target_directory = "/app/repo/"
    summary = list_directory_contents(target_directory)
    save_summary_to_file(summary)

if __name__ == "__main__":
    main()
