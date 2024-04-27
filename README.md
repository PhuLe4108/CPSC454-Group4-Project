# CPSC454-Group4-Project

**Project name:** Multi-factor Authentication (MFA) Service<br>

**Team members:**
  - Tung Nguyen, duytung7@csu.fullerton.edu
  - Gustavo Couto Vanin, gvanin@csu.fullerton.edu
  - Saakshi Parikh, saakshi20@csu.fullerton.edu
  - Andrew Kang, andrew.kang1209@csu.fullerton.edu
  - Mike Thai, miket126@csu.fullerton.edu
  - Daniel Le, PhuLe4108@csu.fullerton.edu
  - Kiet Hoang, kiethoang1411@csu.fullerton.edu

**Usage**
Server - authentication server, generate OTP
_replace 'localhost' in the file with the IP of the authentication server
_run 'python3 server.py' in the terminal

Client - front end of authentication server, displaying the OTP
_replace 'localhost' in the file with the IP of the authentication server
_run 'python3 client.py' in the terminal

endUserValidateOTP - a resource/application that use authentication server as MFA
_replace 'localhost' in the file with the IP of the authentication server
_run 'python3 endUserValidateOTP.py' in the terminal
_enter 'admin' for both username and password
_wait for the next OTP from client and enter the code to be verified
