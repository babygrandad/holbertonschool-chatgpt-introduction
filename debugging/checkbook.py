class Checkbook:
    """
    Class Description:
    Represents a simple checkbook system with functionalities to deposit, withdraw, and check balance.

    Attributes:
    - balance (float): The current balance in the checkbook.

    Methods:
    - __init__(): Initializes the checkbook with a balance of 0.0.
    - deposit(amount): Deposits the specified amount into the checkbook.
    - withdraw(amount): Withdraws the specified amount from the checkbook, if sufficient funds are available.
    - get_balance(): Displays the current balance of the checkbook.
    """

    def __init__(self):
        """
        Function Description:
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposits the specified amount into the checkbook.

        Parameters:
        - amount (float): The amount to be deposited into the checkbook.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws the specified amount from the checkbook, if sufficient funds are available.

        Parameters:
        - amount (float): The amount to be withdrawn from the checkbook.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Displays the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function Description:
    Executes the main functionality of the checkbook system, allowing users to interact with the checkbook.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
