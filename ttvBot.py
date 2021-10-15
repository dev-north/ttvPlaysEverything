# ldv54146isublxvs32t6k9e7a22uc1
import json
import keyboard
from termcolor import cprint
import colorama
colorama.init()
from twitchio.ext import commands


class ttvPlays(commands.Bot):

    def __init__(self):
        try:
            with open("/user.json", "r") as user:
                user_data = json.load(user)
            channel=[]
            channel.append(user_data['c_name'])
            super().__init__(token=user_data['token'], prefix='>', initial_channels=channel)
        except Exception as e:
            cprint("An error occured try restarting the program and running the setup.","red")
    async def event_ready(self):
        cprint(f"Logged in as {self.nick} and connected to","green")

    async def event_message(self, message):
        if message.echo:
            return
        with open('/keybinds.json',"r") as keybinds:
            kb=json.load(keybinds)
        msg=message.content
        for key, value in kb.items():
            if msg==value:
                keyboard.press_and_release(key)
                cprint(f"Pressed {key}","green")
                return
    def bootup(self):
        self.run()


