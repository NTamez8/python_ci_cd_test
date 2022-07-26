import unittest
from python_ci_cd import add_two_nums


class testPythonCICD(unittest.TestCase):
    def test_add_two_nums(self):
        first_num = 1
        second_num = 2
        result = add_two_nums(first_num, second_num)
        self.assertEqual(result,first_num + second_num)

if __name__ == '__main__':
    unittest.main()