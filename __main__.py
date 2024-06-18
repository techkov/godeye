from core.flask import _flask


def main():
    _flask.run(
        host='0.0.0.0', port=8080,
        debug=True
    )


if __name__ == '__main__':
    main()
