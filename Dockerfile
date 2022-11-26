FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --assume-yes install -y \
    build-essential \
    maven \
    openjdk-17-jdk \
    python3-dev \
    python3-pip

ENV JDK_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PIP_NO_BINARY=jpy

RUN pip3 install -U Jinja2
RUN pip3 install ansible ansible-rulebook ansible-runner wheel aiohttp

RUN mkdir /ansible-rules
ADD ansible-rules/ /ansible-rules

RUN ansible-galaxy collection install -r /ansible-rules/collections/requirements.yml -p /ansible-rules/collections

WORKDIR /ansible-rules
CMD ansible-rulebook --rulebook rules/sample.yml -i inventory  --verbose
