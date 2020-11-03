from algorithm import algorithm
from quick_sort import quick_sort

if __name__ == '__main__':
    N = 3
    with open("discnt.in", "r+") as fileIn:
        prices = [int(x) for x in next(fileIn).split()]
        discount = int(fileIn.readline())

    quick_sort(prices, 0, len(prices)-1)
    total_price = algorithm(prices, discount, N)

    with open('discnt.out', 'w') as fileOut:
        fileOut.write('Total price with discount: %f' % total_price)