class RefineDealsAndOrdersData:
  def __init__(self):
    self.status = "Lists not set"
    self.refined_data = None

  def set_lists(self, deals, orders):
    """Get deals & orders as lists and initialize and assign them to the class as attributes"""
    deals_length = len(deals)
    orders_length = len(orders)
    
    if deals_length != orders_length:
        raise ValueError("Deals and orders must be same length")
    
    self.deals_length = deals_length
    self.orders_length = orders_length
    self.deals = deals
    self.orders = orders
    self.status = "Lists set but not yet refined"
    print("Deals and orders set")
  
  def get_refined_dictionary(self):
    """Returns refined dictionary, will not return any data if the lists are not set by the set_lists method"""
    if self.deals_length == 0 or self.orders_length == 0 or self.deals_length == None or self.orders_length == None or self.deals_length != self.orders_length or self.refined_data == None:
        return {
           "refined_data": None,
           "orders": None,
           "status": self.status
        }
    print("Returning refined dictionary")
    return {
        "refined_data": self.refined_data,
        "status": self.status
    }
  
  def refine_dictionary(self):
    """Refines the list from the following disctionary structures:
      [
        {
          "Order": "2",
          "Symbol": "EURUSD",
          "Type": "Buy",
          "Volume": "1.01",
          "EntryPrice": "1.13562",
          "StopLossPrice": "1.1332",
          "TakeProfitPrice": "0.0",
          "Profit": "0.0",
          "Comment": ""
        },
        {
          "Order": "3",
          "Symbol": "EURUSD",
          "Type": "Sell",
          "Volume": "1.01",
          "EntryPrice": "1.1332",
          "StopLossPrice": "1.1332",
          "TakeProfitPrice": "-244.42000000000002",
          "Profit": "-244.42000000000002",
          "Comment": "sl 1.13320"
        }
      ]
      to the following dictionary structure:
      [
        {
          "Order": "2",
          "Symbol": "EURUSD",
          "Type": "Buy",
          "Volume": "1.01",
          "EntryPrice": "1.13562",
          "StopLossPrice": "1.1332",
          "TakeProfitPrice": "1.14043",
          "Profit": "-244.42000000000002",
          "Comment": "sl 1.13320",
          "EntryTime": "2022.01.03 11:15:00",
          "ExitTime:": "2022.01.03 16:20:40"
        }
      ]
    """
    new_data = []
    skip_next_index = False
    order_number = 1

    if self.deals_length == 0 or self.orders_length == 0 or self.deals_length == None or self.orders_length == None or self.deals_length != self.orders_length:
        
        return {
           "deals:": None,
           "orders": None,
           "status": self.status
        }
    
    for counter, (deals, orders) in enumerate(zip(self.deals,self.orders)):
        
        if skip_next_index:
            skip_next_index = False
            continue

        print("Stop Loss price: ", orders["StopLossPrice"])
        print("Entry Time: ", orders["Time"])
        new_data.append({
            "Order": order_number,
            "Symbol": deals["Symbol"],
            "Type": deals["Type"],
            "Volume": deals["Volume"],
            "EntryPrice": deals["EntryPrice"],
            "StopLossPrice": deals["StopLossPrice"],
            "TakeProfitPrice": orders["TakeProfitPrice"],
            "Profit": self.deals[counter + 1]["Profit"],
            "Comment": self.deals[counter + 1]["Comment"],
            "EntryTime": orders["Time"],
            "ExitTime": self.orders[counter + 1]["Time"]
        })

        skip_next_index = True
        order_number += 1
    
    print("Data successfully refined")
    self.refined_data = new_data
