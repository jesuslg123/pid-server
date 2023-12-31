#! -*- coding: utf-8 -*-
from aiohttp import web
import click
import os
import routes
# configure logging
import settings

@click.command()
@click.option('-H', '--host', default='0.0.0.0', help='TCP/IP hostname to serve on')
@click.option('-P', '--port', default=lambda: os.environ.get("PORT", "9099"), help='TCP/IP port to serve on')
def run_server(host, port):
    app = web.Application(client_max_size=16*1024*1024)
    routes.setup(app)
    web.run_app(app=app, host=host, port=port)


if __name__ == '__main__':
    run_server()
