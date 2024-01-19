from flask import Flask, request, render_template #Flask is a micro web app framework written in Python.
import openai

app = Flask(__name__)

openai.api_key = ''

@app.route('/', methods = ['GET']) #Get request to openai API
def index():
    return render_template('index.html')

@app.route('/prompt', methods = ['POST']) #Post request to openai API
def prompt():
    data = request.get_json()
    input_text = data['text'] #Gets the input text, saves it to 'input_text' variable, so that it can be sent to openai
    
    response = openai.ChatCompletion.create(
         model = 'gpt-3.5-turbo',
         messages = [{"role": "user", "content": input_text}]
    ) #In the variable 'response', select your gpt model, and send your message with the role of user, and your content being 'input_text' form earlier
    
    generated_text = response.choices[0].message.content
    
    return generated_text

if __name__ == '__main__':
    app.run()
