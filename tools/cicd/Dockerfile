# This Docker image is a modified version of the python image including
# a few necessary packages for building and publishing this library.
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

# Pick up the latest OS trust store (emSign/eMudhra CA removal,
# GHSA-6q48-6c7w-9gw2).
RUN apt-get update \
    && apt-get install -y --only-upgrade ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade "pip>=26.2.2" "certifi>=2026.10.19" build==1.3.0 twine==6.2.0

ENTRYPOINT ["python3"]