__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 10, 2015, 2:38 PM$"

import os
import shutil
import tempfile

from mouse.picture import main


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
        main(
            "",
            "."
        )

        filenames = []
        for each_filename in os.listdir(self.tempdir):
            filenames.append(os.path.join(self.tempdir, each_filename))
        filenames.sort()
        assert len(filenames) == 1
        assert ".jpg" in filenames[0]
