import pytest


@pytest.mark.smoke  #Marking the test case as smoke/sanity/regression (This will populate in console if fails)
def test_method1():
    print("Hello World")
    assert 5 == 6    #Check expected result with actual result

@pytest.mark.smoke
def test_method2():
    print("Hello World")
    assert 5 == 5