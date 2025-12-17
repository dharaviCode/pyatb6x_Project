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
    print(response_data.status_code)
    #print(response_data.json())
    print(response_data.text)
    assert response_data.status_code == 200

