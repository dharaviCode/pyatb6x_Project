import pytest
import allure
import requests

@allure.title("TC1 - Token generation validation")
@allure.description("TC1 - Verify Token generation validation")

@pytest.mark.token
def test_create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    full_url = base_url + base_path
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)
    print(response_data)
    assert response_data.status_code == 200 #1st step validation

    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)

    assert type(token) == str #2nd step validation
    assert len(token) > 0     #3rd step validation





