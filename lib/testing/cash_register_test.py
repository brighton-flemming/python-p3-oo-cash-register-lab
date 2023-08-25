
      
import unittest
from cash_register import CashRegister  

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.register = CashRegister()

    def test_add_item(self):
        self.register.add_item("Apple", 0.75, 3)
        self.assertEqual(len(self.register.items), 1)

    def test_calculate_total(self):
        self.register.add_item("Apple", 0.75, 3)
        self.register.add_item("Banana", 0.5, 5)
        self.assertEqual(self.register.calculate_total(), 4.75)

    def test_apply_discount(self):
        self.register.add_item("Apple", 0.75, 3)
        self.register.apply_discount(10)
        self.assertEqual(self.register.calculate_total(), 2.025)

    def test_void_last_transaction(self):
        self.register.add_item("Apple", 0.75, 3)
        self.register.add_item("Banana", 0.5, 5)
        self.register.void_last_transaction()
        self.assertEqual(len(self.register.items), 1)

if __name__ == '__main__':
    unittest.main()
