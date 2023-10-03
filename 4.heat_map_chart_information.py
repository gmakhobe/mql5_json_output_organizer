import json
import os
import sys

json_file_final_refined_data_buy_and_sell = open(os.path.join(sys.path[0], "information/GBPJPY-10-STOPLOSS/3.pie_chart_buys_and_sells_gbpjpy.json"), "r")
json_file_final_refined_data_sell = open(os.path.join(sys.path[0], "information/GBPJPY-10-STOPLOSS/3.pie_chart_buys_gbpjpy.json"), "r")
json_file_final_refined_data_buy = open(os.path.join(sys.path[0], "information/GBPJPY-10-STOPLOSS/3.pie_chart_sells_gbpjpy.json"), "r")
dict_buy_sell = json.load(json_file_final_refined_data_buy_and_sell)
dict_sell = json.load(json_file_final_refined_data_sell)
dict_buy = json.load(json_file_final_refined_data_buy)

dictionary = {
    "buy_and_sell": {
        "net_winnings": dict_buy_sell["net_winnings"],
        "net_rewards": dict_buy_sell["net_rewards"],
    },
    "sell": {
        "net_winnings": dict_sell["net_winnings"],
        "net_rewards": dict_sell["net_rewards"]
    },
    "buy": {
        "net_winnings": dict_buy["net_winnings"],
        "net_rewards": dict_buy["net_rewards"]
    }
}

with open("information/GBPJPY-10-STOPLOSS/4.heat_map_gbpjpy.json", "w") as file:
    json.dump(dictionary, file)
