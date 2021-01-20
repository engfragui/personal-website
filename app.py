from flask import Flask, render_template
from actorinfo import full_name, bio, reel, twitter, instagram, facebook, imdb

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', full_name=full_name, bio=bio, reel=reel, twitter=twitter, instagram=instagram, facebook=facebook, imdb=imdb)


if __name__ == '__main__':
    app.run(debug=True)
