'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''

p1_score = 0
p2_score = 0
p1_name = input("Player 1 name: ")
p2_name = input("Player 2 name: ")

while True:

        long_str = """
Please choose in the ff:
     ==========
    ||Rock    ||
    ||Paper   ||
    ||Scissors||
     ==========
            """
        print(long_str)

        # ask user input
        p1 = input("%s's choice: " % p1_name)
        p1 = p1.lower()
        if p1 not in ['rock', 'paper', 'scissors']:
            print("Invalid Input")
            continue
        p2 = input("%s's choice: " % p2_name)
        p2 = p2.lower()
        if p2 not in ['rock', 'paper', 'scissors']:
            print("Invalid Input")
            continue

        # game started
        if p1 == p2:
            print("\nDRAW!")
            p1_score += .5
            p2_score += .5
        if p1 == 'rock' and p2 == 'scissors' or p1 == 'paper' and p2 == 'rock' or p1 == 'scissors' and p2 == 'paper':
            print("\n%s's wins!" % p1_name)
            p1_score += 1
        elif p1 == 'scissors' and p2 == 'rock' or p1 == 'rock' and p2 == 'paper' or p1 == 'paper' and p2 == 'scissors':
            print("\n%s's wins!" % p2_name)
            p2_score += 1

        # ask if start a new game
        y_n = input("Again? y/n: ")
        y_n = y_n.lower()
        if y_n not in ['y', 'n', 'yes', 'no']:
            print("GAME OVER!")
            break
        if y_n in ['y', 'yes']:
            continue
        if y_n in ['n', 'no']:
            break

# game statistics
long_str2 = """
%s's Score     %s's Score
%s                %s
""" % (p1_name, p2_name, p1_score, p2_score)
print(long_str2)

if p1_score > p2_score:
    print("%s's wins!" % p1_name)
    print("CONGRATULATIONS!")
if p1_score == p2_score:
    print("DRAW!")
if p1_score < p2_score:
    print("%s's wins!" % p2_name)
    print("CONGRATULATIONS!")
