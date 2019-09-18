import random

def ask_question():
    question = input("What is your question?")
    check_question(question)

def answer_question():
    magic_ball = {1:"It is certain", 2:"It is decidedly so", 3: "Without a doubt", 4:"Yes-definitely", 5:"You may rely on it", 20: "As I see it, yes", 6:"Most likely", 7: "Outlook good", 8:"Yes", 9:"Signs point to yes", 10:"Reply hazy, try again", 11:"Ask again later", 12:"Better not tell you now", 13:"Cannot predict now", 14:"Concentrate and ask again", 15:"Don't count on it", 16:"My reply is no", 17:"My sources say no", 18:"Outlook not so good", 19:"Very doubtful"}
    answer = random.randint(1,20)
    print(magic_ball[answer])

def check_question(question):
    if question[-1] is "?":
        answer_question()
    elif question is "quit" or "Quit" or "quit." or "Quit.":
        print("Talk to you later.")
    else:
        ask_question()

ask_question()
