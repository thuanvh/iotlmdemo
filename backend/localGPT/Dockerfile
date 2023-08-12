# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM ubuntu:22.04 AS builder

WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip build-essential libopenblas-dev

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

RUN apt-get install python-is-python3

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

FROM builder as deploy
COPY . /app

ENTRYPOINT ["python3"]
CMD ["run_localGPT_API.py"]

# FROM builder as dev-envs

# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /