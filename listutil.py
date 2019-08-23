def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    """
    # Another solution but didn't work with dict.
    # _________
    # if not isinstance(list, type([])):
    #     raise TypeError
    # list_to_set = set([tuple(element) if isinstance(element, type([])) else element for element in list])
    # set_to_tuple = [[*element] if type(element) == tuple
    #                 else element for element in list_to_set]
    # return set_to_tuple

    if not isinstance(list, type([])):
        raise TypeError('Input argument type must be list.')
    list_with_out_duplicate = []
    for item in list:
        if item not in list_with_out_duplicate:
            list_with_out_duplicate.append(item)
    return list_with_out_duplicate


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
