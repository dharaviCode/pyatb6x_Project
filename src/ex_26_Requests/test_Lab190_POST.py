import pytest
import allure
import requests

@allure.title("TC1 - Create booking CRUD postive")
@allure.description("Verify the create booking")

@pytest.mark.crud
def test_create_booking_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {
        "Content-Type": "application/json",   #Headres will be given as a key value pair
    }

    payload =  {           #Original JSON body can be kept here as a payload
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,  #True (with capital T will be supported)
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url,headers=headers,json=payload )
    assert response_data.status_code == 200
    time = response_data.elapsed.total_seconds()
    print(time)
    assert time < 3
    print(response_data.status_code)
    response_data = response_data.json()

    print(response_data)

    #BookingID > 0 and firstname - Jim
    bookingId = response_data["bookingid"]
    print(bookingId)
    firstName = response_data["booking"]["firstname"]
    print(firstName)

    assert bookingId is not None
    assert bookingId > 0
    assert type(bookingId) == int

    assert firstName == 'Jim'
    assert type(firstName) == str

    lastName = response_data["booking"]["lastname"]
    totalPrice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]

    assert lastName == 'Brown'
    assert totalPrice == 111
    assert depositpaid == True

    # https: // jsonpathfinder.com
    # x.booking.bookingdates.checkin
    # response_data_json["booking"]["bookingdates"]["checkin"]

    checkin = response_data["booking"]["bookingdates"]["checkin"]
    checkout = response_data["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"



@allure.title("TC2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
   base_url = "https://restful-booker.herokuapp.com"
   base_path = "/booking"
   URL = base_url + base_path
   headers = {"Content-Type": "application/json"}
   json_payload = {}
   response = requests.post(url=URL, headers=headers, json=json_payload)
   assert response.status_code == 500
   print(response.status_code)
   assert response.text == "Internal Server Error"







