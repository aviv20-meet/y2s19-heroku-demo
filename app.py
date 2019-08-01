from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/info')
def info_route():
	print(query_all())
	return render_template('info.html', idiots = query_all())

@app.route('/signup', methods= ['GET','POST'])
def signup_route():
	if(request.method == 'GET'):
		return render_template('signup.html')
	else:
		FName = request.form['FName']
		LName = request.form['LName']
		gender = request.form['gender']
		print("+++++++++++ " + gender)
		stupid_level = request.form['stoobid']
		add_idiot(FName,LName,gender,stupid_level)
		return redirect(url_for('info_route'))


if __name__ == '__main__':
	app.run(debug=True)