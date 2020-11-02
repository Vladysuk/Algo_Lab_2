def algorithm(prices, discount, N):
    """
    >>> prices = [50, 20, 30, 17, 100]
    >>> discount = 10
    >>> N = 3
    >>> algorithm(prices, discount, N)
    207.0
    >>> prices = [1, 2, 3, 4, 5, 6, 7]
    >>> discount = 100
    >>> N = 3
    >>> algorithm(prices, discount, N)
    15.0
    >>> prices = [1, 1, 1]
    >>> discount = 33
    >>> N = 3
    >>> algorithm(prices, discount, N)
    2.67
    """
    position = len(prices) // N
    discounted_prices = prices[-position:]
    default_prices = prices[:-position]
    total_price = 0
    for el in discounted_prices:
        total_price += el * (1 - (discount / 100))
    for el in default_prices:
        total_price += el
    return total_price


def main():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
