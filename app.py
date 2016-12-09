from flask import *
import config
from warmup import Warmup
from spotify_routes import spotify_search

app = Flask(__name__)
app.register_blueprint(Warmup)
app.register_blueprint(spotify_search)

if __name__ == '__main__':
	app.run()