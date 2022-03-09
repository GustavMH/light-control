#!/usr/bin/env python
import paho.mqtt.client as mqtt
from time import sleep
from flask import redirect, Flask

app = Flask(__name__)

def clearColors(client):
    for color in ["Red", "Green", "Yellow"]:
        client.publish(r"esp/test", payload="#%s_OFF"%(color))

def setColor(client, color):
    client.publish(r"esp/test", payload="#%s_ON"%(color))

def on_connect(client, userdata, flags, rc):
    print("Connected, result code:", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.40.114")

@app.route("/")
def index():
    return redirect("/Clear")

@app.route("/<color>")
def colors(color):
    clearColors(client)
    if color in ["Red", "Green", "Yellow"]:
        setColor(client, color)
    return """
    <body>
        <style>
    a {
      display:block;
      width:70px;
      color:rgba(0,0,0,0);
    }
        </style>
        <a href="/Red" style="background:red">Red</a>
        <a href="/Yellow" style="background:yellow">Yellow</a>
        <a href="/Green" style="background:green">Green</a>
        <a href="/Clear" style="background:black">clear</a>
    </body>
    """


