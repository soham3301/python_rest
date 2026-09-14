from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

my_email = "admin@email.com"
my_pass = "12345678"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "heyitisme"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    login_form = LoginForm()
    if request.method == "GET":
        return render_template('login.html', form=login_form)
    else:
        if login_form.validate_on_submit():
            the_email = login_form.email.data
            the_password = login_form.password.data
            if the_email == my_email and the_password == my_pass:
                return render_template('success.html')
            else:
                return render_template('denied.html')
        else:
            render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
