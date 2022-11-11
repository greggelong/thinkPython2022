import math



def evalLoop():

    while True:
        ex = input("type an expression or done to quit: ")
        if ex == "done":
            break
        print(eval(ex))
        


evalLoop()


