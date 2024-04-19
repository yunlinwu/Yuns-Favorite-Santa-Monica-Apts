# Initialize Flask App
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__) # Create the Flask app instance

@app.route('/')  # Define the route for the root URL
def home():
    return render_template('index.html')  # Render index.html when the root URL is accessed

# Run the application
if __name__ == '__main__':
    app.run(debug=True)