print("Hello! My name is Mom`s Hacker.")
print("I was created in 2024.")
#1
print("Please, remind me your name.")
name = input("> ")

print(f"What a great name you have, {name}")
#2
print("Let me guess your age.")
print("Enter remainders of dividing your by 3,5 and 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 *15) % 105

print(f"Your age is {age}; that`s a good time to start programming")
#3
print("Now I will prove to you that Ican count to any number you want.")
number = int(input("> "))

for i in range(number + 1):
    print(f"{i} !")
print("Completed, have a nice day!")
#4
def test_qustion():
    print("Let`s test your programming knowledge.")
    print("Why programming?")
    print("1. To automate tasks.")
    print("2. To create problems.")
    print("3. To create computer viruses.")
    print("4. To learn all programming languages.")

    while True:
        answer = int(input("> "))
        if answer == 1:
            print("Congratulations, have a nice day!")
            break
        else:
            print("Please, try again.")

test_qustion()
#5