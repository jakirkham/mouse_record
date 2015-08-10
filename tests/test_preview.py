__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 10, 2015, 2:38 PM$"

import os
import shutil
import tempfile
import time

from mouse.preview import main


class TestPreview(object):
    def setup(self):
        self.cwd = os.getcwd()
        self.tempdir = ""
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

        print("tempdir = \"%s\"" % self.tempdir)

    def teardown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tempdir)
        self.tempdir = ""
        self.cwd = ""

    def test_main_0(self):
        main("",
             "1"
        )

        while len(os.listdir(self.tempdir)) < 2:
           time.sleep(1)
        time.sleep(1)
