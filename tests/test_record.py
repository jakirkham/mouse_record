__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 10, 2015, 3:47 PM$"

import os
import shutil
import tempfile
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.OUT)

from mouse.record import main


class TestPicture(object):
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
             "1",
             "1",
             "."
        )
        time.sleep(4)
        GPIO.output(12, GPIO.LOW)


        filenames = []
        for each_filename in os.listdir(self.tempdir):
            filenames.append(os.path.join(self.tempdir, each_filename))
        filenames.sort()
        assert len(filenames)==1
        assert ".h264" in filenames[0]
