from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Welcome to Flask Server</h1></body></html>"

@server.get('/about')
def aboutpage():
    return "<html><body><h1>About Flask Server</h1></body></html>"

@server.post('/marks/<int:mark>')
def show_name(mark):
    print(f"marks = {mark}")
    return f"{mark} recieved"

server.run(host='0.0.0.0',port = 4000,debug = True)
