import sys
import json
import itertools

""" calculator.py is a price calculator for shopping carts. """

def extract_json(file):
    """ Decodes the json from a file """
    with open(file) as f:
        res = json.loads(f.read())
    return res

def analyze_prices(prices):
    """ Returns a dictionary that maps product to a list of required options and 
    a dictionary that maps product-type to a dictionary that maps sorted required options to base price """
    required_options = dict()
    product_prices = dict()

    for product in prices:
        product_type = product['product-type']
        options = product['options']
        price = product['base-price']

        if product_type not in required_options:
            required_options[product_type] = [o for o in options]
        if product_type not in product_prices:
            product_prices[product_type] = dict()
        
        options_values = [options[o] for o in required_options[product_type]]
        combinations = itertools.product(*options_values)
        for option_combo in combinations:
            key = tuple(sorted(option_combo))
            product_prices[product_type][key] = price
    
    return required_options, product_prices

def sum_cart(cart, options_dict, prices_dict):
    """ Sums the products in the cart based on the mapping between a product's required options to its base price """
    result = 0

    for product in cart:
        product_type = product['product-type']
        options = product['options']
        markup = product['artist-markup']
        quantity = product['quantity']

        options_values = [options[o] for o in options_dict[product_type]]
        key = tuple(sorted(options_values))

        base_price = prices_dict[product_type][key]
        result += (base_price + round(base_price * (markup / 100))) * quantity
        
    return result

def main(args):
    assert len(args) == 3, "Two command line arguments required: <cart json file> <prices json file>"

    cartfile, pricefile = args[1], args[2]
    cart, prices = extract_json(cartfile), extract_json(pricefile)

    required_options, product_prices = analyze_prices(prices)
    total = sum_cart(cart, required_options, product_prices)

    return total

if __name__ == "__main__":
    total = main(sys.argv)
    print(total)