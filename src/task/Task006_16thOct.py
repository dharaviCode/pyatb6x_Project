# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
#
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

# Input : API response code
response = int(input("Response code received: "))

# Check if the response is successful
if 200 < response < 505:

    if response == 200:
        print("Status: OK")
    elif response == 201:
        print("Status: Resource created!")
    elif response == 400:
        print("Status: Bad request")
    elif response == 401:
        print("Status: Unauthorized")
    elif response == 403:
        print("Status: Forbidden")
    elif response == 405:
        print("Status: Method Not Allowed")
    elif response == 409:
        print("Status: Conflict")
    elif response == 429:
        print("Status: Too Many Requests")
    else:
        print("Status: Internal Server Error")

else:
 print("Status: Unknown Error")





