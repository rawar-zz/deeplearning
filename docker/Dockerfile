FROM ubuntu:16.04
MAINTAINER ramon@wartala.de

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libfreetype6-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libpng12-dev \
        libzmq3-dev \
        libprotobuf-dev \
        libsnappy-dev \
        pkg-config \
        protobuf-compiler \
        rsync \
        software-properties-common \
        unzip \
        vim \
        zlib1g-dev \
        python-pydot \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

#RUN pip --no-cache-dir install \
#		pyopenssl \
#		ndg-httpsclient \
#		pyasn1

# Install useful Python packages using apt-get to avoid version incompatibilities with Tensorflow binary
# especially numpy, scipy, skimage and sklearn (see https://github.com/tensorflow/tensorflow/issues/2034)
RUN apt-get update && apt-get install -y \
		python-numpy \
		python-scipy \
		python-nose \
		python-h5py \
		python-skimage \
		python-matplotlib \
		python-pandas \
		python-sklearn \
		python-sympy \
    python-skimage \
    python-progressbar \
		&& \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

# Install other useful Python packages using pip
RUN pip --no-cache-dir install --upgrade ipython && \
	pip --no-cache-dir install \
		Cython \
		ipykernel \
		jupyter \
		path.py \
		Pillow \
		pygments \
		six \
		sphinx \
		wheel \
		zmq \
    protobuf \
		&& \
	python -m ipykernel.kernelspec


# Install Caffe
#RUN echo "Install Caffe..."
#ENV CAFFE_ROOT=/opt/caffe
#WORKDIR $CAFFE_ROOT

# FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub supports this.
#ENV CLONE_TAG=master
#RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/BVLC/caffe.git . && \
#    for req in $(cat python/requirements.txt) pydot; do pip install $req; done && \
#    mkdir build && cd build && \
#    cmake -DCPU_ONLY=1 .. && \
#    make -j"$(nproc)"

# Install Caffe2
RUN echo "Install Caffe2..."

ENV CAFFE_ROOT=/opt/caffe2
ENV CAFFE_INSTALL=/opt
WORKDIR $CAFFE_INSTALL

RUN git clone --recursive https://github.com/caffe2/caffe2.git && \
  cd caffe2 && \
  make && \
  cd build && \
  make install 

ENV PYCAFFE_ROOT $CAFFE_ROOT/build
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $PYCAFFE_ROOT:$PATH
ENV LD_LIBRARY_PATH=$PYCAFFE_ROOT/caffe2:$LD_LIBRARY_PATH

# export PYTHONPATH=/opt/caffe2/build
# export LD_LIBRARY_PATH=/opt/caffe2/build/caffe2:$LD_LIBRARY_PATH
#RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

# Install TensorFlow
RUN echo "Install TensorFlow related stuff..."

ARG TENSORFLOW_VERSION=1.1.0
ARG TENSORFLOW_ARCH=cpu

# Install TensorFlow
RUN pip --no-cache-dir install \
	https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_ARCH}/tensorflow-${TENSORFLOW_VERSION}-cp27-none-linux_x86_64.whl


# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Copy sample notebooks.
COPY notebooks /notebooks

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /root/

# TensorBoard port
EXPOSE 6006

# Jupyter port
EXPOSE 8888

#WORKDIR "/notebooks"

WORKDIR "/root"
CMD ["/bin/bash"]
