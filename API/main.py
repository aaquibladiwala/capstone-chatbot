import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash
		
@app.route('/all')
def all():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM data")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
@app.route('/city/')
def city(loc):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM data WHERE city=%s",loc)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

if __name__ == "__main__":
    app.run()