from flask import render_template

services = (
    {
    "name": "items",
    "url": "/services/items",
    "metrics": "/services/items/metrics"
    },
    {
    "name": "items",
    "url": "/services/items",
    "metrics": "/services/items/metrics"
    },
)

def service_landing():
    '''services route'''
    return render_template("services.html", services=services)


