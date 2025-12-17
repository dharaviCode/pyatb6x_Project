import allure
import pytest

@allure.title("Verify that create booking is working for valid data")
@allure.description("This test case check for positive scenario of bookings")
@pytest.mark.positve
def test_create_booking_positive():
    print("test1")
    assert 1+1 == 2


@allure.title("Verify that create booking is working for invalid data")
@allure.description("This test case check for negative scenario of bookings")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1-1 == 2


@allure.title("Verify that create booking is working for empty data")
@allure.description("This test case check for negative/empty scenario of bookings")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test3")
    assert 1+1 == 2



