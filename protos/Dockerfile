FROM debian:jessie-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PROTOBUF_VERSION=3.2.0
ARG BUILDTIME_DEPENDENCIES="autoconf automake build-essential ca-certificates curl g++ libtool make unzip wget"

ENV SHARED_VOLUME="/tmp/build"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILDTIME_DEPENDENCIES} && \
	rm -rf /var/lib/apt/lists/*

RUN mkdir ${SHARED_VOLUME} /tmp/.build

RUN wget --no-check-certificate --output-document - https://github.com/google/protobuf/archive/v${PROTOBUF_VERSION}.tar.gz | tar -xz --directory /tmp/.build

WORKDIR /tmp/.build/protobuf-${PROTOBUF_VERSION}

RUN ./autogen.sh
RUN ./configure --prefix /usr/local/ && \
    make && \
    make check && \
    make install

WORKDIR ${SHARED_VOLUME}

RUN rm -r /tmp/.build/protobuf-${PROTOBUF_VERSION}
RUN apt-get purge -y --auto-remove ${BUILDTIME_DEPENDENCIES}

VOLUME ${SHARED_VOLUME}

ENTRYPOINT ["/usr/local/bin/protoc"]
