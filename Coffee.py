# Data: Recipes for drinks (ingredients and cost)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Data: Initial resources in the machine
# Based on your example:
# If report *after* 1 latte (cost $2.50, 200ml water, 150ml milk, 24g coffee) shows:
# Water: 100, Milk: 50, Coffee: 52, Money: 2.5
# Then the *initial* state must have been:
# Water: 300, Milk: 200, Coffee: 76, Money: 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 76,
    "money": 0
}

# Data: Coin values
COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


def print_report(current_resources):
    """Prints the current resource levels in the specified format."""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    # Format money to 2 decimal places
    print(f"Money: ${current_resources['money']:.2f}")


def check_resources(drink_recipe, current_resources):
    """
    Checks if there are sufficient ingredients to make the drink.
    Returns True if resources are sufficient, False otherwise.
    """
    ingredients = drink_recipe['ingredients']
    for item in ingredients:
        if ingredients[item] > current_resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Asks the user to insert coins and returns the total monetary value.
    """
    print("Please insert coins.")
    total_value = 0
    try:
        total_value += int(input("How many quarters?: ")) * COIN_VALUES['quarters']
        total_value += int(input("How many dimes?: ")) * COIN_VALUES['dimes']
        total_value += int(input("How many nickels?: ")) * COIN_VALUES['nickels']
        total_value += int(input("How many pennies?: ")) * COIN_VALUES['pennies']
        return total_value
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0  # Return 0 to fail the transaction


def check_transaction(drink_cost, money_inserted, current_resources):
    """
    Checks if the payment is sufficient.
    If sufficient: adds payment (cost) to machine, gives change, returns True.
    If insufficient: refunds money, returns False.
    """
    if money_inserted < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_inserted - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        
        # Add the cost of the drink to the machine's money
        current_resources['money'] += drink_cost
        return True


def make_coffee(drink_name, drink_recipe, current_resources):
    """Deducts the required ingredients from resources and serves the drink."""
    ingredients = drink_recipe['ingredients']
    for item in ingredients:
        current_resources[item] -= ingredients[item]
    
    print(f"Here is your ☕ {drink_name}. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine loop."""
    is_on = True
    
    while is_on:
        # Get user input
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            # Turn off the machine
            is_on = False
            print("Turning off the machine.")
        
        elif choice == "report":
            # Print the resource report
            print_report(resources)
            
        elif choice in MENU:
            # Handle a drink order
            drink = MENU[choice]
            
            # 1. Check if resources are sufficient
            if check_resources(drink, resources):
                
                # 2. Process coins
                payment = process_coins()
                
                # 3. Check if transaction is successful
                if check_transaction(drink['cost'], payment, resources):
                    
                    # 4. Make the coffee
                    make_coffee(choice, drink, resources)
        
        else:
            print("Invalid selection. Please try again.")

# Run the machine
if __name__ == "__main__":
    coffee_machine()
