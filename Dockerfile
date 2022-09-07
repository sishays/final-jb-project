# Multistage build for the ec2 checker #
# Build, lint & serve #


# Build stage #
FROM python:3.8-slim as builder
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
# Building the app
RUN pip wheel -r requirements.txt \
    && mkdir for-lint \
    && cp *.py pylint.cfg for-lint


# Lint tests stage #
FROM eeacms/pylint:latest as linter
WORKDIR /code
COPY --from=builder /app/for-lint ./
RUN cp pylint.cfg /etc/pylint.cfg
RUN ["/docker-entrypoint.sh", "pylint"]


# Serve #
FROM python:3.8-slim as runtime
ARG USER=ishays
RUN useradd -ms /bin/bash ${USER}
USER ${USER}
WORKDIR /home/${USER}
COPY config credentials ./
#RUN mkdir /home/${USER}/.aws && \
#    mv config /home/${USER}/.aws && \
#    mv credentials /home/${USER}/.aws
COPY --from=builder /app .
#RUN pip install -r requirements.txt \
#    -f /app \
#    && rm -rf *.whl \
#    && rm -rf /root/.cache/pip/*
RUN mkdir /home/${USER}/.aws && \
    mv config /home/${USER}/.aws && \
    mv credentials /home/${USER}/.aws && \
    pip install -r requirements.txt 

CMD ["python3", "ec2checker.py"]
