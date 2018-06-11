from pymygw import Database
import userLogic

class MyPublisher(object):
    def __init__(self):
        #self._log = getLogger('pymygw')
        self.db = Database.Database()

    def setSendCallback(self, callback):
        self.sendFunc = callback

    def publish(self, msg, info = None):
        reload(userLogic)
        allSensors = self.db.get()
        data = {}
        for sensor in allSensors:
            nid = sensor.node_id
            sid = sensor.sensor_id
            val = sensor.last_value
            data[(nid,sid)] = val
        print data

        nid = info.node_id
        sid = info.sensor_id
        val = info.last_value
        try:
            actions = userLogic.onChange(nid, sid, val, data)
            for line in actions.splitlines():
                tok = line.split('\t')
                self.set(tok[0], tok[1], tok[2])
        except:
            None

    def handle(self, nodeId, sensorId):
        # user code here. 
        None

    # nodeid, childid, messagetype=command, subtype=S_?|V_?|I_?, payload
    '''
    _cmd = {'nodeid': 255,
            'childid': 255,
            'messagetype': config.MySensorMessageType['SET']['id'],
            'subtype': self.id('I_ID_RESPONSE'),
            'payload': newID}
    '''
    def set(self, nodeId, sensorId, value):
        # call self.sendFunc(...). 
        cmd = {'nodeid': nodeId,
               'childid': sensorId,
               'messagetype': config.MySensorMessageType['SET']['id'],
               'subtype': self.db.get(nodeId,sensorId).sensor_type,
               'payload': value}
        self.sendFunc(cmd)
        # TODO: set DB
        None
        
    def disconnect(self):
        # nothing
        None
