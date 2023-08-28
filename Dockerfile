FROM python:3.10-slim
RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

EXPOSE 5000
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . ./
CMD python3 vulcan_middleware.py