from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define your questions here
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Rome', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is 2 + 2?',
        'options': ['3', '4', '5'],
        'answer': '4'
    },
# Add more questions here
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))


import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname) 

if __name__ == "__main__":
    app.run(host=IP, port=7000)
