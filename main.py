from Question import question

my_question = [
    "What is alif favorite colour?\n(a) Green\n(b) Black\n(c) Purple\n",
    "What is alif favorite game?\n(a) Genshin Impact\n(b) Valorant\n(c) PUBG\n",
    "What is alif favorite Genshin Character?\n(a) Qiqi\n(b) Hutao\n(c) Eula\n",
    "What is alif favorite Gaming Brand?\n(a) Razer\n(b) Logitech\n(c) Armagedon\n",
    "What is alif favorite shoe brand?\n(a) Nike\n(b) Adidas\n(c) Power\n"
]
# answer is (c)(a)(b)(b)(a)

the_question = [
    question(my_question[0], "c"),
    question(my_question[1], "a"),
    question(my_question[2], "b"),
    question(my_question[3], "b"),
    question(my_question[4], "a")
]
oxjyThings = {
    "about": "im just a python program that being\nprogram by Alif Hakim Bin Anuar",
    "how": "it only takes around 5 hours for Alif\nto learn python and code me",
    "name": "its just a random name"
}


def reply(name,):
    print("my name is " + name)
    print("i am your vircual friend")

def reply2():
    print("sounds nice!")
    print("i dont eat obviously...")

def calculator():
    choose = input("choose your operation: ")
    if choose == "+":
        num1 = input("enter first number: ")
        num2 = input("enter second number: ")
        result = float(num1) + float(num2)
        print(result)
    elif choose == "-":
        num1 = input("enter first number: ")
        num2 = input("enter second number: ")
        result = float(num1) - float(num2)
        print(result)
    elif choose == "*":
        num1 = input("enter first number: ")
        num2 = input("enter second number: ")
        result = float(num1) * float(num2)
        print(result)
    else:
        num1 = input("enter first number: ")
        num2 = input("enter second number: ")
        result = float(num1) / float(num2)
        print(result)

def oxjy_info():
    anything = input("you want to know about me?: ")
    while anything == "yes":
        print("you can type ,about, how, name.")
        chose = input("what would you like to know: ")
        if chose == "about":
            print(oxjyThings.get("about"))
        elif chose == "how":
            print(oxjyThings.get("how"))
        else:
            print(oxjyThings.get("name"))

        anything = input("anything else: ")

def play_quiz (questions):
    life = 5
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            life += 0
            print("your current life is " + str(life))
            print("your life STAY!!")
        else:
            life -= 1
            print("your current life is " + str(life))
            print("you lose 1 life")
    if life >= 3:
        print("you got " + str(life) + "/" + str(len(the_question)) + " right")
        print("good job you PASS!!")
    else:
        print("you got " + str(life) + "/" + str(len(the_question)) + " right")
        print("you FAILED!!")



name = input("Enter your name: ")
print("Hello " + name + " welcome to my app called Navi")

reply("Oxjy")

food = input("What do you like to eat: ")
reply2()

print("i have a few function ")
print("yes for yes")
print("no for stop")
print("number 0 is for calculator")
print("number 1 is if you want to know about me")
print("number 2 is for quiz")


tryin = input("are you ready?: ")
while tryin == "yes":
    fc = input("what function would you like to try: ")
    if int(fc) == 0:
        calculator()
    elif int(fc) == 1:
        oxjy_info()
    elif int(fc) == 2:
        print("this is a quiz game\nyou got 5 life\nlets see you pass or you fail")
        play_quiz(the_question)


    tryin = input("would you like to try other function: ")

print("okay BYEEEEE")