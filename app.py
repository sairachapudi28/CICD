from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is Sai Rachapudi"

if __name__ == '__main__':
    # Use Gunicorn as the WSGI server
    app.run(host='10.142.0.5', port ='3000' )

