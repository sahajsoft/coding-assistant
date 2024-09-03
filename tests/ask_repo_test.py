import pytest
import os

from ask_repo import AskRepo


class TestAskRepo:
    @pytest.fixture
    def model_name(self):
        if os.getenv("TEST_USE_OPENAI"):
            return "gpt-3.5-turbo"
        else:
            return "ollama/llama3.1:8b"


    def test_invalid_repo_path(self):
        with pytest.raises(FileNotFoundError):
            AskRepo("/non_existent_path")


    def test_repo_map(self):
        ask_repo = AskRepo(os.getcwd())
        assert "pyproject.toml" in ask_repo.get_repo_map()


    def test_generates_valid_summary(self, model_name):
        ask_repo = AskRepo(os.getcwd(), model_name)
        assert "summary" in ask_repo.summarise()
