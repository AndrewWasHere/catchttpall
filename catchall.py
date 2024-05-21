import argparse
import logging

from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

status_code = 418  # I'm a teapot

def headers_to_str(headers):
    s = '\nHeaders:\n'
    for k, v in headers:
        s += f'  {k}: {v}\n'
    return s

def body_to_str(body):
    return f'\nBody:\n  {body.decode("utf-8")}'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTION'])
def catchall(path):
    """The One route handler to rule them all."""
    app.logger.info(f'\n{request.method} {request.url}')
    app.logger.info(headers_to_str(request.headers))
    app.logger.info(body_to_str(request.get_data()))
    return '', status_code


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--status-code', 
        type=int, 
        default=200,
        help='Status code to return', 
    )
    args = parser.parse_args()
    return args


def main():
    global status_code

    args = parse_command_line()
    status_code = args.status_code

    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
