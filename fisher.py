# coding: utf-8
from app import create_app

__author__ = 'Vinson'


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)

    # 此处是单进程，单线程
