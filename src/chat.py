import tempfile
from aider.models import Model
from aider.io import InputOutput
from aider.repo import GitRepo
from aider.coders import AskCoder


class Chat:
    def __init__(self, repo_path: str, model_name="ollama/llama3.1:8b") -> None:
        self.chat_history_file = tempfile.NamedTemporaryFile()
        self.io = InputOutput(chat_history_file=self.chat_history_file.name)
        self.repo = GitRepo(io=self.io, fnames=None, git_dname=repo_path)
        self.model = Model(model_name)
        self.coder = AskCoder(main_model=self.model, io=self.io, repo=self.repo)

    def chat(self):
        while True:
            self.coder.run()


# chat_repo = Chat("/Users/akshaykarle/src/github.com/sahajsoft/pii-detection-and-anonymizer")
# chat_repo.chat()
