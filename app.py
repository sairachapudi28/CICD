from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is Rishav"

if __name__ == '__main__':
    # Use Gunicorn as the WSGI server
    app.run(host='0.0.0.0', port=8000)

