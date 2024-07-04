from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def snake_game():
    os.system('python snake_game.py')
    return "Snake Game is running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
