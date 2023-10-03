class TradePercentageAndRawWinsAndLoss:
    def __init__(self):
        self.winning_trades = 0
        self.losing_trades = 0
        self.winning_trades_percentage = 0
        self.losing_trades_percentage = 0
        self.reward = 0
        self.loss = 0
        self.reward_percentage = 0
        self.loss_percentage = 0
        self.net_winnings = 0
        self.net_rewards = 0

    def set_dictionary(self, data):
        """Set the dictionary data to the class variable data"""
        self.data = data
        print("Data is set")
        print("You can call the get_profit method to get the profit dictionary")

    def process_data(self):
        """Process data to get the winning and losing trades"""
        for month in self.data:
            for trade in self.data[month]:
                profit = float(trade["Profit"])
                if profit > 0:
                    self.winning_trades += 1
                    self.reward += 2
                else:
                    self.losing_trades += 1
                    self.loss += 1
        self.net_winnings = self.winning_trades - self.losing_trades
        self.net_rewards = self.reward - self.loss
        self.winning_trades_percentage = (self.winning_trades / (self.winning_trades + self.losing_trades)) * 100
        self.losing_trades_percentage = (self.losing_trades / (self.winning_trades + self.losing_trades)) * 100
        self.reward_percentage = (self.reward / (self.reward + self.loss)) * 100
        self.loss_percentage = (self.loss / (self.reward + self.loss)) * 100


    def get_trade_percentage_and_raw_winsloss(self):
        """Return information about trade percentage and raw wins and losses"""
        self.process_data()
        print("Data successfully processed and output is given below")
        return {
            "winning_trades": self.winning_trades,
            "losing_trades": self.losing_trades,
            "winning_trades_percentage": self.winning_trades_percentage,
            "losing_trades_percentage": self.losing_trades_percentage,
            "reward": self.reward,
            "loss": self.loss,
            "reward_percentage": self.reward_percentage,
            "loss_percentage": self.loss_percentage,
            "net_winnings": self.net_winnings,
            "net_rewards": self.net_rewards
        }
