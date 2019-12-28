#!/usr/bin/python3
import os
import sys


class NordvpnMonitor:
    """A program that periodically (crontab) monitors nordvpn
    and reconnects if it is disconected.  It reconnects
    to Atlanta unless otherwise specified.
    Allows a single argument which is a city name (defaults to Atlanta.)"""

    def __init__(self, *argv):
        if len(sys.argv) == 2:
            location = sys.argv[1]
        else:
            location = "Atlanta"
        self.location = location

    def check_status(self):
        """ Check the status of Nordvpn and return the
        connection status True/False """

        response = os.popen("nordvpn status").read()
        lines = response.split("\n")
        status = [line.split(" ")[1] for line in lines if line.startswith("Status")]
        if (status[0] == 'Connected'):
            return True
        else:
            return False

    def start_nordvpn(self):
        """ Start the nordvpn server and return the status after restart """
        retval = os.popen("nordvpn connect Atlanta").read()
        return response


# --------------------------------------------------------------------
# CALL THE CLASS TO CHECK THE STATUS AND RESTART IF NEEDED
# --------------------------------------------------------------------
nord = NordvpnMonitor()
response = nord.check_status()
if response == False:
    response = nord.start_nordvpn()
