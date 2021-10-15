import time

from termcolor import cprint
import colorama
colorama.init()
from initialSetup import *
from ttvBot import ttvPlays

ttvp=ttvPlays()

choice=0
def welcome():
    global choice
    cprint(text="Welcome to TTV Plays Everything. Made by North\n",color="magenta")
    cprint(text='Enter the number corresponding to the choices listed below to make a selection\n',color="magenta")
    cprint(text='1 > Setup the bot(mandatory when ran for the first time)\n2 > Tutorial(Info on how to use the thingie)\n3 > Play(Let the chat play for you)\n4 > Credits', color="magenta")
    cprint(text="Enter your choice...",color="green")
    choice = int(input())
    resolve(choice)

def resolve(choice):

    if choice==1:

        cprint("You selected to run the setup\n",color="cyan")
        cprint(text='Enter the number corresponding to the choices listed below to make a selection\n',color="cyan")
        cprint(text='1 > Enter user details(user token)\n2 > Keybinds Settings', color="cyan")
        cprint(text="Enter your choice...",color="green")
        ans=int(input())
        s=Setup()
        
        if ans==1:
            s.userSetup()
            welcome()
        elif ans==2:
            s.keybindSetup()
            welcome()
    elif choice==2:
        cprint("Go to  for a walkthrough.\n","yellow")
        welcome()
    elif choice==3:
        cprint("Press Enter when ready to start","green")
        keyboard.wait(hotkey="enter")
        cprint("Bot will start listening to chat in 10 seconds.","red")
        time.sleep(10)
        ttvp.bootup()

    elif choice==4:
        cprint("Credits Placeholder","magenta")
        welcome()
    else:
        cprint(text="Invalid Choice, please enter a number corresponding to the choices below.",color="red")
        time.sleep(2)
        welcome()

if __name__=="__main__":
    welcome()
