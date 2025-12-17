from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Welcome to Flask Server</h1></body></html>"

@server.get('/about')
def aboutpage():
    return "<html><body><h1>About Flask Server</h1></body></html>"

server.run()
