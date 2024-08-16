import argparse

from ask_repo import AskRepo


def generate_summary(args):
    ask_repo = AskRepo(args.repo_path, args.model_name)
    print(ask_repo.summarise())


def generate_repo_map(args):
    ask_repo = AskRepo(args.repo_path, args.model_name)
    print(ask_repo.get_repo_map())


def main():
    parser = argparse.ArgumentParser(description="A CLI for interacting with the coding assistant.")
    parser.add_argument("--repo-path", required=True, type=str, metavar="FILE")
    parser.add_argument("--model-name", required=False, type=str, default="ollama/llama3.1:8b")
    subparsers = parser.add_subparsers(required=True)

    summary_parser = subparsers.add_parser("summary", description="Generate summary of a local git repository.")
    summary_parser.set_defaults(func=generate_summary)

    summary_parser = subparsers.add_parser("repomap", description="Generate summary of a local git repository.")
    summary_parser.set_defaults(func=generate_repo_map)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
