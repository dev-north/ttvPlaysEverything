import json
import time
from time import sleep

import keyboard
import termcolor
from termcolor import cprint

from clear import clear


class Setup():

    def __init__(self) -> None:
        pass

    def userSetup(self):
        cprint(text="Welcome to User setup.\nThis step will help you setup the bot which will read your chat.\nSteps to do that are...\n", color='yellow')
        time.sleep(2)
        cprint(text="Go to https://twitchtokengenerator.com/ and click on Bot Token and copy the access token(Do this off screen your token must be kept safe)", color="yellow")
        cprint(text="Paste the token here when prompted", color="yellow")
        time.sleep(5)
        cprint(text="Enter your access token", color="green")

        token = str(input())
        token_dict = {"token": token}

        cprint("Enter the name of your twitch channel with appropriate capitalization","yellow")
        channel_name=str(input())
        token_dict.update({"c_name": channel_name})


        with open("/user.json", "w") as user:
            user.write(json.dumps(token_dict))

        clear()
        cprint(text="User config done successfully", color="green")
        return

    def keybindSetup(self):
        cprint(text="Welcome to Keybinds Setup.\nThis step will setup the chat messages and keybinds for your stream.", color="blue")
        cprint(text="The Keybinds you create will be global and for all games.\nAny keybinds created earlier will be overwritten.", color="blue")
        cprint(text="Continue[Y/N]...", color="green")

        ch = str(input())
        ch = ch.lower()
        keyDict = {}

        while ch == 'y':
            cprint(text="Press the key you want to bind.", color="cyan")
            k = keyboard.read_event()
            time.sleep(1)
            keyboard.press_and_release('backspace')
            cprint(text=f'Enter chat message to press {k.name}', color="cyan")
            chatMsg = str(input())
            keyDict.update({k.name: chatMsg})
            cprint(
                text="Enter Y to add more keybind OR enter N to exit keybind setup", color="green")
            ch = str(input()).lower()

        else:
            with open("/keybinds.json", "w") as keybinds:
                keybinds.write(json.dumps(keyDict))

        clear()
        cprint("Keybinds setup done successfuly", color="green")
        return
