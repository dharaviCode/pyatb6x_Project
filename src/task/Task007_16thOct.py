# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "

expected_title = "Dashboard"
#actual_title = "dashboard" - Fail
actual_title = "Dashboard"  # - Pass

if expected_title.strip().lower() == actual_title.strip().lower():
    print("Test passed!")
else:
    print("Test failed!")