#!/usr/bin/env python

""" (insert tool description in docstrings format) """

__author__ = "Nicolas Perreault"
__email__ = "name@acme.com"
__version__ = "0.0.2"
__status__ = "Alpha"

# Imports here, don't break libaries namespaces with from statements
import argparse
import logging
import urllib2

def fetch_url(url):
    """ Method that fetch the DOCTYPE information from any webpage """
    request = urllib2.Request(url)

    try:
        response = urllib2.urlopen(request)
        answer = response.read()
        doctype = answer[:answer.find('>')+1]

        print
        print 'DOCTYPE for this page is:'
        print '-'*len(doctype)
        print doctype
        print '-'*len(doctype)
        print
    except urllib2.URLError, e:
        logging.warning('Unable to acquire data, please validate url provided',e)

def main():
    parser = argparse.ArgumentParser(description='Script definition')
    parser.add_argument('--url', default='http://www.canoe.ca', help='Test URL')
    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')

    fetch_url(args.url)

if __name__ == '__main__':
    main()
