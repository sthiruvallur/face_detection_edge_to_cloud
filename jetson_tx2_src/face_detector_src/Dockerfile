FROM nvcr.io/nvidia/l4t-base:r32.3.1

#RUN apt-get install dialog apt-utils -y

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libavcodec-dev \
#     libavformat-dev \
#     libavutil-dev \
#     #libeigen3-dev \
#     #libglew-dev \
#     #libtiff5-dev \
#     libjpeg-dev \
#     libpng-dev \
#     #libpostproc-dev \
#     #libswscale-dev \
#     libtbb-dev \
#     #libgtk2.0-dev \
#     #libxvidcore-dev \
#     #libx264-dev \
#     #pkg-config \
#     #zlib1g-dev \
#     && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    #python-dev \
    python-numpy \
    #python-py \
    #python-pytest \
    python-opencv \
    python-opencv-apps \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    #python3-dev \
    python3-numpy \
    #python3-py \
    #python3-pytest \
    python3-opencv \
    #libopencv-python \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# GStreamer support
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
