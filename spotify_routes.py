from flask import *
import config

spotify_search = Blueprint('spotify_search', __name__)

@spotify_search.route("/spotify")
def spotify_search_route():
	return "Hello World!"