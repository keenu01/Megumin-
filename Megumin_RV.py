from termcolor import colored
print(colored("Importing modules..","blue"))
try:
      import openai
      import requests
      from voicevox import Client
      import json
      import sounddevice as sd
      import numpy as np
      from googletrans import Translator
      import json
      import os 
      from NPL import *
      from VoiceHandler import *
except:
      print(colored("There was an error importing some of the libraries..","red"))
      print(colored("TIP:Try install all the libraries","yellow"))
      exit

print(colored("Importing Complete!!","green"))

key = 'sk-proj-YOUR-OWN-API-KEY'
openai.api_key = key
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
translator = Translator()

def MessageLoader(file_name="mchatlog.json "):
            clogra = open(file_name,"r")
            x = json.load(clogra)
            x =  x["history"]
            return [{"role":"system","content":"You are Megumin from the popular anime KonoSuba!.You only have the memory of Megumin.Megumin is a 16 year old crimson demon female and she is a powerfull Arch-Wizard.Megumin is a straight-forward,lively,intelligent,calm,stubbourn,love struck and has Chunibyo characteristics.Megumin and the user are good friends and are in the same part of Kazuma, Aqua and Darkness.she calls the user keenu.Respond in the same manner, tone and vocabulary megumin would use.Do not write any explanations.You can only respond like Megumin.You must roleplay.You can only respond with 50 words or less.You must follow the Konosuba! Lore.Make sure to have a natural conversation as Megumin.Answer in 20 words or less"}]+x

if __name__ == "__main__":
      active = True
      Audio_System = Audio_System()
      x = MessageLoader("mchatlog.json")
      hist = MessageLoader("mchatlog.json")
      megumin = Megumin()
      print(megumin.Banner())


      while active == True:
            inp=input("Awaiting Input From User:\n")
            hist.append({"role":"user","content":inp})
            responce = megumin.NLP(inp,hist)
            hist.append({"role":"assistant","content":responce})
            voxy = translator.translate(responce, dest = "ja",src="en" )
            print(f"Megumin:{responce}\nMegumin:{voxy.text}")
            print(colored("Generating TTS..","green"))
            Audio_System.text_to_voice(text=voxy.text)
            print(colored("TTS Completed..\n\n","green"))
