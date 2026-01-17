def maxProfit(prices):
    if len(prices) == 0 or len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(maxProfit([1, 4, 7, 5, 12]))  #Output: 11
print(maxProfit([45, 31, 64, 12, 21, 67]))  #Output: 55