import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(data.resources)
cashier_instance = Cashier




def main():
    choice = input("What would you like? (small/ medium/ large/ off/ report) ").strip().lower()
    if choice == "small" or choice == "medium" or choice == "large":
        size = choice
        size_details = recipes[choice]
        if sandwich_maker_instance.check_resources(size_details["ingredients"]):
            cash = cashier_instance.process_coins()

            if cashier_instance.transaction_result(cash, size_details["cost"]):
                sandwich_maker_instance.make_sandwich(size, size_details["ingredients"])

                cont = input("Would you like to continue? (y/n) ").strip().lower()
                if cont == "y":
                    pass
                else:
                    on = False

            else:
                print("Insufficient money")
                on = False
        else:
            on = False
    elif choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    elif choice == "off":
        print("Goodbye!")
        on = False
    else:
        print("Invalid input, please try again.")

if __name__=="__main__":
    main()
