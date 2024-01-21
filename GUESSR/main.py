from random import *

attempts: int = 0
answer: int = 0

def new_game():
    global answer, attempts
    answer = round(random() * 100)
    attempts = 10

    update()
    return

def header():
    print(" =============== GUESSR PLAY ============= ")
    print(" == Guess the number between 0 and 100! == ")
    return

def play_again() -> bool:
    print(" =============== WANNA PLAY AGAIN? ============= ")
    print(" ===================== Y/N ===================== ")
    
    pa = input()

    return pa.lower() == "y"


def game_over():
    print(" =============== GAME OVER ============= ")
    print(" =========== THE ANSWER WAS ============ ")
    print(answer)

    # Ask if want to play more
    if(play_again()):
        return new_game()
    return

def game_won():
    print(" =============== YOU WON! ============== ")
    print(" =========== THE ANSWER WAS ============ ")
    print(answer)

    # Ask if want to play more
    if(play_again()):
        return new_game()
    return


def update():
    global attempts

    header()
    guess = int(input())
    print(" == You guessed: "+str(guess))
    if(guess == answer):
        game_won()
    else: 
        if(guess < answer):
            print(" == GREATER...")
        else:
            print(" == LESSER...")
        attempts -= 1
        if(attempts < 1):
            game_over()
            return
        print(" == You have "+str(attempts)+" left.")
        return update()
    return
def main():
    new_game()
    return


if __name__ == "__main__":
    main()