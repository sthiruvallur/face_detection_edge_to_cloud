FROM python:3.7-alpine
  
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# install ca-certificates so that HTTPS works consistently
# other runtime dependencies for Python are installed later
RUN apk update && apk add --no-cache ca-certificates

#ENV PYTHON_VERSION 3.7.6

RUN apk add --no-cache mosquitto

CMD ["mosquitto"]
