#!/usr/bin/env python


import time
import sys
import picamera
def main(*argv):
    with picamera.PiCamera(framerate=90) as camera:
        try:
            camera.preview_fullscreen=False
            camera.preview_window=(100,20,640,480)
            time.sleep(2)
            camera.start_preview()
            time.sleep(10)
            camera.stop_preview
        except KeyboardInterrupt:
            print("-ending session-")
    return 0
                
    


