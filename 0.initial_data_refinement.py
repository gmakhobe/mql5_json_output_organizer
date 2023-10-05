import json
import os
import sys
import time

from utilities.refine_deals_and_orders_data import RefineDealsAndOrdersData

json_file_deals = open(os.path.join(sys.path[0], "raw_data/Gold/deals_sells_Gold.json"), "r")
json_file_orders = open(os.path.join(sys.path[0], "raw_data/Gold/orders_sells_Gold.json"), "r")
json_data_orders = json.load(json_file_orders) 
json_data_deals = json.load(json_file_deals)
refine_deals_and_orders_data = RefineDealsAndOrdersData()

defined_information = {}

for deals_key, orders_keys in zip(json_data_deals, json_data_orders):
  deals = json_data_deals[deals_key]
  orders = json_data_orders[orders_keys]

  refine_deals_and_orders_data.set_lists(deals, orders)
  refine_deals_and_orders_data.refine_dictionary()
  refined_data = refine_deals_and_orders_data.get_refined_dictionary()

  defined_information[deals_key] = refined_data["refined_data"]

with open("final_refined_data/Gold/sells_Gold.json", "w") as file:
  json.dump(defined_information, file)