from core.system.logging import logger
from core.flask import _flask, _background

wsgi = _flask

def main():
    try:
        wsgi.run()

    except KeyboardInterrupt:
        _background.stop()
        logger.info('Application stopped by user...')


if __name__ == '__main__':
    main()
