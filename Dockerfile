FROM ubuntu:20.04
WORKDIR /app
RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until \
    && apt-get update \
    && apt-get install -y wget \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt install -y python3.6 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install google-chrome-stable -y

RUN apt-get install -y wget xvfb unzip \
    && mkdir driver \ 
    && apt-get update \
    && wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip \
    && unzip chromedriver_linux64 -d /app/driver \
    && apt-get -y install python3-pip \
    && python3.6 -m pip install pandas \
    && python3.6 -m pip install selenium
COPY main_crawling.py ./

CMD ["python3.6", "main_crawling.py"]
