  gst-launch-1.0 -e -v \
    v4l2src device=/dev/video0 ! \
    video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! \
    videoconvert ! video/x-raw,format=NV12 ! \
    nvvideoconvert ! 'video/x-raw(memory:NVMM),format=NV12' ! \
    m.sink_0 nvstreammux name=m batch-size=1 width=640 height=480 ! \
    nvinfer config-file-path=/home/relics9/vtx/test/ds_infer_primary.txt ! \
    nvdsosd ! \
    nvvideoconvert ! 'video/x-raw(memory:NVMM),format=RGBA' ! \
    nv3dsink sync=false


  gst-launch-1.0 -e -v \
    v4l2src device=/dev/video0 ! \
    video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! \
    videoconvert ! video/x-raw,format=NV12 ! \
    nvvideoconvert ! 'video/x-raw(memory:NVMM),format=NV12' ! \
    m.sink_0 nvstreammux name=m batch-size=1 width=640 height=480 ! \
    nvinfer config-file-path=/home/relics9/vtx/test/ds_infer_primary.txt ! \
    nvdsosd ! \
    nvvideoconvert ! 'video/x-raw(memory:NVMM),format=RGBA' ! \
    nv3dsink sync=false
