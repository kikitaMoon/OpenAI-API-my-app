import os
from pyexpat.errors import messages

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# for private key, it's better to set it in System Env settings.
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        place = request.form["place"]  # the code that sends the actual API request

        ### Using model GPT 3.5
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant to provide the latitude and longitude in JSON format of the given place."},
                {"role": "user", "content": "Beijing"},
                {"role": "assistant", "content": " 'city':'Beijing', 'latitude':39.9042, 'longitude':116.4074"},
                {"role": "user", "content": place}
            ],
            temperature=0.6,
            max_tokens=50
        )
        return redirect(url_for("index", result=response.choices[0]))

    result = request.args.get("result")
    return render_template("index.html", result=result)






