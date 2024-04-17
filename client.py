import socket
import time

def get_otp_from_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 9999))
        client.sendall(b"send_otp")
        otp = client.recv(1024).decode()
        return otp

def main():
    while True:
        otp = get_otp_from_server()
        print(f"Received OTP from server: {otp}")
        time.sleep(30)  # Wait for 30 seconds before requesting a new OTP

if __name__ == "__main__":
    main()
