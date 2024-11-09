import random


while True:
    try:
        num_of_friends = int(input("Enter the number of friends joining (including you): "))
        if num_of_friends <= 0:
            print("No one is joining for the party")
            exit()
        break
    except ValueError:
        print("Please enter a valid integer for the number of friends.")
#loop with input checking to request the number of friends


friends = {}
print("Enter the name of every friend (including you), each on a new line:")
#dictionary for storing friends' names and their contributions

for _ in range(num_of_friends):
    name = input("> ")
    friends[name] = 0
#ask for each friend's name and add it to the dictionary with a default contribution of zero


while True:
    try:
        total_amount = float(input("Enter the total amount: "))
        if total_amount < 0:
            print("The total amount cannot be negative.Please enter a valid amount.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for the total amount.")
#loop with input checking for the amount: request and handle exceptions


lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
if lucky_choice != "Yes":
    print("No one is going to be lucky")
    amount_per_person = round(total_amount / num_of_friends, 2)
    for friend in friends:
        friends[friend] = amount_per_person
    print(friends)
    exit()
#we request the lucky function, everything except “Yes” will be “No”

lucky_person = random.choice(list(friends.keys()))
print(f"{lucky_person} is the lucky one!")
#random selection of lucky winner

amount_per_person = round(total_amount / (num_of_friends - 1), 2)
#calculation of the amount except the lucky one

for friend in friends:
    if friend == lucky_person:
        friends[friend] = 0
    else:
        friends[friend] = amount_per_person
#we update fees for all friends, the lucky one doesn't pay

print(friends)
