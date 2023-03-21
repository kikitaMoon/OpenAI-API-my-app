import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# for private key, it's better to set it in System Env settings.
openai.api_key = os.getenv("OPENAI_API_KEY")


# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]     # the code that sends the actual API request
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)

# the function that generates the prompt that we were using above.
# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.
#
#         Animal: Cat
#         Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
#         Animal: Dog
#         Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
#         Animal: {}
#         Names:""".format(
#         animal.capitalize()
#     )


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        place = request.form["place"]  # the code that sends the actual API request
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(place),
            temperature=0.6,
            max_tokens=50
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(place):
    return """Suggest the latitude and longitude in JSON format of the given place.
    
    Place: Beijing
    latlon: "city": "Beijing","latitude": 39.9042,"longitude": 116.4074
    Place: Shanghai
    latlon: "city": "Shanghai","latitude": 31.2304,"longitude": 121.4737
    Place: {}
    Latlon:""".format(place.capitalize())
