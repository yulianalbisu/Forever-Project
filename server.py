"""Server for forever app."""

from flask import Flask

app = Flask(__name__)

#comming soon, functions and routes!

@app.route('/register, methods=['POST'])
def register_user():
    email = request.form['email']
    password= request.form['password']

    user = get_user_by_email(email)
    if user:
        return 'This user already exist.'
    else:
        create_user(email, password)

        return redirect('/login-form')






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)