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

def test_weird():
    tc = unittest.TestCase()
    tc.assertEqual(wierd(10), 'Weird')

def main():
    print ('test')
    wierd(10)
    test_weird()

    
if __name__ == "__main__":
    main()
