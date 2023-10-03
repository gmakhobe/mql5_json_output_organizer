import json
import os
import sys

from utilities.trade_percentage_and_raw_wins_and_loss import TradePercentageAndRawWinsAndLoss

json_file_final_refined_data = open(os.path.join(sys.path[0], "final_refined_data/GBPJPY/10_sells_gbpjpy.json"), "r")
json_refined_data = json.load(json_file_final_refined_data)

obj = TradePercentageAndRawWinsAndLoss()
obj.set_dictionary(json_refined_data)
dictionary = obj.get_trade_percentage_and_raw_winsloss()

with open("information/GBPJPY-10-STOPLOSS/3.pie_chart_sells_gbpjpy.json", "w") as file:
    json.dump(dictionary, file)
