class CoffeeMachine:
    def __init__(self):
        # Initialize the coffee machine with default resources and state
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"
        self.fill_stage = None

    def handle_input(self, user_input):
        # Handles user input and directs it to the appropriate method based on the current state
        if self.state == "choosing_action":
            self.choose_action(user_input)
        elif self.state == "choosing_coffee":
            self.buy_coffee(user_input)
        elif self.state == "filling":
            self.fill_machine(user_input)

    def choose_action(self, action):
        # Processes the user's action choice and transitions the machine to the appropriate state
        if action == "buy":
            self.state = "choosing_coffee"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif action == "fill":
            self.state = "filling"
            self.fill_stage = "water"
            print("Write how many ml of water the coffee machine has:")
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.display_status()
        elif action == "exit":
            self.state = "exit"
        else:
            print("Invalid action")

    def buy_coffee(self, choice):
        # Handles the 'buy' action: checks resources and processes the coffee purchase
        if choice == "back":
            self.state = "choosing_action"
            return

        if choice == "1":
            water_needed, milk_needed, beans_needed, cost = 250, 0, 16, 33
        elif choice == "2":
            water_needed, milk_needed, beans_needed, cost = 350, 75, 20, 37
        elif choice == "3":
            water_needed, milk_needed, beans_needed, cost = 200, 100, 12, 37
        else:
            print("Invalid choice")
            return

        # Check if resources are sufficient
        if self.water >= water_needed and self.milk >= milk_needed and self.beans >= beans_needed and self.cups >= 1:
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost
            print("I have enough resources, making you a coffee!")
        else:
            # Print which resource is insufficient
            if self.water < water_needed:
                print("Sorry, not enough water!")
            elif self.milk < milk_needed:
                print("Sorry, not enough milk!")
            elif self.beans < beans_needed:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")

        self.state = "choosing_action"

    def fill_machine(self, user_input):
        # Handles the 'fill' action: incrementally updates resources based on user input
        if self.fill_stage == "water":
            self.water += int(user_input)
            self.fill_stage = "milk"
            print("Write how many ml of milk the coffee machine has:")
        elif self.fill_stage == "milk":
            self.milk += int(user_input)
            self.fill_stage = "beans"
            print("Write how many grams of coffee beans the coffee machine has:")
        elif self.fill_stage == "beans":
            self.beans += int(user_input)
            self.fill_stage = "cups"
            print("Write how many disposable cups of coffee you want to add:")
        elif self.fill_stage == "cups":
            self.cups += int(user_input)
            self.state = "choosing_action"

    def take_money(self):
        # Handles the 'take' action: withdraws all money from the machine
        print(f"I gave you {self.money}")
        self.money = 0

    def display_status(self):
        # Displays the current resources and money in the coffee machine
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def run(self):
        # Main loop: processes user commands until 'exit' is selected
        while self.state != "exit":
            if self.state == "choosing_action":
                print("Write action (buy, fill, take, remaining, exit):")
            user_input = input("> ")
            self.handle_input(user_input)

coffee_machine = CoffeeMachine()
coffee_machine.run()
