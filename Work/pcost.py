# pcost.py
#
# Exercise 1.27

def run():
    with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f)
        print(headers)
        cost = 0.0

        for line in f:
            row = line.split(',')
            name = str(row[0][1:-1])
            shares = int(row[1])
            price = float(row[2][:-1])
            print(name, shares, price)
            cost += shares * price

        print(f'Total cost of portfolio is {cost}')
