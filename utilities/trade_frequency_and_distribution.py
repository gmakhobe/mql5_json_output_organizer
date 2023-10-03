import datetime

class TradeFrequencyAndDistribution:
    """Class to calculate the frequency and distribution of trades."""

    def __init__(self):
        self.data = None
        self.week_day_trades = None
        self.winning_and_losing_trades = {}
        self.total_trades = 0
        self.average_trades = 0

    def set_dictioanry(self, data):
        """Set the dictionary data to the class variable data"""
        self.data = data
        print("Data is set")
        print("You can call the get_profit method to get the profit dictionary")

    def set_total_trades(self):
        """Return the total number of trades"""

        if self.data == None:
            raise ValueError("Data is not set")

        trade_counter = 0

        for month in self.data:
            for trade in self.data[month]:
                trade_counter += 1

        self.total_trades = trade_counter
        print("Calculated total trades: ", self.total_trades)

    def set_average_trades(self, term_divider=1):
        """Return the average number of trades"""

        if self.data == None:
            raise ValueError("Data is not set")
        if self.total_trades == 0:
            raise ValueError("Total trades is not set")

        average_trades = self.total_trades / term_divider

        self.average_trades = average_trades
        print("Calculated average trades: ", self.average_trades)

    def set_week_day_trades(self):
        """Set the number of trades per week day"""
        if self.data == None:
            raise ValueError("Data is not set")
        if self.total_trades == 0:
            raise ValueError("Total trades is not set")

        monday_total_trades = 0
        monday_winning_trades = 0
        monday_losing_trades = 0
        tuesday_total_trades = 0
        tuesday_winning_trades = 0
        tuesday_losing_trades = 0
        wednesday_total_trades = 0
        wednesday_winning_trades = 0
        wednesday_losing_trades = 0
        thursday_total_trades = 0
        thursday_winning_trades = 0
        thursday_losing_trades = 0
        friday_total_trades = 0
        friday_winning_trades = 0
        friday_losing_trades = 0

        for month in self.data:
            for trade in self.data[month]:
                week_day_raw = trade["EntryTime"]
                week_day = datetime.datetime.strptime(week_day_raw, "%Y.%m.%d %H:%M:%S").strftime("%A")
                profit = float(trade["Profit"])

                if week_day == "Monday":
                    monday_total_trades += 1

                    if profit > 0:
                        monday_winning_trades += 1
                    else:
                        monday_losing_trades += 1

                if week_day == "Tuesday":
                    tuesday_total_trades += 1

                    if profit > 0:
                        tuesday_winning_trades += 1
                    else:
                        tuesday_losing_trades += 1

                if week_day == "Wednesday":
                    wednesday_total_trades += 1

                    if profit > 0:
                        wednesday_winning_trades += 1
                    else:
                        wednesday_losing_trades += 1

                if week_day == "Thursday":
                    thursday_total_trades += 1

                    if profit > 0:
                        thursday_winning_trades += 1
                    else:
                        thursday_losing_trades += 1

                if week_day == "Friday":
                    friday_total_trades += 1

                    if profit > 0:
                        friday_winning_trades += 1
                    else:
                        friday_losing_trades += 1

        monday = {
            "total_trades": monday_total_trades,
            "total_winning_trades": monday_winning_trades,
            "total_losing_trades": monday_losing_trades
        }
        tuesday = {
            "total_trades": tuesday_total_trades,
            "total_winning_trades": tuesday_winning_trades,
            "total_losing_trades": tuesday_losing_trades
        }
        wednesday = {
            "total_trades": wednesday_total_trades,
            "total_winning_trades": wednesday_winning_trades,
            "total_losing_trades": wednesday_losing_trades
        }
        thursday = {
            "total_trades": thursday_total_trades,
            "total_winning_trades": thursday_winning_trades,
            "total_losing_trades": thursday_losing_trades
        }
        friday = {
            "total_trades": friday_total_trades,
            "total_winning_trades": friday_winning_trades,
            "total_losing_trades": friday_losing_trades
        }

        self.week_day_trades = {
            "Monday": monday,
            "Tuesday": tuesday,
            "Wednesday": wednesday,
            "Thursday": thursday,
            "Friday": friday
        }

        print("Calculated week day trades.")

    def set_winning_and_losing_trades(self):
            """Set the number of winning and losing trades"""
            day_monday = "Monday"
            percentage_monday = (self.week_day_trades["Monday"]["total_winning_trades"] * 2) - self.week_day_trades["Monday"]["total_losing_trades"]

            highest_winning_day = {
                "day": None,
                "net_percent": 0
            }
            lowest_winning_day = {
                "day": day_monday,
                "net_percent": percentage_monday
            }
            highest_losing_day = {
                "day": None,
                "net_percent": 0
            }
            lowest_losing_day = {
                "day": None,
                "net_percent": 0
            }

            for day in self.week_day_trades:
                total_winning_trades = self.week_day_trades[day]["total_winning_trades"] * 2
                total_losing_trades = self.week_day_trades[day]["total_losing_trades"]
                net_profit_in_percentages = total_winning_trades - total_losing_trades

                if net_profit_in_percentages > 0:

                    if highest_winning_day["net_percent"] < net_profit_in_percentages:

                        highest_winning_day["day"] = day
                        highest_winning_day["net_percent"] = net_profit_in_percentages

                    if lowest_winning_day["net_percent"] > net_profit_in_percentages:

                        lowest_winning_day["day"] = day
                        lowest_winning_day["net_percent"] = net_profit_in_percentages

                if net_profit_in_percentages < 0:

                    if highest_losing_day["net_percent"] < net_profit_in_percentages:
                        highest_losing_day["day"] = day
                        highest_losing_day["net_percent"] = net_profit_in_percentages

                    if lowest_losing_day["net_percent"] > net_profit_in_percentages:
                        lowest_losing_day["day"] = day
                        lowest_losing_day["net_percent"] = net_profit_in_percentages

            self.winning_and_losing_trades["highest_winning_day"] = highest_winning_day
            self.winning_and_losing_trades["lowest_winning_day"] = lowest_winning_day
            self.winning_and_losing_trades["highest_losing_day"] = highest_losing_day
            self.winning_and_losing_trades["lowest_losing_day"] = lowest_losing_day

            print("Calculated winning and losing trades.")


