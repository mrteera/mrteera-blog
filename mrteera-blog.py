from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! test3'


if __name__ == '__main__':
    app.run(host='vm.mrteera.com', port=5555)
