import logging

from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

def headers_to_str(headers):
    s = '\nHeaders:\n'
    for k, v in headers:
        s += f'  {k}: {v}\n'
    return s

def body_to_str(body):
    return f'\nBody:\n  {body.decode("utf-8")}'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catchall(path):
    app.logger.info(f'\n{request.method} {request.url}')
    app.logger.info(headers_to_str(request.headers))
    app.logger.info(body_to_str(request.get_data()))
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0')
