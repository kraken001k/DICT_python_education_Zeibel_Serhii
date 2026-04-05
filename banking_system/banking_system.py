import random
import sqlite3
import sys


connect_sqlite3 = sqlite3.connect('card.s3db') # Create or connect to a SQLite database file
cursor_connection = connect_sqlite3.cursor() # We get a "cursor" - an object for executing SQL queries

# Create the card table if it doesn't exist yet
cursor_connection.execute('''CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
    );''')
connect_sqlite3.commit() # Save changes


def luhn_check_summary(card_number_without_checking_summary):
    """
    Calculates the check digit using the Luhn algorithm
    (based on the first 15 digits of the card number).
    """
    digits = [int(digit) for digit in card_number_without_checking_summary]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    return (10 - total % 10) % 10


def generate_card_number():
    """
    Generates a unique card number:
    - BIN = 444111
    - account ID = random 9-digit number
    - the last digit is a control digit (according to the Luhn algorithm)
    """
    bank_bin = '444111'
    while True:
        account_id = f'{random.randint(0, 999999999)}'
        partial_card_number = bank_bin + account_id
        check_summary = luhn_check_summary(partial_card_number)
        card_number = partial_card_number + str(check_summary)
        cursor_connection.execute('SELECT number FROM card WHERE number = ?', (card_number,))
        if not cursor_connection.fetchone():
            return card_number


# Generate PIN code
def generate_pin():
    return f'{random.randint(0, 9999):04d}'


def create_account():
    """
    Generates a new card and PIN code, saves them to the database.
    """
    card_number = generate_card_number()
    pin = generate_pin()
    cursor_connection.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (card_number, pin))
    connect_sqlite3.commit()
    print('Your card has been created')
    print('Your card number:')
    print(card_number)
    print('Your card pin:')
    print(pin)


def add_income(number):
    """
    Adds an amount to the user's account.
    """
    income_input = input('Enter income:\n> ')
    if not income_input.isdigit():
        print('Incorrect input!')
        return
    income = int(income_input)
    cursor_connection.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (income, number))
    connect_sqlite3.commit()
    print('Income was added!')


def luhn_valid(card_number):
    """
    Checks if the map is correct according to the Luhn algorithm.
    """
    check_digit = int(card_number[-1])
    calculated = luhn_check_summary(card_number[:-1])
    return check_digit == calculated


def do_transfer(sender_number):
    """
    Transferring money from one card to another:
    - Luna check
    - does the recipient's card exist
    - does the sender have enough money
    - updating the balance
    """
    print('Transfer')
    target = input('Enter card number:\n> ')
    if target == sender_number:
        print('You cant transfer money to the same account')
        return
    if not target.isdigit():
        print('Incorrect input')
        return
    if not luhn_valid(target):
        print('Probably you made a mistake in the card number. Try again')
        return

    # Check if the map exists
    cursor_connection.execute('SELECT * FROM card WHERE number = ?', (target,))
    if not cursor_connection.fetchone():
        print('Such a card number doesnt exist')
        return

    # Transfer amount
    amount_input = input('Enter how much money you want to transfer:\n> ')
    if not amount_input.isdigit() or int(amount_input) <= 0:
        print('Incorrect input!')
        return
    amount = int(amount_input)

    # Checking the sender's balance
    cursor_connection.execute('SELECT balance FROM card WHERE number = ?', (sender_number,))
    sender_balance = cursor_connection.fetchone()[0]
    if amount > sender_balance:
        print('You dont have enough money')
        return

    # Translation: we take from one, we add to another
    cursor_connection.execute('UPDATE card SET balance = balance - ? WHERE number = ?', (amount, sender_number))
    cursor_connection.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (amount, target))
    connect_sqlite3.commit()
    print('Success!')


def close_account(number):
    """
    Deletes an account from the database.
    """
    cursor_connection.execute('DELETE FROM card WHERE number = ?', (number,))
    connect_sqlite3.commit()
    print('The account has been closed')


def logging():
    """
    User authorization by card number and PIN code.
    If login is successful, access to the internal menu is provided:
    - balance
    - replenishment
    - transfer
    - account deletion
    - account logout
    """
    number = input('Enter your card number:\n> ')
    pin = input('Enter your PIN:\n> ')
    cursor_connection.execute('SELECT * FROM card WHERE number = ? AND pin = ?', (number, pin))
    row = cursor_connection.fetchone()
    if row:
        print('You have successfully entered your account')
        while True:
            print('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
''')
            choice = input('> ')
            if choice == '1':
                cursor_connection.execute('SELECT balance FROM card WHERE number = ?', (number,))
                balance = cursor_connection.fetchone()[0]
                print(f'Balance: {balance}')
            elif choice == '2':
                add_income(number)
            elif choice == '3':
                do_transfer(number)
            elif choice == '4':
                close_account(number)
                break
            elif choice == '5':
                print('You have successfully logged out')
                break
            elif choice == '0':
                print('Bye!')
                connect_sqlite3.close()
                sys.exit()
            else:
                print('Incorrect input! Choose number from 0 to 5')
    else:
        print('Wrong card number or PIN!')


def main():
    """
    Main application menu:
    - account creation
    - account login
    - shutdown
    """
    while True:
        print('''
1. Create an account
2. Log into account
0. Exit
''')
        choice = input('> ')
        if choice == '1':
            create_account()
        elif choice == '2':
            logging()
        elif choice == '0':
            print('Bye!')
            connect_sqlite3.close()
            break
        else:
            print('Incorrect input! Choose number from 0 to 2')


if __name__ == '__main__':
    main()
