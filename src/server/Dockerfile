FROM python:alpine


WORKDIR /webServer
COPY webserver.py .

# Install Flask
RUN pip install flask

# Install requests
RUN pip install requests

# Copy templates folder
COPY templates templates/

# Run Flask
ENV FLASK_APP=webserver.py

# "--host 0.0.0.0" so that the server listens on all interfaces and not only lo
CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5001"] 

