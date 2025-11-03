# Check if the user can log in based on correct username and password.
#
# I/p
#
# username = "admin"
# password = "1234"
#
# O/p
# ✅ Login Successful
#
#
# For the Fail condition Other O/P = ❌ Invalid Credentials

username = input("enter your username: ").strip ()
password = input("enter your password: ").strip()

if username == "admin" and password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")