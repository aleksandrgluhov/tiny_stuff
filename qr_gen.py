#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------- imports ---------------
import sys
from hashlib import md5
from time import localtime
from qrcode import *
from qrcode.image.pure import PymagingImage


# ----------------- constants -------------
qr = QRCode(version=1, error_correction=ERROR_CORRECT_L, image_factory=PymagingImage)


# ----------- program entry point ---------
if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as fr: 
            qr.add_data(fr.read())
        qr.make(fit=True)
        img = qr.make_image()
        with open('%s.%s' % (md5(str(localtime()).encode('utf-8')).hexdigest(), 'png'), 'wb') as fw:
            img.save(fw)
    except:
        print('Impossiburu to convert file to QR')
