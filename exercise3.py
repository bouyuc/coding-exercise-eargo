def partA(stock_price):
    """A function to find out the best Buying and Selling day 
    for maximum gain from daily stock prices of the last 10 days.

    With the following constraits:
        1. Buy first
        2. You can only buy once and sell once

    Parameters
    ----------
    stock_price: list of int, required
    10 day stock prices

    Returns
    ----------
    list: Best buying and selling day on index 0 and index 1 respectively
    """
    max = 0
    min = stock_price[0]
    maxDay = 0
    minDay = 0
    for day, price in enumerate(stock_price):
        if(price < min):
            min = price
            minDay = day
        else:
            if(price - min > max):
                max = price-min
                maxDay = day
    return [minDay, maxDay]

def partB(stock_price):
    """A function to find out the best Buying and Selling day 
    for maximum gain from daily stock prices of the last 10 days.
    Returns a list of Buying and Selling days
    With the following constraits:
        1. You buy first and then sell
        2. Buy and sell as many times as possible. Goal is to maximize profit.

    Parameters
    ----------
    stock_price: list of int, required
    10 day stock prices
    
    Returns
    ----------
    list: List of Best buying and selling days
    """
    gains = 0
    buySellDays = []
    for i in range(1, len(stock_price)):
        if(stock_price[i] > stock_price[i-1]):
            buySellDays.append([i-1, i])
    mergedList = []
    for datePair in buySellDays:
        if(len(mergedList)> 0 and mergedList[-1][1] == datePair[0]):
            mergedList[-1][1] = datePair[1]
        else:
            mergedList.append(datePair)
    return mergedList

# Test cases
stockPriceTests = [[3, 8, 8, 55, 38, 1, 7, 42, 54, 53]]
stockPriceTests.append([0, 100, 0, 0, 0, 0, 0, 0, 0, 0])
stockPriceTests.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
stockPriceTests.append([100, 50, 40, 30, 20, 10, 0, 0, 0, 0])
stockPriceTests.append([0, 5, 30, 100, 0, 0, 0, 0, 0, 0])
stockPriceTests.append([0, 100, 0, 0, 0, 0, 0, 0, 0, 0])
stockPriceTests.append([55, 0, 3, 5, 56, 12, 51, 54, 32, 22])

print('Running exercise 3 part A')
for case in stockPriceTests:
    print("Running Test Case:", case)
    print("Best day to buy and sell stocks are:", partA(case))
    print("")

print('-------------------------------------------')
print('Running exercise 3 part B')
for case in stockPriceTests:
    print("Running Test Case:", case)
    print("Best days to buy and sell stocks are:", partB(case))
    print("")