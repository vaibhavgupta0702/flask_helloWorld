from flask import Flask
import os

port = int(os.getenv("PORT"))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
