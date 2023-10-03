import json
import os
import sys

from utilities.time_duration import get_duration_in_hours
from utilities.profit_and_stop_calculations import get_take_profit_in_pips, get_stop_loss_pips

json_file_final_refined_data = open(os.path.join(sys.path[0], "final_refined_data/GBPJPY/10_sells_gbpjpy.json"), "r")
json_refinened_data = json.load(json_file_final_refined_data)
SYMBOL = "GBPJPY"

trades_list = []

for month in json_refinened_data:
    for trade in json_refinened_data[month]:
        profit = float(trade["Profit"])
        entry_time = trade["EntryTime"].replace(".", "-")
        exit_time = trade["ExitTime"].replace(".", "-")
        duration = get_duration_in_hours(entry_time, exit_time)
        trade_type = trade["Type"]
        entry_price = float(trade["EntryPrice"])
        stop_loss_price = float(trade["StopLossPrice"])
        take_profit_price = float(trade["TakeProfitPrice"])
        stop_loss_price = get_stop_loss_pips(SYMBOL, trade_type, entry_price, stop_loss_price)
        take_profit_price = get_take_profit_in_pips(SYMBOL, trade_type, entry_price, take_profit_price)

        if profit > 0:

          trades_list.append({
            "Profit": 2,
            "Type": "Win",
            "TradeType": trade_type,
            "EntryPrice": entry_price,
            "StopLossPrice": stop_loss_price,
            "TakeProfitPrice": take_profit_price,
            "Month": month,
            "Duration": duration,
            "EntryTime": entry_time,
            "ExitTime": exit_time
          })
        else:
          trades_list.append({
            "Profit": -1,
            "Type": "Loss",
            "TradeType": trade_type,
            "EntryPrice": entry_price,
            "StopLossPrice": stop_loss_price,
            "TakeProfitPrice": take_profit_price,
            "Month": month,
            "Duration": duration,
            "EntryTime": entry_time,
            "ExitTime": exit_time
          })

information = {
    "trades": trades_list
}

print(information)

with open("information/GBPJPY-10-STOPLOSS/5.scatter_plot_sells_gbpjpy.json", "w") as file:
  json.dump(information, file)