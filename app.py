from flask import Flask, render_template
import spotify_routes

app = Flask(__name__)

@app.route("/hello-world")
def home_route():
	return "Hello world!"

if __name__ == '__main__':
	app.run()