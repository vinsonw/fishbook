# coding: utf-8
__author__ = 'Vinson'

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html>i</html>', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers


# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
