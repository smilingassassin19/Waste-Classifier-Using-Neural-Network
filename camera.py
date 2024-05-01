import cv2 as cv
class Camera:
    def __init__(self):
        self.Camera=cv.VideoCapture(0)
        if not self.Camera.isOpened():
            raise ValueError("Unable to open the camera!")
        self.width=self.Camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height=self.Camera.get(cv.CAP_PROP_FRAME_HEIGHT)
    def __del__(self):
        if self.Camera.isOpened():
            self.Camera.release()
    def get_frame(self):
        if self.Camera.isOpened():
            ret,frame=self.Camera.read()

            if ret:
                return (ret,cv.cvtColor(frame,cv.COLOR_RGB2BGR))
            else:
                return (ret,None)
        else:
            return None
