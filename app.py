from flask import Flask, render_template
import os
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("valmynd.html")+"""
    <h1>Hello user1</h1>
    """

@app.route("/sida2/")
def sida2():
    return render_template("default.html")+"""
    <h1>Hello user2</h1>
    """
@app.route("/sida3/")
def sida3():
    return render_template("valmynd.html")+"""
    <h1>Hello user3</h1>
    """
@app.route("/sida/<kt>/")
def page(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)
    
    return render_template("kt_summa.html", kt=kt, summa = summa)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404
if __name__ == "__main__":
    app.run(debug=True)
