# flask logic
from flask import  request, Flask, render_template


from google import genai

import os

from dotenv import load_dotenv

load_dotenv("api.env") #loads the key-value pairs in the .env file into the or this file 

API_KEY = os.getenv("key")

app = Flask(__name__)

@app.route("/")
def welcoming():

    return render_template("index.html", text = "you have'nt entered anything")

@app.route("/display", methods = ["POST"])
def display():

    try:
        user_input = request.form["user_name"] #returns an immutable dictionary

        client = genai.Client(api_key = API_KEY)
        
        response = client.models.generate_content(
            model= "gemini-3-flash-preview", contents=user_input 
        )

        return render_template("index.html", text = response.text, user_input = user_input)
    

    except:
        return "please Wait for a few moments before returning to the page. "
    
