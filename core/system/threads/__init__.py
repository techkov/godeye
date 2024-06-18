from time import sleep
from threading import Thread

from core.shark import Filter, Shark
from core.system.logging import logger


class Background:
    def __init__(self, interface) -> None:
        self.tasks = {
            'ip': Filter(interface, 'ip'),
            'tls': Filter(interface, 'tls.handshake.type == 1 and tcp'),
            'dns': Filter(interface, 'dns'),
            'http': Filter(interface, 'http.request.method and tcp'),
            'tcp': Shark(interface, 'tcp'),
            'udp': Shark(interface, 'udp')
        }

        self.running = True

    def run_thread(self, name, thread):
        while self.running:
            data = thread.live_packets()

            if data:
                logger.info(f'{name} Filter: {data}')

            sleep(5)


    def start(self):
        for name, task in self.tasks.items():
            thread = Thread(
                target=self.run_thread,
                args=(name, task)
            )

            thread.daemon = True

            thread.start()


    def stop(self):
        self.running = False