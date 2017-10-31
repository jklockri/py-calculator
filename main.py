import re

previous = 0
run = True

def math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter some math:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    elif equation == 'clear':
        previous = 0
    else:
        equation = re.sub('[A-Za-z.,:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    math()
