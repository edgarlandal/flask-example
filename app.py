from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/developer")
def get_developer():

    dev = {
        "first_name" : "Edgar",
        "last_name" : "Landa",
        "hobbies": "Play VideoGames and listen to music"
    }
    return json.dumps(dev)


app.run(debug=True)