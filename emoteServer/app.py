import os
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

# Configuration file path
config_file_path = 'config.txt'

# Function to read the current configuration
def read_config():
    with open(config_file_path, 'r') as f:
        return f.read()

# Function to update the configuration
def update_config(new_text):
    with open(config_file_path, 'w') as f:
        f.write(new_text)

@app.route('/')
def index():
    current_config = read_config()
    return render_template('index.html', current_config=current_config)

@app.route('/update_config', methods=['POST'])
def update_config_route():
    new_text = request.form.get('new_config_text')
    update_config(new_text)
    return redirect('/')

@app.route('/api/config')
def get_config_api():
    current_config = read_config()
    return jsonify({'config': current_config})

if __name__ == '__main__':
    app.run(debug=True)
