import slixmpp
from threading import Thread
from slixmpp.exceptions import IqError, IqTimeout
from menu import OptionsMenu, get_option, menu


class User(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.menu = Thread(target=OptionsMenu, args=(
            menu,
            self.send_individual_message,
            self.get_roster,
        ))

        # start event
        self.add_event_handler('session_start', self.start)
        # register event
        self.add_event_handler('register', self.register)
        # message event
        self.add_event_handler('message', self.message)

    def start(self, event):
        # <presence />
        self.send_presence()
        # <iq type=get>
        #   <query xmlns="data:iq:rooster" />
        # </iq>
        self.get_roster()
        # self.send_message(mto='a@alumchat.xyz', mbody='Hello')

    async def register(self, iq):
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            await resp.send()
            print("Account created")
        except IqError:
            print("Error al crear cuenta, probablemente ya existe")
        except IqTimeout:
            print("timeout")
            self.disconnect()

        self.menu.start()

    def message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            # Do something
            print(msg['body'])
        else:
            # Error
            print('Error')
            print(msg['body'])

    def send_individual_message(self):
        mto = get_option('Para: ')
        mbody = get_option('Contenido: ')
        self.send_message(mto=mto, mbody=mbody)

    def send_group_message(self):
        return

    def get_my_roster(self):
        print(self.get_roster())

    def add_to_roster(self):
        jid = get_option('Nombre del jid: ')
        self.update_roster(jid=jid)

    def exit(self):
        self.disconnect(wait=True)

    def





