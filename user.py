import slixmpp

class User(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.add_event_handler('session_start', self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()


