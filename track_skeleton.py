#!/usr/bin/env python3

from pathlib import Path
import argparse
import logging
import time
import json
import cv2

import fastmot


def main():


    # load config file
    with open(Path(__file__).parent / 'cfg' / 'mot.json') as config_file:
        config = json.load(config_file, cls=fastmot.utils.ConfigDecoder)


    draw = True
    
    mot = fastmot.MOT((1280, 720), 0.04, config['mot'],
                        draw=draw, verbose=False)




    url = "rtsp://admin:abcd1234@192.168.1.104:554/Streaming/Channels/101?transportmode=mcast&profile=Profile_1"
    cap = cv2.VideoCapture(url)
    
        
    while True:
        ret, frame = cap.read()
        if frame is None:
            break

        mot.step(frame)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


    

if __name__ == '__main__':
    main()
