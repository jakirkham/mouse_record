__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 10, 2015, 2:38 PM$"

import os
import shutil
import tempfile
import time

from mouse.preview import main
class TestPreview(object):
    def test_main_0(self):
        main(
            "",
            "1"
        )
