#An API sometimes fails due to network delays.
#Write a program to retry the API call 3 times until the response code becomes 200.
#If it still fails after 3 tries, print a failure message.
#Hint: Use a while loop with a counter.
#Expected Output Example:
#Attempt 1: Response 500
#Attempt 2: Response 200
#✅ Test Passed

#Initialization
attempt = 1
max_attempt = 3

#Condition
while attempt <= max_attempt:
    response = int(input("Enter status code response: "))
    if response == 200:
        print("✅ Test Passed")
        break
    else:
        if attempt < max_attempt:
         print("❌ Error status, try again!")

        #Updation
        attempt = attempt + 1

if response != 200:
    print("❌ Test Failed after 3 attempts.")

"""
attempt = 1
max_attempt = 3
success = False  # We use this to remember if kid guessed correctly

while attempt <= max_attempt:
    try:
        response = int(input("Enter status code response: "))
    except:
        print("Please enter numbers only!")
        continue  # ask again without losing an attempt

    if response == 200:
        print("✅ Test Passed")
        success = True
        break
    else:
        print("❌ Wrong number, try again!")
        attempt = attempt + 1

if not success:
    print("❌ Test Failed after 3 attempts.")
    """


