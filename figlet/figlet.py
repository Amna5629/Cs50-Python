from pyfiglet import Figlet
import sys
import random



def random_font():
    figlet = Figlet()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    s=str(input("Input:"))
    print("output:")
    print(figlet.renderText(s))

def chosen_font():
    figlet = Figlet()
    f = sys.argv[2]
    figlet.setFont(font=f)
    s=str(input("Input:"))
    print("output:")
    print(figlet.renderText(s))


if len(sys.argv) == 1:
    random_font()

elif len(sys.argv) == 3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font" :
        chosen_font()


    else:
        sys.exit("Invalid usage")

else:  
    sys.exit("Invalid usage")
