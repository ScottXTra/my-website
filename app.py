from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def hello():
  return "Hello World!"


@app.route("/home")
def home():
  return render_template("homepage.html")





if __name__ == "__main__":
  app.run()