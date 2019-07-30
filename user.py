import slixmpp
from threading import Thread
from slixmpp.exceptions import IqError, IqTimeout
from menu import OptionsMenu, get_option, menu
from blessed import Terminal

t = Terminal()


def msg_group(msg):
    print(t.color(40)(msg))


class User(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.menu = Thread(target=OptionsMenu, args=(
            menu,
            self.send_individual_message,
            self.get_roster_print,
            self.delete_account,
            self.send_file,
        ))

        # start event
        self.add_event_handler('session_start', self.start)
        # register event
        self.add_event_handler('register', self.register)
        # message event
        self.add_event_handler('message', self.message)
        # group message event
        self.add_event_handler("groupchat_message", self.muc_message)

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

    async def delete_account(self):
        resp = self.Iq()
        resp['type'] = 'set'
        resp['from'] = self.boundjid.jid
        resp['register'] = ' '
        resp['register']['remove'] = ' '

        try:
            await resp.send()
            print('')
        except IqError:
            print("Error al eliminar cuenta")
        except IqTimeout:
            print("timeout")
            self.disconnect()

    def message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            # Do something
            print(msg['body'])
        else:
            # Error
            print('Error')
            print(msg['body'])

    def muc_message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            # Do something
            msg_group(msg['body'])
        else:
            # Error
            print('Error')
            print(msg['body'])

    def send_individual_message(self):
        mto = get_option('Para: ')
        mbody = get_option('Contenido: ')
        self.send_message(mto=mto, mbody=mbody)

    # TODO: enter to room
    def send_group_message(self):
        pass

    # TODO: get all users connected
    def get_my_roster(self):
        print(self.get_roster())

    def get_roster_print(self):
        print(self.roster)

    def get_one_user(self):
        jid = get_option('jid: ')
        print(self.roster[jid])

    def add_to_roster(self):
        jid = get_option('jid: ')
        self.update_roster(jid=jid)

    def exit(self):
        self.disconnect()

    async def send_file(self):
        file_name = get_option('Dirección del archivo: ')
        receiver = get_option('Para: ')
        file = open(file_name, 'rb')

        # open stream
        proxy = await self['xep_0065'].handshake(receiver)

        try:

            # Send file
            while True:
                data = file.read(1048576)
                if not data:
                    break
                await proxy.write(data)

            proxy.transport.write_eof()
        except (IqTimeout, IqError):
            print(t.color(9)('Error en transferencia'))
        else:
            print(t.color()('Transferencia completada'))
        finally:
            file.close()





