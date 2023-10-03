import json
import os
import sys

from utilities.time_duration import get_duration_in_hours
from utilities.profit_and_stop_calculations import get_take_profit_in_pips, get_stop_loss_pips

json_file_final_refined_data = open(os.path.join(sys.path[0], "final_refined_data/GBPJPY/sells_gbpjpy.json"), "r")
json_refinened_data = json.load(json_file_final_refined_data)
SYMBOL = "GBPJPY"

month_trades_list = []
year_trades_list = {}

for month in json_refinened_data:
    for trade in json_refinened_data[month]:

        trade_type = trade["Type"]
        entry_price = float(trade["EntryPrice"])
        stop_loss_price = float(trade["StopLossPrice"])
        take_profit_price = float(trade["TakeProfitPrice"])
        stop_loss_price = get_stop_loss_pips(SYMBOL, trade_type, entry_price, stop_loss_price)
        take_profit_price = get_take_profit_in_pips(SYMBOL, trade_type, entry_price, take_profit_price)

        if stop_loss_price >= 10 and take_profit_price >= 18:
            month_trades_list.append(trade)

    year_trades_list[month] = month_trades_list
    month_trades_list = []


print(year_trades_list)

with open("final_refined_data/GBPJPY/10_sells_gbpjpy.json", "w") as file:
  json.dump(year_trades_list, file)