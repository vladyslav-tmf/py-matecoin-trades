import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    """
    Calculates profit and coin balance from
    trades and saves them to profit.json.

    Parameters:
        filename: Name of the file containing trade data.
    Returns:
        None
    """
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price
        elif trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    print("The profit.json file was successfully created.")
