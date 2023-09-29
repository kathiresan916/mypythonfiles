"""Generate OTP using Authenticator App"""

import time
import pyotp

secret = pyotp.random_base32()  # Generate a random secret key.

totp = pyotp.TOTP(secret)  # Create TOTP Object

token = totp.now()  # Get Currect TOTP Token

print("Current Token is: ", token)

# Sleep time, it will automatically generate next OTP within the time frame
time.sleep(30)

new_token = totp.now()  # Get and store the TOTP token in this object

print("New Token is: ", new_token)
