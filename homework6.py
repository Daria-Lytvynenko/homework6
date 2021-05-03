if __name__ == '__main__':
# Task 2. Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.
    stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    total_prices = {}
    x1 = stock.get('banana')
    x2 = stock.get('apple')
    x3 = stock.get('orange')
    x4 = stock.get('pear')
    y1 = prices.get('banana')
    y2 = prices.get('apple')
    y3 = prices.get('orange')
    y4 = prices.get('pear')
total_prices = {"banana": x1 * y1, "apple": x2 * y2, "orange": x3 * y3, "pear": x4 * y4}
print(total_prices)
# Task3. List comprehension exercise.Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
print([(x, x**2) for x in range(10)])
