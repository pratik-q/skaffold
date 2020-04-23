import time
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("REQ received from client")
    return "Hello World!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


#while(True):
    #print("hello world")
#    logging.debug("Hello-2")

#    time.sleep(5)