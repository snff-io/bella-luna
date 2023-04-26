# Description: services blueprint
from flask import Blueprint, render_template


services = Blueprint('services', __name__, template_folder='templates')

service_view = {
    "title": "bella-luna",
    "services": [{
        "name": "items",
        "description": "services all item instances",
        "url": "/services/items",
        "metrics": "/metrics"
    },
        {
        "name": "interaction",
        "description": "servicses all item instances",
        "url": "/services/interaction",
        "metrics": "/metrics"
    }]

}


@services.route("/")
def index():
    '''services route'''
    return render_template("services.html", view=service_view)


@services.route("/metrics")
def metrics():
    '''services route'''
    metrics = {
        "uptime": "1",
        "cpu": "1",
        "memory": "1",
        "disk": "1"
    }

    return metrics
