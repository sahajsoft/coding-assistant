import argparse

from ask_repo import AskRepo
from chat import Chat


def generate_summary(args):
    ask_repo = AskRepo(args.repo_path, args.model_name)
    print(ask_repo.summarise())


def generate_repo_map(args):
    ask_repo = AskRepo(args.repo_path, args.model_name)
    print(ask_repo.get_repo_map())


def start_chat(args):
    chat_repo = Chat(args.repo_path, args.model_name)
    chat_repo.chat()


def main():
    parser = argparse.ArgumentParser(description="A CLI for interacting with the coding assistant.")
    parser.add_argument("--repo-path", required=True, type=str, metavar="FILE")
    parser.add_argument("--model-name", required=False, type=str, default="ollama/llama3.1:8b")
    subparsers = parser.add_subparsers(required=True)

    summary_parser = subparsers.add_parser("summary", description="Generate summary of a local git repository.")
    summary_parser.set_defaults(func=generate_summary)

    summary_parser = subparsers.add_parser("repomap", description="Generate summary of a local git repository.")
    summary_parser.set_defaults(func=generate_repo_map)

    chat_parser = subparsers.add_parser("chat", description="Start a Chat with the assistant to help with local git repository.")
    chat_parser.set_defaults(func=start_chat)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
