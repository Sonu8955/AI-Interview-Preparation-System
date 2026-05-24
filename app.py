from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = {

    "Python": [

        "What is Python?",

        "Explain list and tuple difference.",

        "What is OOP in Python?",

        "What is a dictionary?"
    ],

    "Java": [

        "What is JVM?",

        "Explain inheritance.",

        "What is polymorphism?",

        "Difference between abstract class and interface?"
    ],

    "DBMS": [

        "What is normalization?",

        "Difference between SQL and NoSQL?",

        "Explain primary key.",

        "What is indexing?"
    ],

    "AI/ML": [

        "What is Machine Learning?",

        "Difference between AI and ML?",

        "Explain CNN.",

        "What is overfitting?"
    ]
}

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():

    category = request.form['category']

    question = random.choice(questions[category])

    return render_template(
        'question.html',
        question=question,
        category=category
    )

@app.route('/submit', methods=['POST'])
def submit():

    answer = request.form['answer']

    if len(answer) > 100:
        score = 9
        feedback = "Excellent answer! Very detailed and professional."

    elif len(answer) > 60:
        score = 7
        feedback = "Good answer! Try adding more confidence and examples."

    elif len(answer) > 30:
        score = 5
        feedback = "Average answer. Add more details."

    else:
        score = 3
        feedback = "Answer is too short. Explain properly."

    return render_template(
        'result.html',
        answer=answer,
        score=score,
        feedback=feedback
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)