  gst-launch-1.0 -e -v \
    libcamerasrc camera-name="/base/axi/pcie@1000120000/rp1/usb@200000-1.3:1.0-056e:701c" ! \
    video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! \
    queue leaky=downstream max-size-buffers=1 ! \
    videoconvert ! videoscale ! \
    video/x-raw,format=RGB,width=640,height=640,framerate=30/1 ! \
    queue leaky=downstream max-size-buffers=1 ! \
    hailonet hef-path=/usr/share/hailo-models/yolov8s_h8l.hef ! \
    queue leaky=downstream max-size-buffers=1 ! \
    hailofilter so-path=/usr/lib/aarch64-linux-gnu/hailo/tappas/post_processes/libyolo_hailortpp_post.so function-name=yolov8s ! \
    hailooverlay ! videoconvert ! autovideosink sync=false
