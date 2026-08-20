import random
print("Welcome to the number guessing game!")
a = random.randint(1,200)
count =0
while True:
    x = int(input("Guess the number that is between 1 and 200: "))
    if x==a:
        print("You nailed it! You guessed the number correctly.")
        count+=1
        break
    elif x>a:
        print("Try lower!")
        count+=1

        continue
        
    else:
        print("Try higher!")
        count+=1
        continue
        
print(f"You got the number in your {count} tries!")