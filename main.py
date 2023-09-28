# person = {
#     'name': 'nsr',
#     'shirt': 'black',
#     'laptop': 'Apple',
#     'assets': 100,
#     'debt': 50,
#     'networth': lambda: person['assets'] - person['debt']
# }
#
# person['assets']=1000
# print(list(person.values()))


# fruits = ['apple', 'orange', 'toto']
# for i, fruit in enumerate(fruits):
#     print(f'fruit {fruit}')
#
# for i in range(10):
#     fruits.append('apple')
# print(fruits)

from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)

# Configure Flask-Session to use filesystem-based sessions
app.config['SESSION_TYPE'] = 'filesystem'  # used to save counter when restarting the program (same like local
# storage in js)
Session(app)


@app.route('/')
def home():
    # Use session to store and retrieve the counter value
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('counter_page.html', counter=session['counter'])


@app.route('/increment', methods=['POST'])
def increment():
    if request.method == 'POST':
        # Increment the counter in the session
        session['counter'] += 1
    return render_template('counter_page.html', counter=session['counter'])


@app.route('/decrement', methods=['POST'])
def decrement():
    if session['counter'] > 0:
        if request.method == 'POST':
            # Decrement the counter in the session
            session['counter'] -= 1
    return render_template('counter_page.html', counter=session['counter'])


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

# @app.route('/')
# def home_page():
#     return render_template('info.html')


# @app.route('/saveData', methods=['POST'])
# def save_data():
#     global user
#     if request.method == 'POST':
#         new_user = {
#             'name': request.form.get('name'),
#             'age': request.form.get('age'),
#             'salary': request.form.get('salary')
#         }
#         user.append(new_user)
#
#     return render_template('info.html', users=user)
#
#
# @app.route('/render', methods=['POST'])
# def render():
#     user_input = ''
#     if request.method == 'POST':
#         user_input = request.form.get('name')
#     return render_template('index.html', user_input=user_input)


# @app.route('/increment', methods=['POST'])
# def increment():
#     global counter
#     if request.method == 'POST':
#         counter += 1
#     return render_template('hello.html', counter=counter)

#
# @app.route('/decrement', methods=['POST'])
# def decrement():
#     global counter
#     if request.method == 'POST':
#         if counter > 0:
#             counter -= 1
#     return render_template('hello.html', counter=counter)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
