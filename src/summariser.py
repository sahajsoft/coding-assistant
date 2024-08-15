from aider.models import Model
from aider.io import InputOutput
from aider.repo import GitRepo
from aider.coders import AskCoder


class Summariser:
    summary_prompt = "Summarise the purpose and structure of this project. Also list out the most important modules, classes, functions used and their purpose. If any examples, tests and documentation is supplied also summarise that."

    def __init__(self, repo_path: str, model_name="ollama/llama3.1:8b") -> None:
        self.io = InputOutput()
        self.repo = GitRepo(io=self.io, fnames=None, git_dname=repo_path)
        self.model = Model(model_name)

    def summary(self) -> str:
        coder = AskCoder(main_model=self.model, io=self.io, repo=self.repo)
        summary = coder.run(self.summary_prompt)
        return summary

# summary = Summariser("/home/akshaykarle/src/github.com/sahajsoft/pii-detection-and-anonymizer").summary()
