import unittest

from HW2_Recurcion import rec



class MyTestCasesForRecursion(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(rec(3, 3), 1)

    def test_rec_2(self):
        self.assertEqual(rec(5, 1), 5)

    def test_rec_3(self):
        self.assertEqual(rec(5, 4), 5)




if __name__ == '__main__':
    unittest.main()
