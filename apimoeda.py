from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

#Build functions
@app.route("/moedas")
def get_currency():
    # Opening JSON file
    f = open('moedas.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()
    return data

@app.route("/conversao")
def get_type_currency():
        # Opening JSON file
    f = open('conversao.json')
    
    # returns JSON object as
    # a dictionary
    data_conversation = json.load(f)
    f.close()
    return data_conversation

@app.route("/Clara")
def amorzinho():
    return "<h1> Te amo, Clara 💖 </h1>"


if __name__ == "__main__":
    app.run(debug=True)