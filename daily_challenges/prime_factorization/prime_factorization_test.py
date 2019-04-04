import unittest
from prime_factorization import prime_factor

class TestPrimeFactorization(unittest.TestCase):
	def test_all_prime_numbers(self):
		prime_numbers = [
							2, 3, 5, 7, 11, 13, 
							17, 19, 23, 29, 31, 
							37, 41, 43, 47, 53, 
							59, 61, 67, 71, 73, 
							79, 83, 89, 97, 101, 
							103, 107, 109, 113, 
							127, 131, 137, 139, 
							149, 151, 157, 163, 
							167, 173, 179, 181, 
							191, 193, 197, 199
						]
		for expected_value in prime_numbers:
			actual_value = prime_factor(expected_value)
			self.assertEqual(expected_value, int(actual_value[0]))
			print(f'{expected_value} - {int(actual_value[0])}')

if __name__ == '__main__':
	unittest.main()


