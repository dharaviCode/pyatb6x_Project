import pytest
import allure

@allure.title("TC1 - Verify the 2-2 = 0")
@allure.description("this is a smoke test that test that checks the 2-2")
@pytest.mark.smoke
def test_sub0():
    assert 2-2 == 0

@allure.title("TC2 - Verify the 5-5 = 0")
@allure.description("this is a regression test that test that checks the 5-5")
@pytest.mark.regression
def test_sub1():
    assert 5-5 == 0

@allure.title("TC3 - Verify the 0-0 = 0")
@allure.description("this is a smoke test that test that checks the 0-0")
@pytest.mark.skip(reason="this is out-of-scope requirement, so skip this test")
def test_sub3():
    assert 0-0 == 0

