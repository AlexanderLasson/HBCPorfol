from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # root directory
def my_home():
    return render_template("Home.html")



@app.route("/<string:page_name>")   
def html_page(page_name):
    return render_template(page_name)
