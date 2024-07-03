import random

class ProblemGenerator:
    def numgenerator(self):
        # This will generate the equations. For now, I will start with x, then add other arithmetic operations.
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        prob1 = x + y
        prob2 = x + y + z
        prob3 = x * y
        prob4 = x * y * z
        choice = ('BABY', 'EASY', 'MED', 'HARD')
        question = input(f"How hard do you want to practice? {choice}: ").strip().upper()
        match question:
            case 'BABY':
                print(f"Problem: {x} + {y}")
                probstring = f"{x} + {y}"
                return prob1, probstring
            case 'EASY':
                print(f"Problem: {x} + {y} + {z}")
                probstring = f"{x} + {y} + {z}"
                return prob2, probstring
            case 'MED':
                print(f"Problem: {x} x {y}")
                probstring = f"{x} x {y}"
                return prob3, probstring
            case 'HARD':
                print(f"Problem: {x} x {y} x {z}")
                probstring = f"{x} x {y} x {z}"
                return prob4, probstring
            case _:
                print("Wrong input")
                return None, None

    def sassy(self, sass):
        # Basic case output based on the number of times you get it wrong (1-3) and how quickly you answer right (4,5)
        sass_dict = {
            1: 'Wrong, rub the two braincells together and try again',
            2: '....Try again, and THINK this time',
            3: 'Ok, you are not 12, how do you not know this ??',
            4: 'Wooow, congrats. you FINALLY did it',
            5: 'Oh, wow. I guess you\'re not an idiot.',
            6: 'Wanna go again? or are you too scared?',
            7: 'Jesus, go back to school, this is the answer:'
        }
        return sass_dict.get(sass, "Invalid input")

if __name__ == "__main__":
    nombre = input("Hello, this is your math tutor. How may I help you? Mr/Ms ...? ")
    selection = input(f"Hello Mr/Ms {nombre}, will you take a class? (yes/no): ").strip().lower()
    
    if selection == 'yes':
        pg = ProblemGenerator()
        while True:
            result, probstring = pg.numgenerator()
            if result is not None:
                attempts = 0
                while True:
                    try:
                        answer = int(input(f"Enter your answer to {probstring}: "))
                        if answer == result:
                            if attempts == 0:
                                print(pg.sassy(5))
                            else:
                                print(pg.sassy(4))
                            break
                        else:
                            attempts += 1
                            if attempts <= 3:
                                print(pg.sassy(attempts))
                            else:
                                print(pg.sassy(7) + f" {result}")
                                break
                    except ValueError:
                        print("Invalid input, please enter an integer.")

                another = input("Do you want to solve another problem? (yes/no): ").strip().lower()
                if another != 'yes':
                    print("Thank you for practicing! Goodbye!")
                    break
    else:
        print("Goodbye!")
