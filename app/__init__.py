#-*- coding: utf-8 -*-
import imp, sys
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as e: pass

from flask import Flask
import config

app = Flask('phobook')
app.config.from_object('config')

# Handling OPTION Method request for cross site
from flask_cors import CORS, cross_origin
CORS(app)

from app.db import init_db, db_session
init_db()

from app.login import *

@app.teardown_appcontext
def shutdown_session(exception):
	db_session.remove()

from app.controller import routes
routes(app)