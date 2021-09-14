from flask import Flask

import logging
import logging.config
import requests
app = Flask(__name__)
from format import CustomFormatter
from flask.logging import default_handler

app.logger.removeHandler(default_handler)

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
# create logger with 'spam_application'
# logger = logging.getLogger("app")
# logger.setLevel(logging.DEBUG)

# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# ch.setFormatter(CustomFormatter())

#logger.addHandler(ch)

@app.route('/hello/')
def hello_world():
    response = "hello world"
    app.logger.warning(response)
    app.logger.info("testing...")
    return response
    

@app.route('/india_covid/', methods=['GET','POST'])
def no_case():
    r = requests.get('https://covid19indiaapi.herokuapp.com/v1/overall')
    return r.json()
# app.logger.addHandler(ch)
app.logger.addHandler(logging.getLogger(__name__))
app.run()
