import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
load_dotenv()
openai.api_key = os.getenv("OPENAI-KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

def get_current_time():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def exitConversation():
    print("Thank you for using the chatbot. Goodbye!")
    exit()

class MessageList:
    def __init__(self, messageLimit=100):
        self.messages = []
        self.last_message = ""
        self.messageLimit = messageLimit
    
    def add_message(self, message, user):
        if len(self.messages) >= self.messageLimit:
            self.messages.pop(0)
        self.messages.append({"role": user, "content": message})
        self.last_message = message

    def get_last_message(self):
        return self.last_message

    def get_messages(self):
        return self.messages

    def reset_message_list(self):
        self.messages = []
        self.last_message = ""


messageList = MessageList()

@app.route('/api/chat')
def chat():
    message = request.args['message']
    messageList.add_message(message, "user")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messageList.get_messages(),
    )
    messageList.add_message(response.choices[0].message.content, response.choices[0].message.role)
    return response.choices[0].message.content

@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/api/image')
def image():
    imagePrompt = request.args['imagePrompt']
    response = openai.Image.create(
        prompt=imagePrompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""
An api that lets you talk to the bot
- conversations are per ip address
- saved in a dictionary
- can be cleared by the user

A web page that calls the api
- a text box for the user to type in
- a button to send the message
- a button to clear the conversation
- the cool typing animation

"""
