import time

def playNIM():
    
    printInstructions()
    print("Let's play NIM!")
    print("")
    n = int(input("How many stones do you want to play with? "))
    m = int(input("How many stones can you remove at a time? "))
    if (n <= 0) or (m <= 0) or m > n:
        print("Invalid Input\n")
        time.sleep(1)
        return playNIM()
    print("")

    condition = whoStarts(n, m)
    while n > 0:
        if condition == True:
            n = n - userChooseMove(n, m)
            printStones(n)
            condition = False
        else:
            n = n - computerChooseMove(n, m)
            printStones(n)
            condition = True

    if condition == False:
        print("You win!")
    else:    
        print("I win!")

def whoStarts (n, m):
    if (n % m + 1) == 0:
        print("You start!")
        return True
    else:
        print("I start!")
        return False

def computerChooseMove (n, m):
    num = n % (m + 1)
    if num > m:
        time.sleep(1)
        print("I remove", m, "stones.\n")
        time.sleep(1)
        return m
    else:
        time.sleep(1)
        print("I remove", num, "stones.\n")
        time.sleep(1)
        return num

def userChooseMove (n, m):
    num = int(input("How many stones do you want to remove? "))
    if num > m:
        print("You can't remove more than", num, "stones!\n")
        return userChooseMove(n, m)
    elif num <= 0:
        print("You can't remove less than 1 stone!\n")
        return userChooseMove(n, m)
    else:
        print("You removed", num, "stones.\n")
        return num

def printInstructions():
    print("---------------------------------------------------------------------------------")
    print("This is a game of NIM.")
    print("There are n stones in a pile.")
    print("You and I take turns removing stones.")
    print("In each turn, the player must remove at least 1 stone and at most m stones.")
    print("The player who removes the last stone wins.")
    print("---------------------------------------------------------------------------------\n")



def printStones(n):
    print("There are", n, "stones left.")
    for i in range(n):
        print("O ", end=" ")
    print("")

def main():
    playNIM()

main()
    