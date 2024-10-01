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