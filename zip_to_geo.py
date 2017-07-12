'''
Created on Jul 12, 2017

@author: akira
'''
#!py_env/bin/python
# python3

import logging, logging.handlers
import argparse
import time
import sys

import requests

MAX_TRY = 5
TIMEOUT = 10
INTERVAL = 5
GOOGLE_API_KEY = "YOUR API KEY"
URL_ZC = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={}"
URL_GOOGLE = "https://maps.googleapis.com/maps/api/geocode/json?address={0}{1}{2}&key={3}"

logger = logging.getLogger(__name__)

def rest_request(url, user=None, password=None):
    status = None
    tries = 0
    while not status and tries < MAX_TRY:
        try:
            creds = (user, password) if user and password else None
            resp = requests.get(url, verify=True, auth=creds, timeout=TIMEOUT)
            status = resp.status_code
        except requests.exceptions.ConnectionError as err:
            logger.warning("rest_request: Could not reach '%s': %s. Trying again in %s seconds", url, err, INTERVAL)
            time.sleep(INTERVAL)
        except requests.exceptions.Timeout as err:
            logger.warning("rest_request: Request to '%s' timed out after %d seconds: %s. Trying again.",
                        url, TIMEOUT, err)
        finally:
            tries += 1
            if tries >= MAX_TRY:
                logger.error("rest_request: Could not reach '%s': %s", url, err)

    if status == 200:
        return resp
    elif status != 200 and resp:
        logger.error("rest_request: '%s' returned status code %s: %s", url, status, resp.text)
        return None
    else:
        return None

def logging_setup(args):
    log_root = logging.getLogger('')
    if args.verbose > 1:
        log_root.setLevel(logging.DEBUG)
    elif args.verbose == 1:
        log_root.setLevel(logging.INFO)
    
    log_format = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(log_format)
    log_root.addHandler(log_handler)

def main(argv):
    parser = argparse.ArgumentParser(description="Get latitude & longitude from zipcode")
    parser.add_argument("-v", "--verbose", action="count", default=0, dest="verbose",
                        help="Enable verbose output (specify multiple times to increase level)")
    parser.add_argument("-z", "--zipcode", action="store", metavar="STRING", dest="zc", required=True,
                        help="Zipcode to be queried")

    args = parser.parse_args(argv)
 
    # Logging setup
    logging_setup(args)
    log_main = logging.getLogger('main')
    
    if args.zc:
        zc = args.zc
    
    r = rest_request(URL_ZC.format(zc))
    if not r:
        log_main.error("request failed for zipcode")
        return 1
    
    data = r.json()
    
    addr1 = data['results'][0]['address1']
    addr2 = data['results'][0]['address2']
    addr3 = data['results'][0]['address3']
    
    log_main.info("fetched %s, %s, %s", addr1, addr2, addr3)
    
    r = rest_request(URL_GOOGLE.format(addr1, addr2, addr3, GOOGLE_API_KEY))
    if not r:
        log_main.error("request failed for geocode")
        return 1
    
    data = r.json()
    log_main.info("latitude: %s, longitude: %s", data['results'][0]['geometry']['location']['lat'],
                                 data['results'][0]['geometry']['location']['lng'])
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))   
