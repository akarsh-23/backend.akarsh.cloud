FROM public.ecr.aws/lambda/python:latest
COPY . ./
RUN pip3 install -r requirement.txt
CMD [ "app.handler" ]