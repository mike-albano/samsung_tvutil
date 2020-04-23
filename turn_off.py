"""Turns off a >2016 model of Samsung TV if past midnight."""
import os
import datetime
import wakeonlan
import json
import logging
import sys
import time
from samsungtvws import SamsungTVWS

# Increase debug level
logging.basicConfig(level=logging.INFO)

OFF_HOURS = ['22', '00', '01', '02', '03', '04', '05', '06', '07']
CHECK_INTERVAL = 60  # How often (s) the TV will be checked.
TV_IP = '192.168.0.42'  # Your TVs IP address.

def _initial_connect():
  """Make the initial TV connection and generate token file if necessary.

  Returns: Samsung TV Class.
  """
  # Autosave token to file
  token_file = os.path.dirname(os.path.realpath(__file__)) + '/tv-token.txt'
  return SamsungTVWS(host=TV_IP, port=8002, token_file=token_file)


def _power_off(tv):
  """Check the time and turn off TV if its still on after hours."""
  powered_off = None
  while powered_off is None:
    try:
      tv.shortcuts().power()  # Power off the TV.
      powered_off = True
      print('TV Powered off.')
    except:
      print('Failed to power off TV at ip:8001/api/v2/\n'
            'Does this URL work in a browser?:\n'
            'http://%s:8001/api/v2/' % TV_IP)
      pass
      time.sleep(5)  # If poweroff Request fails, wait 5s and try again.


def check_ping():
    response = os.system("ping -c 1 %s >/dev/null 2>&1" % TV_IP)
    if response == 0:
      return True
    else:
      logging.info('Host did not respond to ping. Retrying in %ss' % CHECK_INTERVAL)


def check_tv():
  host_check = check_ping()
  if host_check:
    tv = _initial_connect()
    _power_off(tv)

    # Print useful info about the TV.
    #print(json.dumps(tv.rest_device_info(), indent=2))


if __name__ == '__main__':
    while True:
      if datetime.datetime.now().strftime("%H") in OFF_HOURS:
        check_tv()
        logging.info('sleeping for %ss' % CHECK_INTERVAL)
        time.sleep(CHECK_INTERVAL)
      else:
        logging.info('Not time to power off the TV. Sleeping for %ss' %
                     CHECK_INTERVAL)
        time.sleep(CHECK_INTERVAL)
