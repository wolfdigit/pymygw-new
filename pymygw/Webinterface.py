from flask import Flask, render_template, g, request
from datetime import datetime

import config
import Database
import os

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
webSendCallback = None


@app.before_request
def before_request():
    g.db = Database.Database()


@app.template_filter('timestamp2date')
def timestamp2date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    return render_template('index.html',
                           data=g.db.get())


@app.route('/detail/<node>', defaults={'sensor': None})
@app.route('/detail/<node>/<sensor>')
def detail(node, sensor):
    if sensor:
        data = (g.db.get(node=node, sensor=sensor),)
    else:
        data = g.db.get(node=node, sensor=sensor)

    return render_template('nodedetail.html',
                           data=data,
                           config=config)

@app.route('/act/<node>/<sensor>', methods=['POST'])
def act(node, sensor):
    global webSendCallback
    val = request.form['val']
    if webSendCallback is not None:
        typeStr = g.db.get(node=node, sensor=sensor).sensor_type
        #sensorType = config.MySensorPresentation['S_'+typeStr]['id']
        sensorType = config.MySensorSetReq['V_'+typeStr]['id']
        _cmd = {'nodeid': node,
                'childid': sensor,
                'messagetype': config.MySensorMessageType['SET']['id'],
                'subtype': sensorType,
                'payload': val}
        webSendCallback(_cmd)
        return "0|OK"
    else:
        return "-1|empty callback"

@app.route('/upload', methods=['POST'])
def upload():
    code = request.form['code']
    filename = os.path.dirname(os.path.realpath(__file__)) + "/../userLogic.py"
    print filename
    with open(filename, 'w') as fp:
        fp.write(code)
    return "0|OK"