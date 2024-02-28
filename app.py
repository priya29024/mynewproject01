from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz data
quiz_data = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct_answer': 'Paris',
    },
    # Add more questions here
]

@app.route('/')
def home():
    return render_template('index.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in quiz_data:
        user_answer = request.form.get(f"q_{quiz_data.index(q)}")
        if user_answer == q['correct_answer']:
            score += 1
    return render_template('result.html', score=score)

if __name__ == '_main_':
    app.run(debug=True)