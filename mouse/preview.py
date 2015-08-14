from __future__ import print_function

"""
===============================================================================
Overview
===============================================================================

The mouse-picture program shows a preview of the camera, as part of the setup
of the Raspberry Pi module on the behavioral rig. The user can set the length
of the preview and quit at any time, using the ``Ctrl +c`` command.
"""

__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$July 30, 2015 20:20:18 EDT$"

import argparse
import time
import picamera


def main(*argv):
    parser = argparse.ArgumentParser(
        description="Takes camera preview. Exit using `Ctrl + c`."
    )
    parser.add_argument(
        "time",
        nargs='?',
        type=int,
        default=15,
        help="Preview length (default is 15 seconds)."
    )
    args = parser.parse_args(argv[1:])
    t = args.time

    with picamera.PiCamera(framerate=90) as camera:
        try:
            camera.preview_fullscreen = False
            camera.preview_window = (100, 20, 640, 480)
            camera.start_preview()
            time.sleep(t)
        finally:
            camera.stop_preview()
            print("-ending session-")
    return 0
