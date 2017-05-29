from __future__ import absolute_import
import os
import socket
import time
import httplib
import logging

# Set-up logging to match gunicorn's
logging.basicConfig(format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s', datefmt='[%Y-%m-%d %H:%M:%S %z]', level=logging.INFO)

# Puppetboard has the irritating hard requirement that puppetdb
# must be running and listening before it starts, and will otherwise
# crash. This makes starting services difficult.
conn = httplib.HTTPConnection(os.getenv('PUPPETDB_HOST', 'puppetdb'), int(os.getenv('PUPPETDB_PORT', '8080')), timeout=10)

while True:
    try:
        conn.request('GET', '/')
        response = conn.getresponse()
        status = response.status
    except (socket.error, httplib.ResponseNotReady, httplib.ImproperConnectionState, httplib.HTTPException):
        logging.info('Waiting for PuppetDB')
        time.sleep(5)
    else:
        if status == 302:
            time.sleep(10)
            conn.close()
            break

os.environ['PUPPETBOARD_SETTINGS'] = '/var/www/puppetboard/settings.py'
from puppetboard.app import app as application
