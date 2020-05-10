import csv


# Valuation Service
#
# Three csv files (data.csv, currencies.csv, matchings.csv) are required to run program
#
# Program is reading data.csv and selecting this one which quantity * price is the highest.
# How many products from every matching_id will be saved in end file top_priced_count is determinate by top_priced_count
# from matchings.csv
#


# Function to read data from csv file
#
# input -  path where file is saved
# output - reading data as Dict or -1 when file weren't found

def read_csv_file(path):

    try:
        with open(path, 'r', newline='') as csvfile:
            ret = csv.DictReader(csvfile)
            return [n for n in ret]
    except FileNotFoundError:
        return -1

#  Function to save data into csv file as Dict
#
# input data in Dict format and path where file will be save

def save_to_csv(data, path):
    try:
        with open(path, 'a+', newline='') as csvfile:
            csvfile.truncate(0)
            fieldnames = ['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count']
            ret = csv.DictWriter(csvfile, fieldnames=fieldnames)
            ret.writeheader()
            for row in data:
                ret.writerow(row)
            return 0
    except Exception:
        return -1

# Function is finding highest value in every matching_id products and select n items, then call function to save as csv
# n - top_priced_count read from matchings.csv
#


def Valuation_service():

    # Read data from data.csv to data variable
    data = read_csv_file('data.csv')
    # Read data from matching.csv to matching variable
    matching = read_csv_file('matchings.csv')
    if data == -1 or matching == -1:
        raise Exception("Cannot read from File")
    data_to_save = []

    # loop to select matching_id and top_prices_count from matching
    for i, match_item in enumerate(matching):
        highest_price = 0  # highest price in matching_id products
        total_price = 0  # total price in current matching_id products
        data_counter = 0  # counter how many item is with correct matching_id
        price = 0  # This is value of price * quantity
        currency = ''
        # loop to select data line from data
        for data_item in data:
            currency = data_item.get('currency')
            # If matching_id is the same in data line and in matching line count total price of this product
            if data_item.get('matching_id') == match_item.get('matching_id'):
                data_counter += 1
                # if quantity is lower than 0 raise error
                if int(data_item.get('quantity')) < 0:
                    raise Exception("Quantity should be over 0")
                # If currency is different than PLN -> function currency_converter is converting to PLN
                if currency != 'PLN':
                    price = currency_converter(data_item)*int(data_item.get('quantity'))
                    # if actual product price is higher than highest_price, highest_price is replacing
                    if price > highest_price:
                        highest_price = price
                # Here currency is PLN
                else:
                    price = int(data_item.get('price'))*int(data_item.get('quantity'))
                    # if actual product price is higher than highest_price, highest_price is replacing
                    if price > highest_price:
                        highest_price = price
                total_price += price
        data_to_save.append({'matching_id': match_item.get('matching_id'), 'total_price': str(price),
                             'avg_price': str(int(total_price/data_counter)), 'currency': currency,
                             'ignored_products_count': str(data_counter - int(match_item.get('top_priced_count')))})
    save_to_csv(data_to_save, 'top_products.csv')
    return 0


# Function convert foreign currency to PLN using currencies table saved as csv
#
# input - data line from data csv where is foreign currency
# output - value converted to PLN
def currency_converter(data):
    currencies = read_csv_file('currencies.csv')
    if currencies == -1:
        raise Exception("Cannot read from File")
    for item in currencies:
        if data.get('currency') == 'PLN':
            return -1
        if data.get('currency') == item.get('currency'):
            if float(item.get('ratio')) == 0.0:
                raise Exception("Ratio cannot be 0")
            return int(data.get('price'))*float(item.get('ratio'))


if __name__ == "__main__":
    Valuation_service()