from llama_index.core.node_parser import CodeSplitter
from tree_sitter_languages import get_language, get_parser


def get_language_variable_code_splitters(languages: list):
    """
    Returns language-specific code-splitters for a provided list of programming languages.
    Prints errors if no language-specific parser is available for a given language.

    Parameters
    ----------
    languages: list[str]
        The list of programming languages
        
    Returns
    -------
    dict
        A dictionary of code splitters by programming langauge
    """
    node_parsers = {}
    for language in languages:
        try:
            node_parsers[language] = CodeSplitter(language=language.lower(), chunk_lines = 100, chunk_lines_overlap = 15, max_chars = 1500)
        except Exception as e:
            pass
    return node_parsers