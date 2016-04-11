# -*- coding: utf-8 -*-

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from edge import app
import sys

port_number = 5015
# TODO - config_dict should be constructed with proper type
# if int(config_dict[constants.HACONFIG_SECTION][constants.HACONFIG_NEWRELIC]):
#     import newrelic.agent

#     newrelic.agent.initialize(
#         '/home/edge/projects/hirenew_venv/local/lib/python2.7/site-packages/newrelic-2.50.0.39/newrelic/newrelic.ini')

sys.dont_write_bytecode = True
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port_number, '0.0.0.0')
print "started service",port_number
IOLoop.instance().start()