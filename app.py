from flask import Flask
from flask import render_template
from flask import request

import mysql.connector

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


db = mysql.connector.connect(user='pi', password='held',
                              host='127.0.0.1',
                              database='my_website')
curs = db.cursor()


@app.route("/")
def hello():
  return "Hello World!"


@app.route("/logCalc")
def logCalc():
  num1 = request.args.get('num1')
  num2 = request.args.get('num2')
  result = request.args.get('result')
  sql = "insert into calculator_results (number1, number2, result) values (%s,%s,%s);"
  val = (num1, num2, result)
  print(result)
  curs.execute(sql,val)
  db.commit()
  return "Saved"


@app.route("/home")
def home():
  return render_template("homepage.html")





if __name__ == "__main__":
  app.run()