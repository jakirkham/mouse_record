from __future__ import print_function

__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 05, 2015, 3:36 PM$"

import argparse
import io
import picamera
import datetime
import os


def main(*argv):
    """
        Simple main function that takes a photo of the background when run.

        Args:
            argv(str):                      Arguments are stored as a list

        Notes:
            these are the parameters of the arguments.

            folder(str):                    File directory


    """

    # Directory is stored here
    parser = argparse.ArgumentParser(
        description="Directory to save the picture into"
    )
    parser.add_argument(
        "folder",
        type=str,
        help="Directory"
    )
    args = parser.parse_args(argv[1:])
    folder = args.folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    with picamera.PiCamera(framerate=90) as camera:
        j = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")
        camera.capture(os.path.join(
            folder, "background-" + str(j) + os.extsep + "jpg"
        ))

    return 0
