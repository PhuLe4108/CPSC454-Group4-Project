import socket
import time
import mysql.connector

def verify_otp_with_server(otp):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 9999))
        client.sendall(b"verify_otp")  # Inform server of the operation type
        time.sleep(0.1)  # Small delay to ensure separate TCP packets
        client.sendall(otp.encode())  # Send the actual OTP
        response = client.recv(1024).decode()  # Receive the response
        return response
    
def database_connection():
    #TODO: Make sure to change the host, user, password, and database parameters 
    database = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )
    ########

    mycursor = database.cursor()

    #TODO: Run your mysql query here to get the user's resource
    mycursor.execute("SELECT * FROM user") #example
    queryResult = mycursor.fetchall()
    return queryResult

def main():
    otp_input = input("Please enter the OTP you received: ").strip()
    response = verify_otp_with_server(otp_input)
    print(f"Server response: {response}")

    if response == "Token verified successfully!":
        db_resource = database_connection()

    print(f"Here is your resource:\n{db_resource}")


if __name__ == "__main__":
    main()
