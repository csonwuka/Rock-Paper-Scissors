import random as rd

option_list = ["R", "P", "S"]
cpu = rd.choice(option_list)
player = ""
option_dict = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}


def user_input():
    print('''
Choose from the option below :
(R stands for Rock, P stands for Paper, S stands for Scissors)
''')
    print(option_list)
    global player
    player = str(input("Choose an option in uppercase: "))


def try_again():
    user_response = str(input("Do you want to play again: (Yes /No) ")).upper()
    if user_response == "YES":
        user_input()
        game_operation()
    elif user_response == "NO":
        print("Okay, see you next time :)")
    else:
        print("PLEASE ENTER ONLY \'Yes\' Or \'No\'")
        try_again()


def game_operation():
    global player, cpu
    for x, y in option_dict.items():
        if player == x:
            player = y
        if cpu == x:
            cpu = y
    print(f"Player ({player}) : CPU ({cpu})")

    if player == "Rock" and cpu == "Paper":
        print("Paper wraps Rock. CPU wins.")
    elif player == "Rock" and cpu == "Scissors":
        print("Rock smashes Scissors. Player wins.")
    elif player == "Paper" and cpu == "Rock":
        print("Paper wraps Rock. Player wins.")
    elif player == "Paper" and cpu == "Scissors":
        print("Scissors shreds the Paper. CPU wins.")
    elif player == "Scissors" and cpu == "Rock":
        print("Rock smashes Scissors. CPU wins.")
    elif player == "Scissors" and cpu == "Paper":
        print("Scissors shreds the Paper. Player wins.")
    elif player == cpu:
        print("The game is a draw. There is no winner.")
        try_again()
    else:
        pass


user_input()


def user_instruction():
    print('''
ERROR. YOU CAN ONLY CHOOSE ONE OPTION AMONG 'R', 'P', 'S'
YOUR OPTION MUST BE IN UPPERCASE LIKE THIS INSTRUCTION
''')
    print(option_list)
    global player
    player = str(input("Choose an option in uppercase: "))


while player not in option_list:
    user_instruction()
else:
    game_operation()
