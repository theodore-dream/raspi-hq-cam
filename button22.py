import picamera

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
camera.start_recording('my_video.h264', quality=25)
camera.wait_recording(5)
camera.stop_recording()
