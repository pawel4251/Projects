import unittest
from Valuationservice import read_csv_file, save_to_csv, Valuation_service, currency_converter

file1 = 'currencies.csv'
file2 = 'data.csv'
file3 = 'matchings.csv'
data1 = [{'matching_id': '1', 'total_price': '10080.0', 'avg_price': '4761', 'currency': 'GBP',
          'ignored_products_count': '1'}, {'matching_id': '2', 'total_price': '21000', 'avg_price': '14175',
                                           'currency': 'GBP', 'ignored_products_count': '0'},
         {'matching_id': '3', 'total_price': '8400.0', 'avg_price': '8130', 'currency': 'GBP',
          'ignored_products_count': '1'}]
data2 = {'id': '2', 'price': '1050', 'currency': 'EU', 'quantity': '1', 'matching_id': '1'}
data3 = {'id': '2', 'price': '1050', 'currency': 'PLN', 'quantity': '1', 'matching_id': '1'}

class Valuation_service_test(unittest.TestCase):

    def setUp(self):
        self.Valuation_service = Valuation_service()

    def test_wrong_read_csv_file(self):
        result = read_csv_file('')
        self.assertEqual(-1, result)

    def test_positive_read_csv_file(self):
        result = read_csv_file(file2)
        self.assertIsInstance(result, list)

    def test_wrong_save_csv_file(self):
        result = save_to_csv(data1, '')
        self.assertEqual(-1, result)

    def test_positive_save_csv_file(self):
        result = save_to_csv(data1, 'top_priced_count.csv')
        self.assertEqual(0, result)

    def tests_positive_currency_converter(self):
        result = currency_converter(data2)
        self.assertEqual(2205.0, result)

    def tests_wrong_currency_converter(self):
        result = currency_converter(data3)
        self.assertEqual(-1, result)

    def tests_valuationservice(self):
        result = Valuation_service()
        self.assertEqual(0, result)

if __name__ == "__main__":
    tests = Valuation_service_test()
    tests.test_wrong_read_csv_file()
    tests.test_positive_read_csv_file()
    tests.test_wrong_save_csv_file()
    tests.test_positive_save_csv_file()
    tests.tests_positive_currency_converter()
    tests.tests_wrong_currency_converter()
    tests.tests_valuationservice()