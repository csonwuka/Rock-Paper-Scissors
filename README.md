This is a game that is played between two people.
Each individual has to make one option out of a possible three: Rock, Paper or Scissors.
Rock smashes scissors. Paper wraps up the rock. Scissors shred up the paper. With this, the game is fair.

This particular game is designed to be played between the computer (CPU) and the user (Player).
The CPU makes a choice by using the python inbuilt random module. Specifically, the choice method.
The Player gets prompted to input one of "R, P, S" each representing "Rock, Paper, Scissors" respectively.

If CPU wins a particular round, "CPU wins" is printed on the console.
If the Player wins, "Player wins" is printed.
But if CPU and Player pick the same option, the game ends in a draw. The game is then restarted.

In LINE 1, the random module is imported as rd, for easy reference.
A list containing the options is created, particularly because the choice method in the random module accepts a list as its argument.
An empty string is assigned to player in order to declare an empty variable that would be used in a function later on.

I grouped most commands into functions for the sake of readability and reuse-ability.

In LINE 19, I used the global keyword to be able to modify the variable, player.
The input from the user is then assigned to player.

In LINE 63, the function, user_input() is called.  This executes the code in LINE 13. 
At the end of the function call, a while loop kicks in.

The while loop checks if the input made by the user is contained in the list of options created earlier. 
If it is not, the function, user_instruction() is called. This executes the code in LINE 66.
But if it is, the function, game_operation() is called. This executes the code in LINE 35.
This loop continues until the user (Player) inputs a valid option

In LINE 35, the function, game_operation() is initiated.
In it, the global keyword is used to access the variables, player and cpu.

Now, in LINE 37, I used a for loop to iterate each key and its corresponding value in the option dictionary.
I did this, because I wanted an autonomous reassignment and printing of whatever values the CPU and Player choose.
So that, in LINE 42, the print statement prints out the following in this particular order, "Player (Rock) : CPU (Scissors)" using the f-string method.

In LINE 44, the conditionals begin to compare the choices of the Player and CPU to determine the winner.
The print statement under each conditional prints out the corresponding result of its conditional operation.
When this happens, the game ends and the program stops.
However, if the Player and the CPU choose the same option, the function, try_again() is prompted.
The function try_again() gives the user another chance to start a new game session.# rock-paper-scissors
