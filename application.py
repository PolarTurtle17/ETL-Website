import requests
import json
from flask import Flask, render_template, Response, request
import random

app = Flask(__name__)
application = app

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/", methods=['POST'])
def submit_button():
    print("Button Pressed")
    anime = request.form ["fname"]
    fixed_anime = ''
    for word in anime.split():
        fixed_anime += word
        fixed_anime += "%20"
    anime = fixed_anime[:-3]
    character = request.form ["lname"]
    fixed_character = ''
    for word in character.split():
        fixed_character += word
        fixed_character += "%20"
    character = fixed_character[:-3]
    extra = requests.get('https://animechan.vercel.app/api/available/anime')
    extra = json.loads(extra.text)
    API = 'https://animechan.vercel.app/api/quotes'
    if anime != "":
        API = API + '/anime?title=' + anime
        print(API)
        test = requests.get(API)

    elif character != "":
        API = API + '/character?name=' + character
        print(API)
        test = requests.get(API)

    else:
        test = requests.get('https://animechan.vercel.app/api/random')
        test = json.loads(test.text)
        print(test)
        return render_template("index1.html", quote=test["anime"] + " u: " + test["character"] + " : " + test["quote"])

    try:
        test = random.choice(json.loads(test.text))
        return render_template("index1.html", quote = test["anime"] + " : " + test["character"] + " : " + test["quote"])
    except KeyError:
        return render_template("index1.html", animes = extra, quote = "Oops! Sorry we don't have a quote for what your asking, Try another...")


if __name__ == "__main__":
    app.run(debug=True)

