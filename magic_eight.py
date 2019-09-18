def ask_question():
    question = input("What is your question?")
    check_question(question)






def check_question(question):
    if question[-1] is "?":
        answer_question()
    elif question is "quit" or "Quit" or "quit." or "Quit.":
        print("Talk to you later.")
    else:
        ask_question()
