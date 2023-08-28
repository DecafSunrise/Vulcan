from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mood_stats')
def mood_stats():
    return "I'd be printing mood stats"

if __name__ == '__main__':
    app.run()