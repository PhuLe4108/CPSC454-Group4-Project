import tkinter as tk
import socket
import time

# Function to send OTP to the server and get the response
def verify_otp_with_server(otp):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # Replace localhost with IP address of the machine running server.py
        client.connect(('localhost', 9999))  # Connect to server on port 9999
        client.sendall(b"verify_otp")  # Inform server of the operation type
        time.sleep(0.1)  # Small delay to ensure separate TCP packets
        client.sendall(otp.encode())  # Send the OTP to the server
        response = client.recv(1024).decode()  # Receive the server's response
        return response

# Function to handle OTP submission
def submit_otp():
    otp = otp_entry.get()  # Get OTP from the input field
    response = verify_otp_with_server(otp)  # Verify OTP with server
    otp_response_label.config(text=f"{response}")  # Display response

# Function to handle login submission
def submit_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check hardcoded login credentials
    if username == "admin" and password == "admin":
        login_frame.pack_forget()  # Hide the login frame
        otp_frame.pack()  # Show the OTP frame
    else:
        login_response_label.config(text="Invalid username or password")  # Display error

# Create the main Tkinter window
root = tk.Tk()
root.title("Login and OTP Verification")

# Create the login frame
login_frame = tk.Frame(root)
login_frame.pack(padx=10, pady=10)

# Create and place the login widgets
login_label = tk.Label(login_frame, text="Please login")
login_label.pack()

username_label = tk.Label(login_frame, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_frame, width=20)
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_frame, width=20, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=submit_login)
login_button.pack(pady=5)

login_response_label = tk.Label(login_frame, text="")
login_response_label.pack(pady=10)

# Create the OTP frame
otp_frame = tk.Frame(root)
otp_frame.pack_forget()  # Hide OTP frame initially

# Create and place the OTP widgets
otp_label = tk.Label(otp_frame, text="Please enter the OTP you received:")
otp_label.pack()

otp_entry = tk.Entry(otp_frame, width=20)
otp_entry.pack(pady=5)

otp_submit_button = tk.Button(otp_frame, text="Submit OTP", command=submit_otp)
otp_submit_button.pack(pady=5)

otp_response_label = tk.Label(otp_frame, text="")
otp_response_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
