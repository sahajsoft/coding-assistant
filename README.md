# coding-assistant

## Prerequisites

Run `./setup.sh` to install all dependencies. This will install [direnv](https://github.com/direnv/direnv/blob/master/docs/installation.md) and [nix](https://nixos.org/download.html) then simply run `direnv allow` to install all build dependencies.

Alternatively, make sure you have [python 3.11](https://www.python.org/downloads/), [poetry](https://python-poetry.org/docs/#installation) and [ollama](https://ollama.com/download) setup on your machine.

## Getting started

To get started, run the following:

```
poetry install --no-root
ollama serve &
ollama pull llama3.1:8b
poetry run python src/main.py -h
poetry run python src/cli.py --help # show the usage of the cli
poetry run python src/cli.py --repo-path . repomap # print out current repo map
poetry run python src/cli.py --repo-path . summary # summarise current repo
```

## Contributing

The recommendation would be to familiarise yourself with the structure of the repo and if you are working on a new feature create a separate module for it and integrate in to the `cli.py` at the least so it is usable. Also make sure any relevant tests get added to the `tests` folder. To run all tests simply run `poetry run pytest`.

## Troubleshooting

There is a chance that `direnv allow` will not load the environment correctly and silently fail. This is observable when you attempt to run `poetry install`, as you will get a `command not found` error in the shell.
To fix this, you need to run the nix commands directly. Run the following:

```
nix --extra-experimental-features 'nix-command flakes' develop
```
This command will create a new Shell instance which has the Nix dependencies loaded. You will need to run commands through this prompt.

## Useful Links

https://mistral.ai/news/codestral-mamba/ Codestral mamba
https://docs.sweep.dev/blogs/chunking-2m-files Ollama CodeSplitter
https://www.codium.ai/blog/rag-for-large-scale-code-repos/ RAG for large-scale code-repos
