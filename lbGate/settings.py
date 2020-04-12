#! /usr/bin/env python3
# coding: utf-8


""" LbGate settings, global variables"""


import time
import copy

import fct
import lbserial


HTTPD_PORT = 8444
MAX_NODE_ERRORS = 10000

node_list = dict(
    volcontrol=lbserial.Serial('volcontrol'))


acq = dict({
    'volcontrol': {
        'ping': {'val': 0, 'fct': "timeout_reset"},
        'vol': {'val': 0},
        'bal': {'val': 0},
        'power': {'val': 0},
        'debug': {'fct': "debugPrint"}
    }
})


run_loop = 0
log_msg = ""

def run():
    """
        Cycle execution to update log file
    """
    global run_loop
    global log_msg
    try:
        flog = open("/dev/shm/lbGate.settings", "w")
        msg = "###########################\n"
        msg = msg + "### " + time.strftime('%Y/%m/%d %H:%M:%S') + " ###\n"
        msg = msg + "# node_list =\n"
        msg = msg + "    #  node =   is_open |  open_cnt |    cmd_rx |   ping_tx |   ping_rx |        wd | Max/" + str(MAX_NODE_ERRORS) + " | read_iter\n"
        for key, value in node_list.items():
            msg = msg + "    " + key.rjust(7) + " = " + str(value.is_open()).rjust(9) + " | " + str(value.open_cnt).rjust(9) + " | " + str(value.cmd_rx_cnt).rjust(9) + " | " + str(value.ping_tx_cnt).rjust(9) + " | " + str(value.ping_rx_cnt).rjust(9) + " | " + str(value.error_cnt).rjust(9) + " | " + str(value.error_cnt_max).rjust(9) + " | " + str(value.read_iter).rjust(9) + "\n"
        msg = msg + "- run_loop = " + str(run_loop) + "\n"
        log_msg = msg
        flog.write(msg)
        flog.close()
    except Exception as ex:
        fct.log_exception(ex)
    run_loop = run_loop + 1
