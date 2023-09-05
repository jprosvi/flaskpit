from flask import Flask
import socket

myhost = socket.gethostname()
ip_address = socket.gethostbyname(myhost)

app = Flask('__name__')

@app.route('/')
def system_info():
    return f"Hostname: {myhost}\nIP: {ip_address}\n"


if __name__== '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
