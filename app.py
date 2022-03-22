#!/usr/bin/env python
import paho.mqtt.client as mqtt
from time import sleep
from flask import redirect, Flask

def clearColors(client):
    for color in ["Red", "Green", "Yellow"]:
        client.publish(r"esp/test", payload="#%s_OFF"%(color))

def setColor(client, color):
    client.publish(r"esp/test", payload="#%s_ON"%(color))

app = Flask(__name__)
mqHost = "192.168.40.114"
client = mqtt.Client()

@app.route("/")
def index():
    return redirect("/Clear")

@app.route("/<color>")
def colors(color):
    if not client.is_connected:
        client.connect(mqHost)
    clearColors(client)
    if color in ["Red", "Green", "Yellow"]:
        setColor(client, color)
    return """
    <body>
        <a href="/Red">Red</a>
        <a href="/Yellow">Yellow</a>
        <a href="/Green">Green</a>
        <a href="/Clear">clear</a>
    </body>
    """
