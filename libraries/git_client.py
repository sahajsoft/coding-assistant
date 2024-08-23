import git
import os

def clone_repo(repo_url):
    """
    Clones a Git repository from the given repository URL.
    Args:
        repo_url (str): The URL of the Git repository to clone.
    Returns:
        git.Repo: The cloned Git repository object.
    Example:
        ```python
        repo_url = "https://github.com/example/repo.git"
        repo = clone_repo(repo_url)
        ```
    """
    repo_name = repo_url.split('/')[-1]
    expanded_path = os.path.expanduser('~/' + repo_name)
    if not os.path.exists(expanded_path):
        repo = git.Repo.clone_from(repo_url, expanded_path)
    else:
        repo = git.Repo(expanded_path) 
    return repo

def get_commits(repo: git.Repo, branch: str = 'master'):
    """
    Retrieves a list of commits from a Git repository, including their messages, affected files, and SHA hashes.

    Args:
        repo (git.Repo): The Git repository object to retrieve commits from.
        branch (str, optional): The branch to retrieve commits from. Defaults to 'master'.

    Returns:
        list: A list of dictionaries, each containing information about a commit, including its message, affected files, and SHA hash.
    """
    commits = list(repo.iter_commits(branch))
    commits_with_affected_files = [{'message': commit.message, 'files': commit.stats.files, 'sha': commit.hexsha} for commit in commits]
    return commits_with_affected_files