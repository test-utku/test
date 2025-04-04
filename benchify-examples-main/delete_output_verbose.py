
import os
import datetime
import platform
import socket
import logging
import time

def get_system_context():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "timestamp": datetime.datetime.now().isoformat()
    }

def initialize_logging(log_file="/tmp/delete_output_log.txt"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("==== File Deletion Script Started ====")

def delete_files_in_directory(target_directory="/app/output/"):
    deleted_files = []
    skipped_entries = []
    errors = []
    logging.info(f"Scanning target directory: {target_directory}")

    if not os.path.exists(target_directory):
        logging.warning(f"Target directory does not exist: {target_directory}")
        return deleted_files, skipped_entries, errors

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                os.remove(full_path)
                logging.info(f"Deleted file: {full_path}")
                deleted_files.append(full_path)
            except PermissionError as pe:
                logging.warning(f"Permission denied for: {full_path}")
                skipped_entries.append((full_path, "PermissionError"))
                errors.append(str(pe))
            except Exception as e:
                logging.error(f"Error deleting {full_path}: {e}")
                skipped_entries.append((full_path, "OtherError"))
                errors.append(str(e))
        time.sleep(0.1)  # simulate workload

    logging.info(f"Completed scanning. Total deleted files: {len(deleted_files)}")
    return deleted_files, skipped_entries, errors

def write_summary(deleted_files, skipped_entries, errors, summary_file="/tmp/delete_summary.txt"):
    with open(summary_file, "w") as f:
        f.write("=== File Deletion Summary ===\n")
        f.write(f"Deleted Files ({len(deleted_files)}):\n")
        for file in deleted_files:
            f.write(f"  - {file}\n")

        f.write(f"\nSkipped Entries ({len(skipped_entries)}):\n")
        for entry, reason in skipped_entries:
            f.write(f"  - {entry} ({reason})\n")

        f.write(f"\nErrors ({len(errors)}):\n")
        for error in errors:
            f.write(f"  - {error}\n")

    logging.info(f"Summary written to: {summary_file}")

def main():
    system_info = get_system_context()
    print("System Context:")
    for k, v in system_info.items():
        print(f"  {k}: {v}")

    initialize_logging()
    target_dir = "/app/output/"
    deleted, skipped, errs = delete_files_in_directory(target_dir)
    write_summary(deleted, skipped, errs)

    print(f"Script completed. Deleted {len(deleted)} file(s).")

if __name__ == "__main__":
    main()
