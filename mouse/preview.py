from __future__ import print_function

__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org"
__date__ = "$July 30, 2015 20:20:18 EDT$"

import argparse
import time
import sys
import picamera


def main(*argv):
    parser = argparse.ArgumentParser(
        description="Takes camera preview. Exit using KeyboardInterrupt."
        )
    args =parser.parse_args()
    with picamera.PiCamera(framerate=90) as camera:
        try:
            while True:
                camera.preview_fullscreen=False
                camera.preview_window=(100,20,640,480)
                camera.start_preview()
                time.sleep(600)
        finally:
            camera.stop_preview
            print("-ending session-")
    return 0
