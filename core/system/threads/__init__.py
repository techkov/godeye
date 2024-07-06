import asyncio
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

    async def run_task(self, name, task):
        while self.running:
            try:
                data = task.live_packets()

                if data:
                    logger.info(f'{name} Filter: {data}')

            except Exception as _ex:
                logger.error(f'Error in `{name}` task: {_ex}')

            await asyncio.sleep(5)


    async def main_loop(self):
        tasks = [
            self.run_task(name, task) \
                for name, task in self.tasks.clear.items()
        ]
        await asyncio.gather(
            *tasks
        )


    def run_loop(self, loop):
        asyncio.set_event_loop(
            loop
        )
        loop.run_until_complete(
            self.main_loop()
        )


    def start(self):
        self.event_loop = asyncio.new_event_loop()

        self.thread = Thread(
            target=self.run_loop,
            args=(self.event_loop)
        )

    def stop(self):
        self.running = False

        for task in asyncio.all_tasks(self.event_loop):
            task.cancel()

        self.event_loop.stop()
        self.event_loop.close()
        self.thread.join()
