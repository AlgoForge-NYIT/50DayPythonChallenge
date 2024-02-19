public class StocksBuySell {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buyValue = prices[0]; // first buy in

        for(int i = 0;i < prices.length; i++){
            // if next buy is less than the previous buy:
            if(prices[i] < buyValue){
                buyValue = prices[i];
            }
            // if sell it for today has greater profit:
            if(prices[i] - buyValue > profit){
                profit = prices[i] - buyValue;
            }
        }

        return profit;
    }
}
