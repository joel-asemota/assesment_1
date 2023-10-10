print("what is the best way to create a password")
print("1. creating a strong password that is combined with capital letters mixed with lowercase letters, punctuation etc.")
print("2. creating a simple and basic password that is very easy to remember so that you don't forget your password")
print("3. setting your favourite sport as a password")
lives = 3
answer = input("Enter your answer ")
if answer == "1":
    print("well done you got the answer correct")
else: 
    print("you are incorrect, the correct answer is 1")
    lives -= 1
    print(f"your lives are {lives}")
