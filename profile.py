import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    
    return render_template("index.html")


@app.route('/api/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    name = request.json['name']
    age = request.json['age']
    occupation = request.json['occupation']
    
    return jsonify({'name': name, 
                    'age': age,
                    'occupation': occupation,
                    })





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
