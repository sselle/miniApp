__author__ = 'sven'
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home_method():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return 'home on ' + host_name + ' with IP ' + host_ip
    
@app.route('/1')
def p_1():
    return 'page 1'

@app.route('/2')
def p_2():
    return 'page 2'

if __name__ == '__main__':
    app.run(host = '0.0.0.0')