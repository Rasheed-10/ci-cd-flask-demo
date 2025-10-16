
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Hello, DevOps World! Your CI/CD pipeline works!"

# Run the app locally
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
