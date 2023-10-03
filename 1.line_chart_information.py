import json
import os
import sys

from utilities.profit_information import ProfitInformation

json_file_final_refined_data = open(os.path.join(sys.path[0], "final_refined_data/GBPJPY/10_buys_and_sells_gbpjpy.json"), "r")
json_refiened_data = json.load(json_file_final_refined_data) 

profit_information = ProfitInformation()
profit_information.set_dictioanry(json_refiened_data)
line_chart_profit_information = profit_information.get_profit(1)

with open("information/GBPJPY-10-STOPLOSS/1.line_buys_and_sells_gbpjpy.json", "w") as file:
  json.dump(line_chart_profit_information, file)