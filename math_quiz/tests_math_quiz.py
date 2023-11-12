import unittest
from math_quiz import get_random_int, get_random_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if random operator is one of the specified operators
        operators = ['+', '-', '*']
        for _ in range(1000): # testign a large number of random values
            rand_operator = get_random_operator()
            self.assertIn(rand_operator, operators)
        

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (7, 2, '+', '7 + 2', 9),
                (12,10,'*', '12 * 10', 120)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
