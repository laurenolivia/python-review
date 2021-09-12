import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,10), 0)
        self.assertEqual(calc.subtract(-10,-10), 0)
        self.assertEqual(calc.subtract(-10,5), -15)
        self.assertEqual(calc.subtract(10,-3), 13)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(2,2), 4)
        self.assertEqual(calc.multiply(-3,-3), 9)
        self.assertEqual(calc.multiply(-4,4), -16)
        self.assertEqual(calc.multiply(5,-6), -30)
        self.assertEqual(calc.multiply(5,0), 0)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)

        with self.assertRaises(ValueError):
            calc.divide(10,0)





if __name__ == '__main__':
    unittest.main()