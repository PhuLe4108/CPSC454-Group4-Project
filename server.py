import socket
import pyotp

def main():
    # Create a fixed secret key for the TOTP generator
    secret = 'S3KRE7BZNF6FQOKJ'
    # Initialize the TOTP generator with the secret key
    totp = pyotp.TOTP(secret)
    print("Server ready with fixed secret.")

    # Set up a socket server on local host and port 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(1)
    print("Server is listening on port 9999")

    # Continuously listen for clients to connect
    while True:
        client, addr = server.accept()  # Accept a new client connection
        print(f"Connected with {addr}")

        # Handle operations after a client has connected
        while True:
            # Receive data from the client, up to 1024 bytes
            operation = client.recv(1024).decode().strip()
            # If no data is received, exit the inner loop to wait for a new client
            if not operation:
                break

            # If the operation is to send an OTP
            if operation == "send_otp":
                # Generate a new OTP token
                token = totp.now()
                print(f"Sent OTP to client: {token}")
                # Send the OTP token back to the client
                client.sendall(token.encode())
            # If the operation is to verify an OTP
            elif operation == "verify_otp":
                # Receive the OTP token from the client
                received_token = client.recv(1024).decode().strip()
                print(f"Received token for verification: {received_token}")
                # Verify the OTP token
                if totp.verify(received_token):
                    response = "Token verified successfully!"
                else:
                    response = "Invalid token."
                # Send the verification result back to the client
                client.sendall(response.encode())
        
        # Close the client connection before waiting for a new client
        client.close()

if __name__ == "__main__":
    main()
