def max_profit(prices):
    result = 0
    min_seen = prices[0]
   
    for i in range(1, len(prices)): # [7,1,5,3,6,4]
       
        curr_price = prices[i]
   
        curr_profit = curr_price - min_seen
       
        if curr_profit > result:
            result = curr_profit
       
        if curr_price < min_seen :
            min_seen = prices[i]
           
    return result