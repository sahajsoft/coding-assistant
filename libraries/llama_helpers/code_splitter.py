from llama_index.core.node_parser import CodeSplitter
from tree_sitter_languages import get_language, get_parser


def get_language_variable_code_splitters(languages: dict):
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

def apply_code_splitters(language_code_splitters_map: dict, language_file_map: dict) -> list[str]:
    """
    Applies the specified code splitters to the supplied dictionary mapping of programming
    language -> file contents.

    Parameters
    ----------
    language_code_splitters_map: dict
        A dictionary of key (programming language) and value (code splitter). Typically obtained through 
        code_splitter.get_language_variable_code_splitters\

    language_file_map:
        A mapping of programming language to filepaths and their content, with the following schema:
        ```
        {
          "$schema": "http://json-schema.org/draft-04/schema#",
          "type": "object",
          "properties": {
            "<programming_language>": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "<filepath_string>": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
        ```
        
    Returns
    -------
    list[str]
        A list of split file contents using the code splitters
    """
    # Trim language_file_map to only include the files for the languages specified
    # in language_code_splitters
    trimmed_language_map = {key: val for key, val in language_file_map.items() if key in language_code_splitters_map.keys()}
    print(f"Will create nodes for the following languages: {trimmed_language_map.keys()}")
    
    # Get nodes
    nodes = []
    for language in trimmed_language_map.keys():
        node_parser = language_code_splitters_map[language]
        contents = trimmed_language_map[language]
        print(f"Getting nodes for {language}: {len(contents.keys())} files")
        split_nodes = [node_parser.split_text(val) for val in contents.values()]
        [nodes.extend(i) for i in split_nodes]

    return nodes