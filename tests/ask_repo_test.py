import pytest
import os

from ask_repo import AskRepo


def test_invalid_repo_path():
    with pytest.raises(FileNotFoundError):
        AskRepo("/non_existent_path")


def test_repo_map():
    ask_repo = AskRepo(os.getcwd())
    assert "pyproject.toml" in ask_repo.get_repo_map()


def test_generates_valid_summary():
    ask_repo = AskRepo(os.getcwd(), "gpt-3.5-turbo")
    assert "Purpose" in ask_repo.summarise()
