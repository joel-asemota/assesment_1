print("what is the best way to create a password")
print("1. creating a strong password that is combined with capital letters mixed with lowercase letters, punctuation etc.")
print("2. creating a simple and basic password that is very easy to remember so that you don't forget your password")
print("3. setting your favourite sport as a password")
lives = 3
answer = input("Enter your answer (type in the number that is the correct answer) ")
if answer == "1":
    print("well done you got the answer correct")
else: 
    print("you are incorrect, the correct answer is 1")
    lives -= 1
    print(f"your lives are {lives}")
print("is it appropriate to share your address with other strangers")
print("1. no")
print("2. yes")
print("3. sometimes")
answer = input("Enter your answer (type in the number to that is the correct answer)")
if answer == "2":
    print("well done you are correct")
else:
    print("you are incorrect, the correct answer is 2")
    lives -= 1
    print(f"your lives are {lives}")
print("should you always trust strangers?")
print("2. yes")
print("1. no")
answer = input("Enter your answer")
if answer == "1":
    print("well done")
else:
    print("sorry, your answer is incorrect, the correct answer is 1")
    lives -= 1
    print(f"your lives are {lives}")
if lives > 0:
    print("what is a spam email?")
    print("1. emails that are sent to you without your knowledge or consent")
    print("2. emails that are sending and spamming too much")
    print("3. a type of email that you can spam messages")
    answer = input("Enter your answer")
    if answer == 1:
        print("nice job")
    else:
        print("sorry, your answer is incorrect")
        lives -= 1
        print(f"your lives are now {lives}")
if lives > 0:
    print("what is malware")
    print("1. a computer virus")
    print("2. a malicious software that can force your computer to do stuffs")
    print("3. a software that is specifically designed to dsrupt, damage, or gain unauthorized access to a computer system")
    answer = input("Enter your answer")
    if answer == 3:
        print("well done you are correct")
    else:
        print("you are incorrect")
        lives -= 1
        print(f"your lives are now {lives}")
    print("why should you be careful when sharing file sites")
    answer = input("Enter your answer")
    print("1. without proper safeguards, they can result in any number of security breaches")
    print("2. sharing files means that you will instantly lose all your data")
    if answer == 1:
        print("well done")
    else:
        print("incorrect")
        lives -= 1
        print(f"your lives are {lives}")
if lives > 0: 
    print("which of these is classed as personal information")
    print("1. date of birth")
    print("2. nickname")
    print("3. Gender")
    if answer == 1:
        print("well done!")
    else:
        print("you are incorrect")
        lives -= 1
        print(f"your lives are {lives}")
if lives > 0:
    print("well done you have completed the quiz")
else:
    print("you have ran out of lives, try again")
    


        


    
    





