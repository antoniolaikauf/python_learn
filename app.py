from flask import Flask, render_template, request


app= Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html") # file index deve sempre stare dentro ad una cartella chiamata templates

@app.route('/greet')
def greet():
    # name è la variabile che si ottiene dal form 
    return render_template("greet.html", name=request.args.get('name','parola di default')) 

