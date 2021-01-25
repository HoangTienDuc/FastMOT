nvidia-docker run --rm --gpus all -it -v `pwd`:/data -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY fastmot:1.0.1
