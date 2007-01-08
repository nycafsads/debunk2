#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2007 - Håvard Dahle 
#    <havard@dahle.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


# To create win32 bdist exe: python setup.py py2exe --includes sip
# To create source: python setup.py 
#
#

from distutils.core import setup
#from setuptools import setup

PY2EXE=False

try:
    import py2exe
    PY2EXE=True
except ImportError:
    print "Warning: py2exe not installed. You will not be able to create windows executables"

import sys, os.path

import nk2parser

setup(name="debunk2",
      version=str(nk2parser.__version__),
      description="Read MS Outlook autocomplete (NK2) files and extract email addresses",
      author='Håvard Dahle',
      author_email="havard@dahle.no",
      url="http://code.google.com/p/debunk2/",
      download_url='http://code.google.com/p/debunk2/downloads/list', 
      py_modules=['nk2parser', 'debunk2_ui'],
      data_files=[#('share/finfaktura/pixmaps', ['pixmaps/error.png', 'pixmaps/warning.png']),
            ('share/debunk2/data', ['debunk2.ui', ]),
           ],
      scripts=["debunk2.py"],
      console=['debunk2.py'], # for py2exe
      license="GPL2",
      long_description="""Microsoft Outlook stores its autocomplete email info in an undocumented file format. This project tries to unlock the information therein.""",
      #install_requires = ['docutils>=0.3', 'reportlab'],
      #zip_safe=True,
     )
