import unittest
from HW1task2_var1 import sumbilet

class MyTestCasesForHappybilet(unittest.TestCase):
    def test_sumbilet(self):
        self.assertEqual(sumbilet(999933),42)

    def test_sumbilet2(self):
        self.assertNotEqual(sumbilet(999949),42)





if __name__ == '__main__':
    unittest.main()