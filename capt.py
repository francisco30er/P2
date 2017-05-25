#!/usr/bin/python
import time
import picamera
 
with picamera.PiCamera() as picx:
    picx.start_preview()
    time.sleep(5)
<<<<<<< HEAD
    picx.capture('mifoto1.jpg')
=======
    picx.capture('mifoto.jpg')
>>>>>>> e1eae7beada0a627172e3b53e39a0883bcb4b630
    picx.stop_preview()
    picx.close()
