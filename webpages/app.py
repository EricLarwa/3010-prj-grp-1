
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


@app.route('/')

def index():
	try:
		conn = psycopg2.connect(
		host="localhost",
		port="5432",
		database="tables",
		user="webuser1",
		password="student")

		cursor = conn.cursor()

		cursor.execute("SELECT * FROM faculty;")
		table_data = cursor.fetchall()
	
		column_names = [desc[0] for desc in cursor.description]
		cursor.close()
		conn.close()

		return render_template('index.html', data=table_data, column_names=column_names)


	except Exception as e:
		return f"Error: {str(e)}"


if __name__ == '__main__':
	app.run(debug=True)
