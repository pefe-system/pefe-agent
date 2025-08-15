from ..config import *
from pefe_common.messaging.json import JSONClient

class Consumer:
    def __init__(self, identity):
        self._host = config['loader']['host']
        self._port = config['loader']['port']
        self._client = JSONClient(self._host, self._port)
        self._identity = identity
        print(f"Agent [{identity}] registered at loader server {self._host}:{self._port}")
    
    def handle_content(self, content):
        raise NotImplementedError

    def run(self):
        self._client.send_json({ "identity": self._identity })
        try:
            while True:
                msg = self._client.recv_json()
                if msg['status'] == 'end':
                    break
                if msg['status'] == 'new_content':
                    try:
                        ack = self.handle_content(msg['content'])
                    except Exception as e:
                        self._client.send_json({ "status": "error", "message": str(e) })
                    else:
                        self._client.send_json({ "status": "done", "message": ack })
        except StopIteration:
            pass

        print()
        print("Stopping... ", end="", flush=True)
        self._client.close()
        print("Done.")
