from core.system.logging import logger
from core.flask import _flask, _background


def main():
    try:
        _flask.run(
            host='0.0.0.0', port=8080,
            debug=True
        )

    except KeyboardInterrupt:
        _background.stop()
        logger.info('Application stopped by user...')


if __name__ == '__main__':
    main()
