from pam import pam

from flask import (
    Flask, render_template, 
    request, redirect, url_for, 
    session, jsonify
)


from core.shark import (
    Shark, Filter)

from os import urandom
from base64 import b64encode

from functools import wraps


_shark = Shark(
    'enp37s0'
)

_filter = Filter(
    'enp37s0'
)

_flask = Flask(
    __name__,
    static_folder='../../static',
    template_folder='../../templates'
)
_flask.secret_key = b64encode(
    urandom(256)
).decode('utf-8')

authenticator = pam()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@_flask.route('/tcp_data')
@login_required
def tcp_data():
    data = _shark.live_packets(
        proto='tcp'
    )

    return jsonify(data)

@_flask.route('/udp_data')
@login_required
def udp_data():
    data = _shark.live_packets(
        proto='udp'
    )

    return jsonify(data)


@_flask.route('/tcp')
@login_required
def tcp():
    return render_template('tcp.html')

@_flask.route('/udp')
@login_required
def udp():
    return render_template('udp.html')


@_flask.route('/filter_ip')
@login_required
def filter_ip():
    data = _filter.live_packets(
        'ip'
    )

    return jsonify(data)

@_flask.route('/filter_dns')
@login_required
def filter_dns():
    data = _filter.live_packets(
        'dns'
    )

    return jsonify(data)

@_flask.route('/filter_tls')
@login_required
def filter_tls():
    data = _filter.live_packets(
        'tls.handshake.type == 1 and tcp'
    )

    return jsonify(data)

@_flask.route('/filter_http')
@login_required
def filter_http():
    data = _filter.live_packets(
        'http.request.method and tcp'
    )

    return jsonify(data)


@_flask.route('/filters')
@login_required
def filters():
    return render_template('filters.html')


@_flask.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):

            #print(request.form)
            username, password = request.form.get('username', None), \
                request.form.get('password', None)

            if (authenticator.authenticate(
                username=username, password=password)
            ): 
                session['authenticated'] = True
                session['username'] = username

                return redirect(url_for('index'))

            else:
                return redirect(url_for('login'))

    return render_template(
        'login.html')

@_flask.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


@_flask.route('/')
def index():
    authenticated = session.get(
        'authenticated', False
    )

    return render_template(
        'index.html', authenticated=authenticated)


if __name__ == '__main__':
    _flask.run(debug=True)
