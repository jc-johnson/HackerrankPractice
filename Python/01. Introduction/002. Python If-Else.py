# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10


def wierd(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')


def main():
    print ('test')
    wierd(10)
    
if __name__ == "__main__":
    main()
