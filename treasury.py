class TreasuryBill:
  def __init__(self, cusip, price):
    self.faceValue = 100
    self.cusip = cusip
    self.price = price

  def yieldToMaturity(self):
    return round(((self.faceValue/self.price) - 1),6)