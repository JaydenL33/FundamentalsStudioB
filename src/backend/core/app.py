from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
  app.run(host="134.122.104.123")