class ProfitInformation:
    """This class will calculate the profit information from the final refined data"""

    def __init__(self):
        # To-Do
        self.data = None
        self.monthly_profit = {}

    def set_dictioanry(self, data):
        """Set the dictionary data to the class variable data"""
        self.data = data
        print("Data is set")
        print("You can call the get_profit method to get the profit dictionary")

    def get_profit(self, term_divider=1):
        """Return the profit dictionary"""
        if term_divider not in (1, 3, 6):
            raise ValueError("Term divider must be 1, 3 or 6, ", term_divider, " was given")

        if self.data == None:
            raise ValueError("Data is not set")

        self.process_profit(term_divider)

        if term_divider == 1:
            return self.monthly_profit

        if term_divider == 3:
            return self.quarterly_profit

        if term_divider == 6:
            return self.semesterly_profit

        return None

    def process_profit(self, term_divider):
        """Process  profit to a dictionary that will include gross profit & loss, net profit & loss in pips and dollars to a dictionary using the following deviders 1=each month, 3=each quarter and 6=each half year"""
        if term_divider not in (1, 3, 6):
            raise ValueError("Term divider must be 1, 3 or 6, ", term_divider, " was given")

        if self.data == None:
            raise ValueError("Data is not set")

        january = self.calculate_profit(self.data["January"], "31 January 2022")
        february = self.calculate_profit(self.data["February"], "28 February 2022")
        march = self.calculate_profit(self.data["March"], "31 March 2022")
        april = self.calculate_profit(self.data["April"], "30 April 2022")
        may = self.calculate_profit(self.data["May"], "31 May 2022")
        june = self.calculate_profit(self.data["June"], "30 June 2022")
        july = self.calculate_profit(self.data["July"], "31 July 2022")
        august = self.calculate_profit(self.data["August"], "31 August 2022")
        september = self.calculate_profit(self.data["September"], "30 September 2022")
        october = self.calculate_profit(self.data["October"], "31 October 2022")
        november = self.calculate_profit(self.data["November"], "30 November 2022")
        december = self.calculate_profit(self.data["December"], "31 December 2022")

        if term_divider == 1:
            self.monthly_profit["PROFIT_"] = [
                january,
                february,
                march,
                april,
                may,
                june,
                july,
                august,
                september,
                october,
                november,
                december
            ]

        if term_divider == 3:
            self.quarterly_profit = {
                "Q1": {
                    "gross_profit": january["gross_profit"] + february["gross_profit"] + march["gross_profit"],
                    "gross_loss": january["gross_loss"] + february["gross_loss"] + march["gross_loss"],
                    "gross_reward": january["gross_reward"] + february["gross_reward"] + march["gross_reward"],
                    "gross_risk": january["gross_risk"] + february["gross_risk"] + march["gross_risk"],
                    "net_profit": january["net_profit"] + february["net_profit"] + march["net_profit"],
                    "net_reward": january["net_reward"] + february["net_reward"] + march["net_reward"]
                },
                "Q2": {
                    "gross_profit": april["gross_profit"] + may["gross_profit"] + june["gross_profit"],
                    "gross_loss": april["gross_loss"] + may["gross_loss"] + june["gross_loss"],
                    "gross_reward": april["gross_reward"] + may["gross_reward"] + june["gross_reward"],
                    "gross_risk": april["gross_risk"] + may["gross_risk"] + june["gross_risk"],
                    "net_profit": april["net_profit"] + may["net_profit"] + june["net_profit"],
                    "net_reward": april["net_reward"] + may["net_reward"] + june["net_reward"]
                },
                "Q3": {
                    "gross_profit": july["gross_profit"] + august["gross_profit"] + september["gross_profit"],
                    "gross_loss": july["gross_loss"] + august["gross_loss"] + september["gross_loss"],
                    "gross_reward": july["gross_reward"] + august["gross_reward"] + september["gross_reward"],
                    "gross_risk": july["gross_risk"] + august["gross_risk"] + september["gross_risk"],
                    "net_profit": july["net_profit"] + august["net_profit"] + september["net_profit"],
                    "net_reward": july["net_reward"] + august["net_reward"] + september["net_reward"]
                },
                "Q4": {
                    "gross_profit": october["gross_profit"] + november["gross_profit"] + december["gross_profit"],
                    "gross_loss": october["gross_loss"] + november["gross_loss"] + december["gross_loss"],
                    "gross_reward": october["gross_reward"] + november["gross_reward"] + december["gross_reward"],
                    "gross_risk": october["gross_risk"] + november["gross_risk"] + december["gross_risk"],
                    "net_profit": october["net_profit"] + november["net_profit"] + december["net_profit"],
                    "net_reward": october["net_reward"] + november["net_reward"] + december["net_reward"]
                },
            }

        if term_divider == 6:
            self.semesterly_profit = {
                "first_simester": {
                    "gross_profit": january["gross_profit"] + february["gross_profit"] + march["gross_profit"] + april[
                        "gross_profit"] + may["gross_profit"] + june["gross_profit"],
                    "gross_loss": january["gross_loss"] + february["gross_loss"] + march["gross_loss"] + april[
                        "gross_loss"] + may["gross_loss"] + june["gross_loss"],
                    "gross_reward": january["gross_reward"] + february["gross_reward"] + march["gross_reward"] + april[
                        "gross_reward"] + may["gross_reward"] + june["gross_reward"],
                    "gross_risk": january["gross_risk"] + february["gross_risk"] + march["gross_risk"] + april[
                        "gross_risk"] + may["gross_risk"] + june["gross_risk"],
                    "net_profit": january["net_profit"] + february["net_profit"] + march["net_profit"] + april[
                        "net_profit"] + may["net_profit"] + june["net_profit"],
                    "net_reward": january["net_reward"] + february["net_reward"] + march["net_reward"] + april[
                        "net_reward"] + may["net_reward"] + june["net_reward"]
                },
                "second_simester": {
                    "gross_profit": july["gross_profit"] + august["gross_profit"] + september["gross_profit"] + october[
                        "gross_profit"] + november["gross_profit"] + december["gross_profit"],
                    "gross_loss": july["gross_loss"] + august["gross_loss"] + september["gross_loss"] + october[
                        "gross_loss"] + november["gross_loss"] + december["gross_loss"],
                    "gross_reward": july["gross_reward"] + august["gross_reward"] + september["gross_reward"] + october[
                        "gross_reward"] + november["gross_reward"] + december["gross_reward"],
                    "gross_risk": july["gross_risk"] + august["gross_risk"] + september["gross_risk"] + october[
                        "gross_risk"] + november["gross_risk"] + december["gross_risk"],
                    "net_profit": july["net_profit"] + august["net_profit"] + september["net_profit"] + october[
                        "net_profit"] + november["net_profit"] + december["net_profit"],
                    "net_reward": july["net_reward"] + august["net_reward"] + september["net_reward"] + october[
                        "net_reward"] + november["net_reward"] + december["net_reward"]
                }
            }

    def calculate_profit(self, data_list, date):
        """Return gross profit & loss, net profit & loss in pips and dollars"""
        gross_profit = 0
        gross_loss = 0
        gross_reward = 0
        gross_risk = 0
        for element in data_list:
            profit = float(element["Profit"])

            if profit > 0:
                gross_profit += profit
                gross_reward += 2
            else:
                gross_loss += profit
                gross_risk += 1

        return {
            "gross_profit": gross_profit,
            "gross_loss": gross_loss,
            "gross_reward": gross_reward,
            "gross_risk": gross_risk,
            "net_profit": gross_profit + gross_loss,
            "net_reward": gross_reward - gross_risk,
            "date": date

        }
