# https://github.com/miguelgrinberg/flask-video-streaming/blob/master/camera_pi.py
import io
import time
try:
    import picamera
    from src.base_camera import BaseCamera
except ImportError:
    pass


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)
            # Flip picture
            camera.hflip = True
            camera.vflip = True

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                               use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
