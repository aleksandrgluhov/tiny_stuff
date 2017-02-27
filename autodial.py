#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
    Autodial - is a python program, that initializes
    an asterisk call to the destination subscriber by 
    creating a call file. After the destination 
    subscriber picks up the phone, asterisk connects
    it to the source subscriber. 

    This is an example of working with a call files 
    with a python.
"""


# -------------------- imports ----------------------
import os
import sys
import pwd
import grp


# ------------------- constants ---------------------
c_path = '/var/spool/asterisk/tmp'
asterisk_cpath = '/var/spool/asterisk/outgoing'

try:
    uid = pwd.getpwnam('asterisk').pw_uid
    gid = grp.getgrnam('asterisk').gr_gid
except KeyError as e:
    print 'Make sure that asterisk user/group exists!'

# ------------ procedures and functions -------------


def create_call(callernum, dialnum):
    """
        Function, that creates an asterisk call file, gives it a uid and gid 
        settings.
        :param callernum: Source subscriber
        :param dialnum: Destination subscriber
        :return: Full file name
    """
    retval = ''
    if (len(callernum) > 0) and (len(dialnum) > 0):
        filename = '%s.call' % callernum
        callerinfo = 'Call to %s' % callernum

        if os.path.exists(c_path):
            callfilename = c_path + '/' + filename
            callfile = open(callfilename, 'w')
            callfile.write('Action: originate\n')
            callfile.write('Channel: SIP/%s\n' % dialnum)
            callfile.write('MaxRetries: 90\n')
            callfile.write('WaitTime: 8\n')
            callfile.write('RetryTime: 10\n')
            callfile.write('CallerID: %s\n' % callerinfo)
            callfile.write('Extension: %s\n' % callernum)
            callfile.write('Set: REALCALLERIDNUM=%s\n' % dialnum)
            callfile.write('Async: yes\n')
            callfile.write('Priority: 1\n')
            retval = callfilename
            
            try:
                os.chown(callfilename, uid, gid)
            except:
                print 'Chown failed on: %s' % callfilename

    return retval


def dial(callfile):
    """
    Procedure that makes a call by moving callfile to apropiate dir
    :param callfile: prepared callfile
    :return:
    """
    if os.path.isfile(callfile):
        oldpath, callfilename = os.path.split(callfile) 
        try:
            os.rename(callfile, asterisk_cpath + '/' + callfilename)
        except:
            print 'Make call failed! Is asterisk installed correct?'


def usage():
    """
    Help srceen
    :return: - 
    """
    print 'AUTODIAL'
    print 'A python script, that initiates dialog between two subscribers'
    print 'by using asterisk callfiles'
    print '---'
    print 'usage: autodial.py <caller_number> <dial_number>'
    print 'or autodial.py with anything to see this help screen'


# ------------- program entry point -------------
if __name__ == '__main__':
    if len(sys.argv) == 3:
        call = create_call(sys.argv[1], sys.argv[2])
        dial(call)
    else:
        usage()
