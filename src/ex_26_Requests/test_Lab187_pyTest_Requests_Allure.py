import pytest
import allure
import requests

@allure.title("TC1 - Verify the GET request for valid endpoint")
@allure.description("Verify status code 200 for valid GET request")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200

@allure.title("TC2 - Verify the GET request for invalid endpoint")
@allure.description("GET request for invalid endpoint")
@allure.description("Verify status code 404 for invalid GET request")
@pytest.mark.negative
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 404