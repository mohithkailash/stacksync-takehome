FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    build-essential \
    autoconf \
    bison \
    flex \
    libprotobuf-dev \
    libnl-route-3-dev \
    libtool \
    pkg-config \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

# Build and install nsjail
RUN git clone https://github.com/google/nsjail.git \
    && cd nsjail \
    && make \
    && mv nsjail /usr/bin/ \
    && cd .. \
    && rm -rf nsjail

RUN pip3 install Flask==3.0.3 Werkzeug==3.0.3

WORKDIR /app


RUN mkdir /app/tmp && chmod 777 /app/tmp

COPY *.py .
COPY nsjail.cfg .

# RUN useradd -m myuser
# RUN chown -R myuser:myuser /app && \
#     chmod 755 /app && \
#     chmod 644 /app/* && \
#     chmod +x /usr/bin/nsjail

# Ensure Python is in a known location
RUN ln -s /usr/bin/python3 /usr/local/bin/python3

EXPOSE 8080

ENV PORT 8080

CMD ["python3", "app.py"]
