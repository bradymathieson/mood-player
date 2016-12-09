from flask import *

Warmup = Blueprint('warmup', __name__)

@Warmup.route("/hello-world")
def home_route():
	return "Hello world!"

@Warmup.route("/hello/<name>")
def home_name_route(name):
	return render_template('name_test.html', name=name)