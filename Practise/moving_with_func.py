#def hello(name): #def hello(fname,lname,age):
#    print("hello! "+name)
    #print("You are "+str(age)+" years old.")
#    print("have a nice day!")
#hello("Vandan")
#hello("Thakar")
#my_name = "Vandy"
#hello(my_name)
#hello("Vandan","Thakar",19)
#-----------------------------------------------------
#def multiply(n1,n2):
#    res = n1*n2
#    return res #or simply return n1*n2
#x = multiply(6,8)
#print(x)
#-----------------------------------------------------
#def hello(fname,mname,lname):
#    print("hello "+fname+" "+mname+" "+lname)
#hello(fname="Vandan",lname="Thakar",mname="Devangbhai")
#-----------------------------------------------------
#num = input("Enter a whole positive integer :")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("Enter a whole positive integer :")))))
#-----------------------------------------------------
#name = "Thakar"
#def display_name():
#    name = "Vandan" #local variable / local scope
#    print(name)
#display_name()
#print(name) # if no global variable / global scope -> error
#-----------------------------------------------------
#def add(n1,n2):
#    return n1+n2
#print(add(1,2))

#OR

#def add(*args): # instead of args it can be any name just '*' must be there
#    sum = 0
#    args = list(args)
#    args[0] = 0
#    for i in args:
#        sum += i
#    return sum
#print(add(1,2,3,4,5,6))
#-----------------------------------------------------
#def hello(**kwargs): # instead of kwargs can use any name but there must be '**'
#    print("Hello ",end=" ")
#    for key,value in kwargs.items():
#        print(value,end=" ")
#hello(title="Mr.",first='Vandan',middle="Devangbhai",last='Thakar')
#-----------------------------------------------------
#animal = "cow"
#title = "moon"

#print("The {} jumped over the {}".format(animal,title))
#print("The {1} jumped over the {0}".format(animal,title)) #positional argument
#print("The {animal} jumped over the {title}".format(animal="cow",title="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,title))

#name = "Vandan"
#print("Hello my name is {}".format(name))
#print("Hello my name is {:10}. Nice to meet you!".format(name)) # padding between vandan and nice
#print("Hello my name is {:<10}. Nice to meet you!".format(name)) # left aligned padding
#print("Hello my name is {:>10}. Nice to meet you!".format(name)) # right aligned padding
#print("Hello my name is {:^10}. Nice to meet you!".format(name)) # center aligned padding

#number = 1000
#print("The no. pi is {:.2f}".format(number)) #upto 2 decimal places printed
#print("The no. pi is {:.3f}".format(number))
#print("The no. pi is {:,}".format(number))
#print("The no. pi is {:b}".format(number)) # binary
#print("The no. pi is {:o}".format(number)) # octal
#print("The no. pi is {:X}".format(number)) # hexadecimal
#-----------------------------------------------------
#import random
#x = random.randint(1,10)
#y = random.random()

#mylist = ['rock','paper','scissors']
#z = random.choice(mylist)

#cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
#random.shuffle(cards)

#print(cards)
#-----------------------------------------------------
#try:
#    numerator = int(input("Enter numerator :"))
#    denominator = int(input("Enter denominator :"))
#    res = numerator / denominator
#except ZeroDivisionError as e:
#    print(e)
#    print("You cannot divide by zero!")
#except ValueError as e:
#    print(e)
#    print("Enter only numbers pls!")
#except Exception as e:
#    print(e)
#   print("Something went Wrong!")
#else:
#    print(res)
#finally:
#    print("This will always execute!")
#-----------------------------------------------------
#try:
#   with open('test.txt') as file:
#    print(file.read())
#except FileNotFoundError:
#   print("That file was not found!")
#-----------------------------------------------------
#text = "Yoooooo\nThis is some text\nHave a good one!"
#with open('test.txt','w') as file: #if 'w' is there it will overwrite text that you put...but instead if 'a' is there , it will append the text
#    file.write(text)
#-----------------------------------------------------
#import random
#while True:
#    choices = ['rock','paper','scissors']
#    computer = random.choice(choices)
#    player = None
#    while player not in choices:
#        player = input("rock,paper or scissors? :").lower()
#    if player == computer:
#        print("computer :",computer)
#        print("player :",player)
#        print("Tie!")
#    elif player == 'rock':
#        if computer == 'paper':
#            print("computer :",computer)
#            print("player :",player)
#            print("You Lose!")
#        if computer == 'scissors':
#            print("computer :",computer)
#            print("player :",player)
#            print("You WIN!")
#    elif player == 'paper':
#        if computer == 'rock':
#            print("computer :",computer)
#            print("player :",player)
#            print("You WIN!")
#        if computer == 'scissors':
#            print("computer :",computer)
#            print("player :",player)
#            print("You Lose!")
#    elif player == 'scissors':
#        if computer == 'rock':
#            print("computer :",computer)
#            print("player :",player)
#            print("You Lose!")
#        if computer == 'paper':
#            print("computer :",computer)
#            print("player :",player)
#            print("You WIN!")
#    play_again = input("Play Again? (yes/no) :").lower()
#    if play_again != "yes":
#        break
#print('Bye!')
#-----------------------------------------------------
#def new_game():
#    guesses = []
#    correct_guesses = 0
#    question_num = 1

#    for key in questions:
#        print("----------------")
#        print(key)
#        for i in options[question_num-1]:
#            print(i)
#        guess = input("Enter (A,B,C or D) :")
#        guess = guess.upper()
#        guesses.append(guess)

#        correct_guesses += check_answer(questions.get(key),guess)
#        question_num += 1

#    display_score(correct_guesses,guesses)
        
#def check_answer(answer,guess):
#    if answer == guess:
#        print("CORRECT!")
#        return 1
#    else:
#        print("WRONG!")
#        return 0
    
#def display_score(correct_guesses,guesses):
#        print("----------------")
#        print("RESULTS!")
#        print("----------------")

#        print("Answers :",end="")
#        for i in questions:
#            print(questions.get(i),end=" ")
#        print()

#        print("Guesses :",end="")
#        for i in guesses:
#            print(i,end=" ")
#        print()

#        score = int((correct_guesses/len(questions))*100)
#        print("Your score is :"+str(score)+"%")
#def play_again():
#    response = input("Do you want to Play Again? (yes/no) :")
#    response = response.upper()

#    if response == 'YES':
#        return True
#    else:
#        return False
#questions = {"Who created Python? :": "A","What year was Python created? :": "B","Python is tributed to which comedy group? :": "C","Is the Earth round? :": "D"}
#options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Vandan Thakar"],["A. 1989", "B. 2004", "C.1991", "D. 2000"],["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

#new_game()

#while play_again():
#    new_game()
#print("BYE!")
#-----------------------------------------------------
#class Car:
#    make = None
#    model = None
#    year = None
#    color = None

#    def __init__(self,make,model,year,color):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.color = color
        
#    def drive(self):
#        print("This "+self.model+" is driving")

#    def stop(self):
#        print("This "+self.model+" hass stopped")

#car_1 = Car("Cheverollet","Corvette","2021","black")
#car_2 = Car("Ford","Mustang","2020","yellow")

#print(car_1.make)
#print(car_1.model)
#print(car_1.year)
#print(car_1.color)
#car_1.drive()
#car_2.stop()
#-----------------------------------------------------
