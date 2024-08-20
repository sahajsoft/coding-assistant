import os
from .language import get_file_language
from .helpers import get_formatted_dict_key_counts
from pygments.util import ClassNotFound
import chardet
import pathspec
import sys
from collections import defaultdict

def read_file_contents(file_path: str, verbose: bool = False) -> tuple[str, str] | None:
    """
    Reads the contents of the filepath and returns the raw data along with
    the detected programming language in the file. 
    
    Parameters
    ----------
    file_path : str
        The file_path string.
    verbose: bool
        Toggle verbose printout (default False)
        
    Returns
    -------
    tuple(str, str) | None
        The programming language name and the data, or None if a language
        is not found, or the encoding of the file cannot be determined.
    """
    with open(file_path, 'rb') as f:
        raw_data = f.read()

        try:
            language = get_file_language(file_path, raw_data)
        except ClassNotFound:
            if(verbose):
                print(f"Could not parse {file_path} as a programming language")
            return None

        # Decode
        try:
            encoding = chardet.detect(raw_data)["encoding"]
            data = raw_data.decode(encoding)
        except (UnicodeDecodeError, TypeError):
            if(verbose):
                print(f"Could not detect encoding for {file_path}")
            return None

        return language, data

def get_number_of_files_recursive(root_path: str,
            ignoreFileExt: list = [],
            ignoreDir: list = [".git"]) -> int:
    """
    Returns the number of files in a directory recursively.

    Parameters
    ----------
    root_path: str
        The root file path string.
    ignoreFileExt: list[str]
        The file extensions to ignore when counting
    ignoreDir: list[str]
        The directories to ignore (default [".git"])
        
    Returns
    -------
    int
        The total number of files
    """
    total_files = 0
    
    gitignore_path = os.path.join(root_path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_patterns = f.read().splitlines()
        spec = pathspec.PathSpec.from_lines('gitwildmatch', gitignore_patterns)
    else:
        spec = None

    for root, dirs, files in os.walk(root_path):
        dirs[:] = [i for i in dirs if i not in ignoreDir]

        trimmed_files = []
        for fi in files:
            _, ext = os.path.splitext(fi)
            file_path = os.path.join(root, fi)
            if spec and spec.match_file(file_path):
                continue
    
            if(ext in ignoreFileExt):
                continue
            trimmed_files.append(fi)
        total_files += len(trimmed_files)

    return total_files

def scan_dir(root_path: str,
            verbose: bool = False,
            ignoreFileExt: list = [],
            ignoreDir: list = [".git"]) -> dict:
    """
    Recursively scans the filepath and returns a dictionary of valid file contents
    with an identifiable programming language in the form:

    {
        "<programming_language>": {
            "<filepath>": <contents>
        }
    }
    
    Parameters
    ----------
    root_path: str
        The root file path string.
    verbose: bool
        Toggle verbose printout (default False)
    ignoreFileExt: list[str]
        The file extensions to ignore when counting
    ignoreDir: list[str]
        The directories to ignore (default [".git"])
        
    Returns
    -------
    dict
        A dictionary of file contents by programming language
    """
    language_map = {}

    _prev_line_size = 0

    # Read .gitignore and compile patterns
    gitignore_path = os.path.join(root_path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_patterns = f.read().splitlines()
        spec = pathspec.PathSpec.from_lines('gitwildmatch', gitignore_patterns)
    else:
        spec = None
    if(verbose):
        total_files = get_number_of_files_recursive(root_path, ignoreFileExt, ignoreDir)
        progress = 0

    ignored_files = []
    ignored_files_ext = defaultdict(lambda: [])
    
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [i for i in dirs if i not in ignoreDir]
        for file_name in files:
            _, ext = os.path.splitext(file_name)
            file_path = os.path.join(root, file_name)

            if spec and spec.match_file(file_path):
                ignored_files.append(file_path)
                ignored_files_ext[ext].append(file_path)
                continue

            if(ext in ignoreFileExt):
                ignored_files.append(file_path)
                ignored_files_ext[ext].append(file_path)
                continue

            if(verbose):
                print(" " * _prev_line_size, end="\r")
                message = f"Progress: {progress+1}/{total_files} | Scanning: {file_path}"
                _prev_line_size = len(message)
                print(message, end="\r", flush=True)
                sys.stdout.flush()
            result = read_file_contents(file_path, False)
            if(result):
                language, contents = result
                if(language in language_map):
                    language_map[language][file_path] = contents
                else:
                    language_map[language] = {file_path: contents}
            else:
                ignored_files.append(file_path)
                ignored_files_ext[ext].append(file_path)
            if(verbose):
                progress += 1
    if(verbose):
        print(f"\nThe following number of files with the specified file extensions were ignored: {get_formatted_dict_key_counts(ignored_files_ext)}")
    return language_map