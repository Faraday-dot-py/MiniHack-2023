
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'



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






if __name__ == '__main__':
    app.run(debug=True, port=5000)