""" A flask app. Line 10 is bad, oh well."""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, 2015 hackNY fellows!"

    if __name__ == "__main__":
            app.run(host='0.0.0.0', port=80)
