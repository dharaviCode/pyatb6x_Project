#Simulate a page loading check using a while loop.
#If page_loaded becomes True within 5 seconds, print success; else timeout.
#Hint: Use a counter (like wait_time) and break condition.

#Writing this code without use of function (def) , sleep()
#Initialization
"""
page_loaded = False
wait_time = 1
max_time = 5

#Condition
while wait_time <= max_time:
    print("Checking... second:", wait_time)
    user_input = input("Has the page loaded? (yes/no): ").strip().lower()

    if user_input == "yes":
        page_loaded = True
        print("✅ Page loaded successfully in", wait_time, "seconds.")
        break
    else:
        if wait_time < max_time:
         print("❌ Not loaded yet...")
     #Updation
    wait_time = wait_time + 1

if page_loaded == False:
    print("❌ Timeout: Page did not load within 5 seconds.")
    """
#Using the functions and sleep()
import time
import random

wait_time = 0
page_loaded = False


def api_response():
    return random.choice([False, True])


while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        print(f"⏳ Checking... (second {wait_time + 1})")
        time.sleep(1)  # wait for 1 second
        wait_time += 1

if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")
