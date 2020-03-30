from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hello.html')

if __name__ == "__main__":
  app.run(host="134.122.104.123")