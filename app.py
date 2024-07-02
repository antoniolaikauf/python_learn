from flask import Flask, render_template, request


app= Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html") # file index deve sempre stare dentro ad una cartella chiamata templates

