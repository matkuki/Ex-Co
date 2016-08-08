
# -*- coding: utf-8 -*-

"""
    Ex.Co. LICENSE :
        This file is part of Ex.Co..

        Ex.Co. is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        Ex.Co. is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with Ex.Co..  If not, see <http://www.gnu.org/licenses/>.


    PYTHON LICENSE :
        "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation,
        used by Ex.Co. with permission from the Foundation


    Cython LICENSE:
        Cython is freely available under the open source Apache License


    PyQt4 LICENSE :
        PyQt4 is licensed under the GNU General Public License version 3
    PyQt Alternative Logo LICENSE:
        The PyQt Alternative Logo is licensed under Creative Commons CC0 1.0 Universal Public Domain Dedication


    Qt Logo LICENSE:
        The Qt logo is copyright of Digia Plc and/or its subsidiaries.
        Digia, Qt and their respective logos are trademarks of Digia Corporation in Finland and/or other countries worldwide.


    Tango Icons LICENSE:
        The Tango base icon theme is released to the Public Domain.
        The Tango base icon theme is made possible by the Tango Desktop Project.

    My Tango Style Icons LICENSE:
        The Tango Icons I created are released under the GNU General Public License version 3.
    
    
    Eric6 LICENSE:
        Eric6 IDE is licensed under the GNU General Public License version 3


    Nuitka LICENSE:
        Nuitka is a Python compiler compatible with Ex.Co..
        Nuitka is licensed under the Apache license.
"""

##  FILE DESCRIPTION:
##      Setup file for the Cython module
##      NOTES:
##          Build the Cython module with:
##              "python cython_setup.py build_ext --build-lib=cython_build/"

import shutil
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import build_ext

# Clean-up
print("Pre-build clean-up started ...")
if os.path.exists('cython_build'):
    shutil.rmtree('cython_build')
if os.path.exists('build'):
    shutil.rmtree('build')
filelist = [f for f in os.listdir(".") if f.endswith(".c")]
for f in filelist:
    os.remove(f)
print("Pre-build clean-up completed.")

source_files = [
    "cython_lexers.pyx"
]

ext_modules = [
    Extension(  
        "cython_lexers",
        source_files,
        include_dirs = [],
        libraries = [],
        library_dirs = []
    )
]

setup(
    name = 'Ex.Co. Cython extensions',
    cmdclass = {
        'build_ext':    build_ext,
    },
    ext_modules = ext_modules
)

# Clean-up
print("Post-build clean-up started ...")
if os.path.exists('build'):
    shutil.rmtree('build')
filelist = [f for f in os.listdir(".") if f.endswith(".c")]
for f in filelist:
    os.remove(f)
print("Post-build clean-up completed.")

print("Kopiranje cython_lexers.pyd datoteke ...")
shutil.copyfile(
    'D:/Domaci_Projekti/ExCoEdit/cython_build/cython_lexers.pyd', 
    "D:/Domaci_Projekti/razno_za_exco/Testiranje/cython_lexers.pyd"
)

