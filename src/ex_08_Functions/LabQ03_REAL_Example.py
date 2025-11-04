#Define/Declare
def validate_status_code(response_code):
  if response_code > 0:
    if response_code == 200:
        print("200 OK")

    else:
        print("Error code:", response_code)

  else:
      print("Wrong response code value")

#Calling
validate_status_code(200)
validate_status_code(404)
validate_status_code(500)
validate_status_code(501)
validate_status_code(int(input("enter the status_code: ")))

