class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))

        total = dollars + half_dollars * 0.5 + quarters * 0.25
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Insufficient money")
            return False

        change = round(coins - cost, 2)
        print(f"Here is your ${change} in change.")
        return True
