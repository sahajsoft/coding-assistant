# coding-assistant

## Prerequisites

Run `./setup.sh` to install all dependencies. This will install [direnv](https://github.com/direnv/direnv/blob/master/docs/installation.md) and [nix](https://nixos.org/download.html) then simply run `direnv allow` to install all build dependencies.

Alternatively, make sure you have [python 3.11](https://www.python.org/downloads/) and [poetry](https://python-poetry.org/docs/#installation) setup on your machine.

## Getting started

To get started, run the following:

```
poetry install --no-root
docker run -d -p 8080:8080 -p 50051:50051 cr.weaviate.io/semitechnologies/weaviate
poetry run jupyter notebook
```

## Troubleshooting

There is a chance that `direnv allow` will not load the environment correctly and silently fail. This is observable when you attempt to run `poetry install`, as you will get a `command not found` error in the shell.
To fix this, you need to run the nix commands directly. Run the following:

```
nix --extra-experimental-features 'nix-command flakes' develop
```
This command will create a new Shell instance which has the Nix dependencies loaded. You will need to run commands through this prompt.
