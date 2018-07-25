# coding: utf-8
"""
0xFF-D8-FF-DB — Samsung D807 JPEG file.
0xFF-D8-FF-E0 — Shown above. Standard JPEG/JFIF file.
0xFF-D8-FF-E1 — Shown above. Standard JPEG/Exif file.
0xFF-D8-FF-E2 — Canon EOS-1D JPEG file.
0xFF-D8-FF-E3 — Samsung D500 JPEG file.
0xFF-D8-FF-E8 — Shown above. Still Picture Interchange File Format (SPIFF).

GIF87a 47 49 46 38 37 61
GIF89a 47 49 46 38 39 61
"""
from __future__ import unicode_literals

import struct

FILE_HEX_CODE = {
    '25504446': 'pdf',
    '89504E47': 'png',
    '47494638': 'gif',

    'FFD8FFDB': 'jpg',
    'FFD8FFE0': 'jpg',
    'FFD8FFE1': 'jpg',
    'FFD8FFE2': 'jpg',
    'FFD8FFE3': 'jpg',
    'FFD8FFE8': 'jpg'
}


def bytes2hex(bytedata):
    num = len(bytedata)
    hexstr = []
    for i in range(num):
        td = '%x' % bytedata[i]
        if len(td) % 2:
            hexstr.append('0')
        hexstr.append(td)
    return ''.join(hexstr).upper()


def get_file_type(filepath):
    with open(filepath, 'rb') as _file:
        num = 4
        hbytes = struct.unpack_from(
            'B' * num,
            _file.read(num))
        f_hcode = bytes2hex(hbytes)
    return FILE_HEX_CODE.get(f_hcode, '')
