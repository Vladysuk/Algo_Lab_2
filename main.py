from algorithm import algorithm

if __name__ == '__main__':
    N = 3
    with open("discnt.in", "r+") as fileIn:
        prices = [int(x) for x in next(fileIn).split()]
        discount = int(fileIn.readline())

    prices.sort()
    total_price = algorithm(prices, discount, N)

    with open('discnt.out', 'w') as fileOut:
        fileOut.write('Total price with discount: %f' % total_price)