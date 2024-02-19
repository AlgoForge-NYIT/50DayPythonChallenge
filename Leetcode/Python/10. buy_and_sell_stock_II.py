def max_profit(prices):

    max_continuous_profit = 0
   
   
    for i in range(0, len(prices) - 1): # [7,1,5,3,6,4]
       
        curr_price = prices[i]
        next_price = prices[i+1]
        next_day_profit = next_price - curr_price
        if next_day_profit >= 0:
            max_continuous_profit += next_day_profit
       
    return max_continuous_profit