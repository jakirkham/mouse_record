from __future__ import print_function

__author__ = "Bailey Hwa <hwab@janelia.hhmi.org>"
__date__ = "$July 30, 2015 20:20:18 EDT$"

from glob import glob

from setuptools import setup, find_packages

import versioneer


setup(
    name="mouse_recorder",
    version=versioneer.get_version(),
    description="An Event Triggered Recorder",
    url="https://github.com/DudLab/mouse_record",
    license="GPLv3",
    author="Bailey Hwa",
    author_email="hwab@janelia.hhmi.org",
    scripts=glob("bin/*"),
    py_modules=["versioneer"],
    packages=find_packages(exclude=["tests*"]),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=["picamera >=1.0", "RPi.GPIO >=0.5.11"],
    tests_require=["nose", "mock"],
    test_suite="nose.collector",
    zip_safe=True
)
