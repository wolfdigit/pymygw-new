from pymygw import Database

class MyPublisher(object):
    def __init__(self):
        #self._log = getLogger('pymygw')
        self.db = Database.Database()

    def setSendCallback(self, callback):
        self.sendFunc = callback

    def publish(self, msg, info = None):
        print "msg:"
        print msg
        print "info:"
        print info
        # parse for changed sensorId
        '''
        self._data = tools.checkKeys(msg, ('nodeid', 'childid', 'payload'))
        if self._data and self.connected:
            self._log.debug('Try to publish values to the MQTT Broker on {0}: {1}'.format(config.MQTTBroker,
                                                                                           msg))
            topic = "/" + config.MQTTTopic
            try:
                topic = topic.replace(
                    '%nodeid', self._data['nodeid']).replace(
                    '%childid', self._data['childid']).replace(
                    '%sensorid', self._data['childid'])
               
                if not (info is None):
                    topic=topic.replace(
                        '%childdescription', info.description).replace(
                        '%sensordescription', info.description)
           
                self.__publish(topic, self._data['payload'])
            except Exception, e:
             self._log.error('MQTT Publish failed: Failed to create topic');
        '''
        None

    def handle(self, nodeId, sensorId):
        # user code here. 
        None

    def get(self, nodeId, sensorId):
        # get from DB.
        None

    # nodeid, childid, messagetype=command, subtype=S_?|V_?|I_?, payload
    '''
    _cmd = {'nodeid': 255,
            'childid': 255,
            'messagetype': config.MySensorMessageType['SET']['id'],
            'subtype': self.id('I_ID_RESPONSE'),
            'payload': newID}
    '''
    def set(self, nodeId, sensorId, valueType, value):
        # call self.sendFunc(...). 
        cmd = {'nodeid': nodeId,
               'childid': sensorId,
               'messagetype': config.MySensorMessageType['SET']['id'],
               'subtype': valueType,
               'payload': value}
        self.sendFunc(cmd)
        # set DB
        None
        
    def disconnect(self):
        # nothing
        None
