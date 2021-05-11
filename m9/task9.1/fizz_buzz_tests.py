import unittest
import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

	def test_buzz(self):
		servers=21
		size=200
		result = fizz_buzz.get_info(servers,size)
		self.assertEqual(result, 'Buzz/Demo')

	def test_fizzbuzz(self):
		servers=50
		size=420
		result = fizz_buzz.get_info(servers,size)
		self.assertEqual(result, 'FizzBuzz/Vip')

	def test_fizz(self):
		servers=24
		size=423
		result = fizz_buzz.get_info(servers,size)
		self.assertEqual(result, 'Fizz/Medium')


if __name__ == '__main__':
	unittest.main()
