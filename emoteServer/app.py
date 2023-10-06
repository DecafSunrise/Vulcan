from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Directory to store user inputs
input_dir = os.path.join(os.getcwd(), "data")

if not os.path.exists(input_dir):
    os.makedirs(input_dir)

# Common sidebar data
sidebar_data = [
    {"url": "/", "text": "Overview"},
    {"url": "/system", "text": "System Prompt"},
    {"url": "/personality", "text": "Personality Prompt"},
    {"url": "/api/get_inputs", "text": "Check files"}
]

@app.route("/")
def home():
    return render_template("overview.html", sidebar_data=sidebar_data)

@app.route("/system")
def page1():
    return render_template("system.html", sidebar_data=sidebar_data)

@app.route("/personality")
def page2():
    return render_template("personality.html", sidebar_data=sidebar_data)

@app.route("/save_input", methods=["POST"])
def save_input():
    data = request.json
    if "filename" in data and "text" in data:
        filename = data["filename"]
        text = data["text"]
        filepath = os.path.join(input_dir, filename)

        with open(filepath, "w") as file:
            file.write(text)
        return jsonify({"message": "Input saved successfully!"})
    else:
        return jsonify({"error": "Invalid request"}), 400

@app.route("/api/get_inputs")
def get_inputs():
    input_files = os.listdir(input_dir)
    input_data = {}

    for filename in input_files:
        filepath = os.path.join(input_dir, filename)
        with open(filepath, "r") as file:
            input_data[filename] = file.read()

    return jsonify(input_data)

if __name__ == "__main__":
    app.run(debug=True)
