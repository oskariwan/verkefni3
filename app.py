from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("valmynd.html")+"""
    <h1>Hello user1</h1>
    """

@app.route("/sida2/")
def sida2():
    return render_template("valmynd.html")+"""
    <h1>Hello user2</h1>
    """
@app.route("/sida3/")
def sida3():
    return render_template("valmynd.html")+"""
    <h1>Hello user3</h1>
    """

if __name__ == "__main__":
    app.run(debug=True)