#!/usr/bin/env bash

# ARGS=("$@")

# XAUTH=/tmp/.docker.xauth
# if [ ! -f $XAUTH ]; then
#     xauth_list=$(xauth nlist $DISPLAY)
#     xauth_list=$(sed -e 's/^..../ffff/' <<<"$xauth_list")
#     if [ ! -z "$xauth_list" ]; then
#         echo "$xauth_list" | xauth -f $XAUTH nmerge -
#     else
#         touch $XAUTH
#     fi
#     chmod a+r $XAUTH
# fi

docker run \
-it \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
-p 2233:22 \
--rm \
--name ros \
--user root \
-e GRANT_SUDO=yes \
-v ~/catkin_ws:/root/catkin_ws \
softmac/sdc-course-docker:latest \
bash
