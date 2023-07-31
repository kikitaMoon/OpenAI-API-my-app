# -*- coding: utf-8 -*-

import os
from pyexpat.errors import messages

import openai
from flask import Flask, redirect, render_template, request, url_for, Markup

app = Flask(__name__)

# for private key, it's better to set it in System Env settings.
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        your_input = request.form["yourInput"]  # the code that sends the actual API request

        ### Using model GPT 3.5
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "Act as an assistant to search name(s) of documentary films , made by BBC or National Geography, based on the given strings by the user.  The input strings are most likely the characters or content that ever shows in the film.   RULES:  1.Only key answer after user input, no other words. 2.The output names are in Chinese and English, with the source name,a sentence of description in Chinese, following the html format as EXAMPLE. EXAMPLE: [user]giraffe; [result]<ol><li><strong>《长颈鹿的世界/The World of Giraffes》- [BBC]</strong> <p>这部纪录片深入探索了长颈鹿作为动物界的独特存在，展示了它们在非洲草原上生存与繁衍的壮丽场面。</p></li><li>[MORE ITEMS]</li></ol>"},
                {"role": "user", "content": your_input}
            ],
            temperature=0.6,
            max_tokens=1000
        )
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index.html", result=Markup(result))
