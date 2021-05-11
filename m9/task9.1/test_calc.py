import calculatorr
import unittest

#print(calculatorr.res.add(10,2))


class TestStringMethods(unittest.TestCase):

##### NEGATIVE TESTS
  def test_add_floats(self):
      self.assertEqual(calculatorr.res.add(3.4,3.7),7.1)
  def test_enormous_values(self):
      self.assertEqual(calculatorr.res.multiply(12345678912345,2),24691357824690)
  def test_divide(self):
      res=calculatorr.res.divide('25',5)
      self.assertEqual(res,"ERROR")
  def test_negative_subtract(self):
      self.assertEqual(calculatorr.res.subtract(-4,-10),6)
##### POSITIVE TESTS
  def test_simple_multiply(self):
      self.assertEqual(calculatorr.res.multiply(3,4),12)
  def test_simple_subtract(self):
      self.assertEqual(calculatorr.res.subtract(3,4),-1)
  def test_int_divide(self):
      self.assertEqual(calculatorr.res.divide(12,4),3)
  def test_simple_add(self):
      self.assertEqual(calculatorr.res.add(1,2),3)
if __name__ == '__main__':
    unittest.main()
