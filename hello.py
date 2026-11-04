import os # importing OS to access the local computer
from anthropic import Anthropic #importing Anthropic from anthropic to be honest not sure what small a and big A difference is 
from dotenv import load_dotenv #using the dotenv library to load our key from the .env file
from dotenv import dotenv_values


load_dotenv()
client = Anthropic()

message = client.messages.create(
    max_tokens = 100,
    messages=[
        {
            "role":"user",
            "content":"Hello, Claude",
        }
    ],
    model = "claude-haiku-5-5",
)

for block in message.content:
    if block.type=="text":
        print(block.text)