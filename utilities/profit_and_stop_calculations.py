from decimal import Decimal

def get_value_rounded(value, symbol):
    results = get_symbol_decimal(symbol)

    if results >= 4:
        return value * 10000

    if results == 3:
        return value * 100

    if results <= 2:
        return value

def get_take_profit_in_pips(symbol, trade_type, entry_price, take_profit_price):
    """
    Return the take profit in pips
    """
    take_profit = 0

    if trade_type == "Buy":
        take_profit = take_profit_price - entry_price

    if trade_type == "Sell":
        take_profit = entry_price - take_profit_price

    return round(get_value_rounded(take_profit, symbol), 2)


def get_stop_loss_pips(symbol, trade_type, entry_price, stop_loss_price):
    """
    Return the stop loss
    """
    stop_loss = 0

    if trade_type == "Buy":
        stop_loss = entry_price - stop_loss_price

    if trade_type == "Sell":
        stop_loss = stop_loss_price - entry_price

    return round(get_value_rounded(stop_loss, symbol), 2)

def get_symbol_decimal(symbol):
    """
    Return the decimal points of a symbol
    """
    symbol_information = {
        "GBPJPY": 3,
        "EURUSD": 4,
        "Nasdaq": 2,
        "Gold": 2,
        "USDZAR": 4
    }

    return symbol_information[symbol]

print(get_stop_loss_pips("EURUSD", "Sell", 0.99650, 1.00000))