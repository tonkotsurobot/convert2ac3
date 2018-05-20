FROM jrottenberg/ffmpeg
MAINTAINER Edward Mario (edward.mario@gmail.com)
RUN apt-get install -y python
RUN mkdir /media/convert /media/done
COPY convert.py /tmp/workdir/
ENTRYPOINT ["python","convert.py"]
CMD ["/media/convert/", "/media/done/"]
