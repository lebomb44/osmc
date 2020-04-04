#! /usr/bin/env python3
# coding: utf-8


""" LbGate basic functions """


from __future__ import print_function
import time
import traceback
from six.moves import urllib
import requests

import settings


def log(msg):
    """ Print message with a time header """
    print(time.strftime('%Y/%m/%d %H:%M:%S: ') + msg)


def log_exception(ex, msg="ERROR Exception"):
    """ Print exception with a time header """
    log(msg + ": " + str(ex))
    log(traceback.format_exc())


def http_request(url):
    """ Do HTTP request to the URL """
    try:
        log("URL call: " + url)
        requests.get(url, timeout=1.0)
    except requests.exceptions.RequestException as ex:
        log("ERROR http_request: " + str(ex))


def timeout_reset(node_, cmd_, arg_array_):
    """ Reset timeout to zero """
    #log("### Reset of " + node_ + " timeout")
    if settings.node_list[node_].error_cnt > settings.node_list[node_].error_cnt_max:
        settings.node_list[node_].error_cnt_max = settings.node_list[node_].error_cnt
    settings.node_list[node_].error_cnt = 0
    settings.node_list[node_].ping_rx_cnt += 1
