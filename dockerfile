FROM public.ecr.aws/lambda/python:latest
COPY requirement.txt ./
RUN pip3 install -r requirement.txt
COPY app.py ./
CMD [ "app.handler" ]