from pygments.lexers import guess_lexer_for_filename

def get_file_language(filename: str, content: str) -> str:
    """
    Attempts to parse the content and file extension
    of a script file to determine the programming languages it contains.
    Note: it uses the filename extension to help it better interpret the language
    ie Python vs Mojo
    
    Parameters
    ----------
    filename : str
        The filename string.
    content : str
        The content of the file.
        
    Returns
    -------
    str
        The programming language name
    
    Raises
    ------
    pygments.util.ClassNotFound
        Raised if a language cannot be determined.
    """
    lexer = guess_lexer_for_filename(filename, content)
    return lexer.name
