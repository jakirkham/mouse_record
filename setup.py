from __future__ import print_function

__author__ = "Bailey Hwa <hwab@janelia.hhmi.org>"
__date__ = "$July 30, 2015 20:20:18 EDT$"

from glob import glob
from setuptools import setup, find_packages

setup(
    name="mouse_recorder",
    version="0.0.1",
    description="An Event Triggered Recorder",
    url="https://github.com/DudLab/mouse_record",
    license="GPLv3",
    author="Bailey Hwa",
    author_email="hwab@janelia.hhmi.org",
    scripts=glob("bin/*"),
    packages=find_packages(exclude=["tests*"]),
    install_requires=["picamera >=1.0", "RPi.GPIO >=0.5.11"],
    tests_require=["nose", "mock"],
    test_suite="nose.collector",
    zip_safe=True
)
