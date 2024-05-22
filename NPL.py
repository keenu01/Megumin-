from termcolor import colored
import json
import openai
class Megumin():
      def __init__(self):
            pass

      def Banner(self)-> string:
            self.asci = colored("""
                  
                                                               ███                  █████████   █████
                                                              ░░░                  ███░░░░░███ ░░███ 
 █████████████    ██████   ███████ █████ ████ █████████████   ████  ████████      ░███    ░███  ░███ 
░░███░░███░░███  ███░░███ ███░░███░░███ ░███ ░░███░░███░░███ ░░███ ░░███░░███     ░███████████  ░███ 
 ░███ ░███ ░███ ░███████ ░███ ░███ ░███ ░███  ░███ ░███ ░███  ░███  ░███ ░███     ░███░░░░░███  ░███ 
 ░███ ░███ ░███ ░███░░░  ░███ ░███ ░███ ░███  ░███ ░███ ░███  ░███  ░███ ░███     ░███    ░███  ░███ 
 █████░███ █████░░██████ ░░███████ ░░████████ █████░███ █████ █████ ████ █████ ██ █████   █████ █████
░░░░░ ░░░ ░░░░░  ░░░░░░   ░░░░░███  ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░ ░░ ░░░░░   ░░░░░ ░░░░░ 
                          ███ ░███                                                                   
                         ░░██████                                                                    
                          ░░░░░░                                                                     

                        ""","red")
            return self.asci
      
      def write_json(self,new_data= {}, filename='mchatlog.json'):
            with open(filename,'r+') as self.file:
        # First we load existing data into a dict.good
                  self.file_data = json.load(self.file)
        # Join new_data with file_data inside emp_details
                  self.file_data["history"].append(new_data)
        # Sets file's current position at offset.
                  self.file.seek(0)
        # convert back to json.
                  json.dump(self.file_data, self.file, indent = 4)

      def NLP(self,user_input=' ',history=[])-> string:
            self.user = user_input
            print("You:",self.user)
            
            self.complete = openai.ChatCompletion.create (model="gpt-3.5-turbo-0613" ,messages=history,max_tokens = 50 ,temperature = 1 ,top_p=0.5,frequency_penalty=0.5,presence_penalty=1)
            self.write_json({"role":"user", "content":self.user},filename='mchatlog.json')
            self.repo = self.complete.choices[0].message.content
            self.write_json({"role":"assistant","content":self.repo},filename='mchatlog.json')
            return self.repo
           
