from aider.models import Model
from aider.io import InputOutput
from aider.repo import GitRepo
from aider.coders import AskCoder


class AskRepo:
    summary_prompt = "Summarise the purpose and structure of this project. Also list out the most important modules, classes, functions used and their purpose. If any examples, tests and documentation is supplied also summarise that."

    def __init__(self, repo_path: str, model_name="ollama/llama3.1:8b") -> None:
        self.io = InputOutput()
        self.repo = GitRepo(io=self.io, fnames=None, git_dname=repo_path)
        self.model = Model(model_name)
        self.coder = AskCoder(main_model=self.model, io=self.io, repo=self.repo)

    def get_repo_map(self) -> str:
        return self.coder.get_repo_map()

    def summarise(self) -> str:
        summary = self.coder.run(self.summary_prompt)
        return summary

    def chat(self):
        while True:
            self.coder.run()

# ask_repo = AskRepo("/home/akshaykarle/src/github.com/sahajsoft/pii-detection-and-anonymizer")
# print(ask_repo.get_repo_map())
# print(ask_repo.summarise())
