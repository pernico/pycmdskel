#!/usr/bin/env python

""" (insert tool description in docstrings format) """

__author__ = "Nicolas Perreault"
__email__ = "name@acme.com"
__version__ = "0.0.1"
__status__ = "Alpha"

# Do your imports here :
import argparse
import urllib2

def fetch_url(url):
    """ Method that handles the request to the web resource """
    request = urllib2.Request(url)

    try:
        response = urllib2.urlopen(request)
        answer = response.read()
        print answer[:100]
    except urllib2.URLError, e:
        print 'Unable to acquire data, please validate url provided',e

def main():
    parser = argparse.ArgumentParser(description='Script definition')
    parser.add_argument('--url', default='http://www.canoe.ca', help='Test URL')
    args = parser.parse_args()
    fetch_url(args.url)

if __name__ == '__main__':
    main()
