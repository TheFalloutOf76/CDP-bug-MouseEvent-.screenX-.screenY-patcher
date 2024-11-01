FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget xvfb

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "DrissionPage_example_docker.py"]