import unittest
import datetime
from treasury import TreasuryBill

class TreasuryTests(unittest.TestCase):

    def test_yield_to_maturity(self):
        treasuryBill = TreasuryBill('912797GF83', 99.614875)
        self.assertEqual(treasuryBill.yieldToMaturity(), 0.003866)

if __name__ == '__main__':
    unittest.main()
