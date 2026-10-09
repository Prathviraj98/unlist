def unlist(nested_iterable, recursive=True):
    """
    Flattens a list or iterable, similar to R's unlist() function.
    
    Args:
        nested_iterable (iterable): A list, tuple, or set that may contain nested elements.
        recursive (bool): If True, unlists all levels of nesting recursively. 
                          If False, only flattens one level. Defaults to True.
        
    Returns:
        list: A flattened list containing the elements.
    """
    flat_list = []
    
    # Check if the input is iterable (excluding strings/bytes which we don't want to split)
    if not hasattr(nested_iterable, '__iter__') or isinstance(nested_iterable, (str, bytes)):
        raise TypeError("Input must be an iterable (e.g., list, tuple, set)")
        
    for item in nested_iterable:
        if isinstance(item, (list, tuple, set)):
            if recursive:
                flat_list.extend(unlist(item, recursive=True))
            else:
                flat_list.extend(list(item))
        else:
            flat_list.append(item)
            
    return flat_list
