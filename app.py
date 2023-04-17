from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect('database.db')
connect.execute(
	'CREATE TABLE IF NOT EXISTS USERS (first_name TEXT, \
	last_email TEXT, polish_id_number TEXT, date_of_birth TEXT)')


@app.route("/form/", methods=("GET", "POST"))
def form():
	if request.method == 'POST':
		first_name = request.form['firstName']
		last_email = request.form['lastName']
		polish_id_number = request.form['pesel']
		date_of_birth = request.form['birthDate']
		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO USERS \
			(first_name,last_email,polish_id_number,date_of_birth) VALUES (?,?,?,?)",
						(first_name, last_email, polish_id_number, date_of_birth))
			users.commit()
		return redirect("/users")
	elif request.method == 'GET':
	    return render_template('form.html')

@app.route('/users')
def users():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM USERS')

	data = cursor.fetchall()
	return render_template("users.html", data=data)


if __name__ == '__main__':
	app.run(debug=False)
