# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

import shutil


def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):
    """Patches shutil method to increase the buffer size"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

shutil.copyfileobj = _copyfileobj_patched
