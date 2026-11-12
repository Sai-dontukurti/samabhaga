from splits import settle_up, expenses, calculate_balances

#import os # importing OS to access the local computer
from anthropic import Anthropic #importing Anthropic from anthropic to be honest not sure what small a and big A difference is 
from dotenv import load_dotenv #using the dotenv library to load our key from the .env file
#from dotenv import dotenv_values


load_dotenv()
client = Anthropic()

payments = settle_up(calculate_balances(expenses))
message = client.messages.create(
    max_tokens = 1000,
    system ="You are Samabhaga, friendly assistant. Turn a list of payments into a message for the group. Write one line per payment, under 5 lines. only use the names and amounts given ",
    messages=[
        {
            "role":"user",
            
            "content":str(payments),
        }
    ],
    model = "claude-haiku-5-5",
)
#print(message)

for block in message.content:
    if block.type=="text":
        print(block.text)

