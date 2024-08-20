def get_formatted_dict_key_counts(value: dict):
    """
    Utility function for returning a formatted string counting the number of elements
    in a dictionary for each key
    
    Parameters
    ----------
    value : dict
        The dictionary whose count to return.
        
    Returns
    -------
    str
        A formatted string with a count of the number of elements per key in the dictionary.
    """
    return "".join([f"\n{key}: {len(value[key])}" for key in value.keys()])