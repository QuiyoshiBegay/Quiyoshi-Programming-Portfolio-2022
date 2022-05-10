def rollDie(sides):
    """This function rolls a die and returns the roll. To use type "rollDie()"
     and pass in the number of sides the die has."""
    import random
    roll = random.randint(1, sides)
    return roll


def pickCard(deck):
    """This function chooses a random card out of a deck list. To use type
    "pickCard()" and pass in a deck/list."""
    import random
    card = random.choice(deck)
    return card


# ask yes no or flip coin or ask a number
def ask_yes_no(question):
    """Asks the user a yes or no question until they answer yes or no and
    returns their answer. To use type "askYesNo()" and pass in a question"""
    while True:
        answer = input(question)
        if "y" in answer.lower() and "n" in answer.lower():
            print("Not a valid option")
        elif "y" in answer.lower():
            return "yes"
        elif "n" in answer.lower():
            return "no"
        else:
            print("It's a yes or no question...")


def flipCoin():
    """Flips a coin and returns Heads or Tails. To use type "flipCoin()"."""
    import random
    choices = ["Heads", "Tails"]
    results = random.choice(choices)
    return results


def ask_number_in_range(question, low, high):
    """Ask the user to choose a number with a given range and return the number if it
       is a good value. To use the function type "askNumber()" and pass in a question,
       a minimum value, and a maximum value in that order. Returns the number."""
    while True:
        number = input(question)
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                if number > high:
                    print("That number is too high")
                else:
                    print("That number is too low")
        except:
            print("Not a good number")


def pick_from_menu(choices, prompt):
    """This function gets a user's choice from a list of choices. To use type "askQuestion()" and pass in a list of
         choices. The choice the user chose will be returned."""
    for i in range(len(choices)):
        print(str.format("{0}. {1}", i + 1, choices[i]))
    while True:
        answer = input(prompt)
        try:
            answer = int(answer)
        except:
            print("Invalid option")
        else:
            if 0 < answer <= len(choices):
                return choices[answer - 1]
            elif answer < 1:
                print("Your choice is too low")
            else:
                print("Your choice is too high")