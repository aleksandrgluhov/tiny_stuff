#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    FDB switch info collector
    
    sudo pip install netsnmp-py
    sudo dnf install net-snmp-config
    sudo dnf install redhat-rpm-config
    sudo dnf install python-devel
    sudo dnf install net-snmp-devel
    sudo dnf install zeromq-devel
    sudo dnf install czmq-devel

"""

# -------------------- imports -----------------------
import sys
import netsnmp


# ------------------- constants ----------------------
_OID = '.1.3.6.1.2.1.17.7.1.2.2.1.2'
_OID_offset = len(_OID) + 1


# ----------- procedures and functions ---------------
def public_resolv(sw_ip):
    retval = []
    device = {}
    with netsnmp.SNMPSession(sw_ip, 'public') as ss:
        discovery = [response for response in ss.walk([_OID])]
        for item in discovery:
            for row in item:
                if _OID in row:
                    device_str = row[_OID_offset:].split('.')
                    vlan = device_str[0]
                    mac = "%02x:%02x:%02x:%02x:%02x:%02x" % tuple(int(i) for i in device_str[1:])
                    device['mac'] = mac
                    device['vlan'] = vlan
                    retval.append(device)
                    device = {}
    return retval


# ------------- program entry point ----------------
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            d = public_resolv(sys.argv[1])
            for host in d:
                print host['mac'], host['vlan']
            print ('total hosts: %s' % len(d))
        except:
            print('Switch resolve error!')
