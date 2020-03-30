from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('hello.html')

if __name__ == "__main__":
  app.run(host="134.122.104.123")