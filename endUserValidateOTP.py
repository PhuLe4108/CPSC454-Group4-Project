import socket
import time

def verify_otp_with_server(otp):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 9999))
        client.sendall(b"verify_otp")  # Inform server of the operation type
        time.sleep(0.1)  # Small delay to ensure separate TCP packets
        client.sendall(otp.encode())  # Send the actual OTP
        response = client.recv(1024).decode()  # Receive the response
        return response

def main():
    otp_input = input("Please enter the OTP you received: ").strip()
    response = verify_otp_with_server(otp_input)
    print(f"Server response: {response}")

if __name__ == "__main__":
    main()
