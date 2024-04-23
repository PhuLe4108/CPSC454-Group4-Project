import socket
import time

i = 0

def verify_cred(name, pssw):
    file = open("user.txt", "r")
    cred = file.read().splitlines()
    if cred[0] == name and cred[1] == pssw:
        return True
    
    print("Wrong username or password!")
    return False


def verify_otp_with_server(otp):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('192.168.142.4', 9999))
        client.sendall(b"verify_otp")  # Inform server of the operation type
        time.sleep(0.1)  # Small delay to ensure separate TCP packets
        client.sendall(otp.encode())  # Send the actual OTP
        response = client.recv(1024).decode()  # Receive the response
        return response
    

def main():
    name = input("Username: ")
    pssw = input("Password: ")
    if verify_cred(name, pssw):
        otp_input = input("Please enter the OTP you received: ").strip()
        response = verify_otp_with_server(otp_input)
        print(f"Server response: {response}")

        if response == "Token verified successfully!":
            print(f"Access Granted\n")


    

if __name__ == "__main__":
    main()
