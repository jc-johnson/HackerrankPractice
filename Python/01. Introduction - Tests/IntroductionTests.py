# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10

import unittest

def wierd(n):
        if n % 2 == 1 or 6 <= n <= 20:
            print('Weird')
            return('Weird')
        else:
            print('Not Weird')
            return('Not Weird')
        
class TestIfElse(unittest.TestCase):  
                
    def test_Weird(self):
        self.assertEqual(wierd(20), 'Weird')
   
if __name__ == "__main__":
    unittest.main()
