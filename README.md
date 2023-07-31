# Wow Wow Magical Documentary Super Seeker

## Summary

> My own version of OpenAI API Quickstart - Python example app

This is an example of documentary film seeker that utilizes OpenAI's [GPT-3.5 Turbo model](https://platform.openai.com/docs/models/gpt-3-5) to assist users in finding documentary films made by **BBC** or **National Geographic** based on their input queries. The app acts as an intelligent assistant that can understand user requests and provides relevant responses in both Chinese and English. This is also for my little boy.

It is based on the App used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Look

![App Screenshot](/img/screenshot.jpg)
![App Screenshot](/img/screenshot2.jpg)

## Environments

- OS: Mac 12.6.8
- Python: 3.11.4 / Flask 
- AnaConda: 4.12

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone [this repo](https://github.com/kikitaMoon/OpenAI-Quickstart-Python) or [the original](https://github.com/openai/openai-quickstart-python).

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment with AnaConda, e.g. named `OpenAI`. Activate it:

   ```bash
   (base) mhoehn1:~ kikitamoon$ conda activate OpenAI
   (OpenAI) mhoehn1:~ kikitamoon$ conda env list
   # conda environments:
   #
   base                     /Users/kikitamoon/opt/anaconda3
   OpenAI                *  /Users/kikitamoon/opt/anaconda3/envs/OpenAI
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

   > Alternatively, set System Env Varaibles if you're using Windows.
   > to support the code: `openai.api_key = os.getenv("OPENAI_API_KEY")`

8.  Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).



See the workflow to understand the necessary steps and quickly get started:

![workflow image](/img/workflow.png)