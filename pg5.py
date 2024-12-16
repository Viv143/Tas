'''Write a Python program for a number guessing game where the user has to guess a number between 1 and 50. 
The program should also check if the guessed number is prime. Use a ‘while loop’ for the guessing game 
and a ‘for loop’ to check if a number is prime.'''


class NumberGuessingGame:
    def __init__(self,CorrectGuessedNumber):
        self.CorrectGuessedNumber=CorrectGuessedNumber

    def is_prime(self,num):
        if num<2:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    

    def start(self):
        print("Guess the number between 1 and 50 ")

        while True:
            guess=input("Enter your guess:")

            if guess.isdigit():
                guess=int(guess)

                if guess<1 or guess>50:
                    print("Please enter a number between 1 and 50:")
                    continue

                if guess == self.CorrectGuessedNumber:
                    print("Congratulation! You Guessed Correct Number")
                    break
                elif guess<self.CorrectGuessedNumber:
                    print("You are guessing low number compare to Correct Guessed Number")
                else:
                    print("You are guessing high number compare to Correct Guessed Number")

                if self.is_prime(guess):
                    print(f"{guess} is a prime number")
                else:
                    print(f"{guess} is not  a prime number")

            else:
                print("Please enter  a valid number")


c1=NumberGuessingGame(23)
c1.start()



        

        
