import os
import maya.standalone
import maya.cmds as cmds
from mayaScale import mayaScale
from bottle import Bottle, run, template, post, request

app = Bottle()

@app.route('/')
def index():
    return template('simax.html')

@app.post('/login/<height>')
def save_new_cube(height=1):
    scaler = mayaScale(float(height))
    forward_message = "Current Height is: " + str(scaler.scaledHeight)
    return forward_message

run(app, host='localhost', port=8080)
