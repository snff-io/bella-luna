from flask import Flask, render_template, url_for
import services

app = Flask(__name__)

@app.route("/")
def index():
    '''default route'''
    return render_template("index.html", title="bella-luna")

@app.route("/services")
def service_landing():
    '''services route'''
    return url_for(services.service_landing())
