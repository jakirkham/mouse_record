
from __future__ import print_function


__author__ = "Bailey Hwa <hwab@janelia.hhmi.org>"
__date__ = "$July 30, 2015 20:20:18 EDT$"


from glob import glob
import os
import shutil
import sys

from setuptools import setup, find_packages
import versioneer
setup(
    name="mouse_recorder",
    version="0.0.1",
    description="An Event Triggered Recorder",
    url="https://github.com/bnhwa/mouse_record"
    license="GPLv3",
    author="Bailey Hwa",
    author_email="hwab@janelia.hhmi.org",
    scripts=glob("bin/*"),
    zip_safe=True
)
