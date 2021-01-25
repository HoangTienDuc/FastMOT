import cv2

import fastmot

input_uri = "rtsp://admin:abcd1234@192.168.1.104:554/Streaming/Channels/101?transportmode=mcast&profile=Profile_1"
output_uri = "output.mp4"
video_io = {
        "camera_size": [1920, 1080],
        "camera_fps": 30,
        "buffer_size": 10
    }
stream = fastmot.VideoIO([1280, 720], video_io, input_uri, output_uri)

stream.start_capture()
while True:
    frame = stream.read()
    if frame is None:
        break
    cv2.imshow('Video', frame)
    cv2.waitKey(1)