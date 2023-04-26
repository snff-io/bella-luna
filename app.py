from flask import Flask, render_template, url_for,redirect
import services

app = Flask(__name__)

app.register_blueprint(services.services, url_prefix='/services')

@app.route("/")
def index():
    '''default route'''
    return redirect("/services")
