from typing import List

prices = [20, 40, 10, 5, 60, 70, 20, 80, 5, 10]

def best_time(prices):
    best_buy = prices[0]
    best_buy_day = 0
    profit = 0
    best_profit_day = 0

    for i in range (1, len(prices)):
        if prices[i] < best_buy:
            best_buy = prices[i]
            best_buy_day = i
        else:
            current_profit = prices[i] - best_buy
            if current_profit > profit:
                profit = current_profit
                best_profit_day = i

    return best_buy, best_buy_day, profit, best_profit_day

print(best_time(prices))