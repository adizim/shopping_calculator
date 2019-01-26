import calculator
import pytest

""" Test calculator.py """

def test_calculator():
    assert calculator.main(['', "examples/cart-4560.json", "examples/base-prices.json"]) == 4560
    assert calculator.main(['', "examples/cart-9363.json", "examples/base-prices.json"]) == 9363
    assert calculator.main(['', "examples/cart-9500.json", "examples/base-prices.json"]) == 9500
    assert calculator.main(['', "examples/cart-11356.json", "examples/base-prices.json"]) == 11356

def test_extract_json():
    assert isinstance(calculator.extract_json("examples/base-prices.json"),list)
    with pytest.raises(FileNotFoundError):
        calculator.extract_json("none.json")
        calculator.extract_json(None)


