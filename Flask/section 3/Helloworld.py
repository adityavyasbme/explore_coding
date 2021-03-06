# Import the Flask package
from flask import Flask
# Initialize Flask
app = Flask(__name__)
# Define the index route
@app.route("/")
def index():
    return "HeY What's up? "
# Run Flask if the __name__ variable is equal to __main__
if __name__ == "__main__":
    app.run('localhost',debug=True)