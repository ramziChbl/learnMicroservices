FROM python:alpine

#RUN mkdir /dbApp
WORKDIR /dbApp
COPY app.py .
COPY data data/

# Install Flask
RUN pip install flask

# Run Flask
ENV FLASK_APP=app.py

# "--host 0.0.0.0" so that the server listens on all interfaces and not only lo
CMD ["flask", "run", "--host", "0.0.0.0"] 

