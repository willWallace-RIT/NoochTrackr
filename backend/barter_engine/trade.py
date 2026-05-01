def match_trades(state):
    inventory = state["inventory"]

    trades = []

    if len(inventory) > 2:
        trades.append({
            "offer": inventory[0],
            "request": inventory[1]
        })

    return trades
