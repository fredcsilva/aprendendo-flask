from flask import Flask

app = Flask(__name__)

from app.controllers import index_controller