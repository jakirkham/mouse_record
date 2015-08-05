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
        Simple main function that performs event center recording.
        Defines arguments:

        Args:
            argv(str):                      Arguments are stored as a list

        Notes:
            these are the parameters of the arguments.

            folder(str):                    File directory


    """

    # Directory is stored here
    parser.add_argument(
        "folder",
        type=str,
        default='.',
        help="Directory"
    )
    args = parser.parse_args(argv[1:])
    folder = args.folder

    with picamera.PiCamera(framerate=90) as camera:
        try:
            # Creates directory/folder if the desired directory is nonexistent
            if not os.path.exists(folder):
                os.makedirs(folder)
                j = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")
                camera.capture(folder, "background" + str(j) + ".jpg")

        except KeyboardInterrupt:
            print("Program is now ending session.")

    return 0
