def unlist(nested_list):
    """
    Flattens a list of any level of nesting.
    
    Args:
        nested_list (list): A list that may contain nested lists.
        
    Returns:
        list: A flattened list containing all non-list elements.
    """
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
        
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(unlist(item))
        else:
            flat_list.append(item)
    return flat_list
