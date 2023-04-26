from flask import Flask, render_template
import service

app = Flask(__name__)


def get_services():
    '''gets services from service directory'''
    return {
        "items.html", service.load_service("service", "items.py")
    }


@app.route("/")
def index():
    '''default route'''
    return render_template("index.html", title="bella-luna")


@app.route("/wc")
def world_computer():
    '''loads the wc service page'''
    return render_template("service_frame.html", loaded_services=get_services())


# maynard 11391
# joshua 20999 (0x5207)
