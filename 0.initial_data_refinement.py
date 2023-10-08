import json
import csv
import datetime

from utilities.refine_deals_and_orders_data import RefineDealsAndOrdersData

def get_duration(from_date, to_date):
    # Define two date and time objects
    start_date = datetime.datetime.strptime(from_date, "%Y-%m-%d %H:%M")  # Example start date and time
    end_date = datetime.datetime.strptime(to_date, "%Y-%m-%d %H:%M")   # Example end date and time

    # Calculate the duration
    duration = end_date - start_date

    # Extract days and seconds from the duration
    days = duration.days
    seconds = duration.seconds

    # Calculate the number of hours
    hours = seconds // 3600  # 3600 seconds in an hour

    # Format the output
    if days > 0:
        duration_str = f"{days} days"
    elif hours > 0:
        duration_str = f"{hours} hours"
    else:
        duration_str = "Less than 1 hour"

    return duration_str

json_data_deals = None
with open('raw_data/STS_GBPJPY/Buys_and_Sells_2/deals.json', 'r') as file:
    string_file_deals = file.read()
    json_file_deals = json.loads(string_file_deals)

json_data_orders = None
with open('raw_data/STS_GBPJPY/Buys_and_Sells_2/orders.json', 'r') as file:
    string_file_orders = file.read()
    json_data_orders = json.loads(string_file_orders)

monitoring_counter = 1
information = []
data_in_dictionary = None
for counter, (orders, deals) in enumerate(zip(json_data_orders["data"], json_file_deals["data"])):
    if monitoring_counter == 1:
        # Execute log
        datetime_ = orders["Time"]
        datetime_ = datetime_.replace(".", "-")
        datetime_object = datetime.datetime.strptime(datetime_, "%Y-%m-%d %H:%M") 
        data_in_dictionary = {
          "Symbol": orders["Symbol"],
          "TradeType": orders["Type"],
          "EntryPrice": deals["EntryPrice"],
          "StopLossPrice": deals["StopLossPrice"],
          "TakeProfitPrice": orders["TakeProfitPrice"],
          "DayTradeTaken": datetime_object.strftime('%A'),
          "MonthTradeTaken": datetime_object.strftime('%B'),
          "EntryDate": datetime_,
          "ExitDate": None,
          "TradeDuration": None,
          "TradeResults": None,
          "PrevMonthCandleType": orders["PrevMonthCandleType"],
          "PrevMonthDidOpenInTheBody": orders["PrevMonthDidCurrentTradeOpenInTheBody"],
          "PrevThreeMonthsClosing": orders["PrevThreeMonthsClosing"],
          "PrevWeekCandleType": orders["PrevWeekCandleType"],
          "PrevWeekDidOpenInTheBody": orders["PrevWeekDidCurrentTradeOpenInTheBody"],
          "PrevThreeWeeksClosing": orders["PrevThreeWeeksClosing"],
          "PrevDayCandleType": orders["PrevDayCandleType"],
          "PrevDayDidOpenInTheBody": orders["PrevDayDidCurrentTradeOpenInTheBody"],
          "PrevThreeDaysClosing": orders["PrevThreeDaysClosing"],
          "PrevFourHoursCandleType": orders["PrevFourHoursCandleType"],
          "PrevFourHoursDidOpenInTheBody": orders["PrevFourHoursDidCurrentTradeOpenInTheBody"],
          "PrevThreeFourHoursClosing": orders["PrevThreeFourHoursClosing"]
        }

        monitoring_counter = 2
        continue
    if monitoring_counter == 2:
        datetime_ = orders["Time"].replace(".", "-")
        trade_results = float(deals["Profit"])
        data_in_dictionary["TradeDuration"] =  get_duration(data_in_dictionary['EntryDate'], datetime_)
        data_in_dictionary["TradeResults"] = 2 if trade_results > 0 else -1
        data_in_dictionary["ExitDate"] = datetime_
    information.append(data_in_dictionary)
    data_in_dictionary = None 
    monitoring_counter = 1

defined_information = {
    "data": information
}

csv_file_path = 'STS_output_v_2.csv'
fieldnames = [
          "Symbol",
          "TradeType",
          "EntryPrice",
          "StopLossPrice",
          "TakeProfitPrice",
          "DayTradeTaken",
          "MonthTradeTaken",
          "EntryDate",
          "ExitDate",
          "TradeDuration",
          "TradeResults",
          "PrevMonthCandleType",
          "PrevMonthDidOpenInTheBody",
          "PrevThreeMonthsClosing",
          "PrevWeekCandleType",
          "PrevWeekDidOpenInTheBody",
          "PrevThreeWeeksClosing",
          "PrevDayCandleType",
          "PrevDayDidOpenInTheBody",
          "PrevThreeDaysClosing",
          "PrevFourHoursCandleType",
          "PrevFourHoursDidOpenInTheBody",
          "PrevThreeFourHoursClosing"
        ]
# Open the CSV file and write data
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in information:
        writer.writerow(row)