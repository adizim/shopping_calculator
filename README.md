# Description
calculator.py is a price calculator for shopping carts. It takes in two JSON files as command line arguments:
1. JSON file representing a cart
2. JSON file representing a list of base prices
and returns the total price of the cart in cents.

It requires python3, and pytest if you are interested in the automated tests.

## Usage

`python3 calculator.py <path/to/cart> <path/to/pricesfile>`

The cart file must be first and the prices file must be second. You can find example JSON files in the example folder.

## Assumptions
calculator.py takes several important assumptions
* JSON files are valid
* JSON files have valid relationships between each other
* Product options are constant

## Run tests
Run 
`pytest`
in project folder