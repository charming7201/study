def dedupe(items, key=None):
    '''
    This function can dedupe the duplicate item and keep the subsequence
    Even the vale is unhashable
    :param items: The items include the duplicate item
    :param key: The duplicate value
    :return: Return a iterator
    '''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def dedupe2(items):
    '''
    This function can remove the duplicate item and keep the subsequence
    But the value must be hashable
    :param items:
    :return: Return a iterator
    '''
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


li = ['y', 'x', 'a', 'a', 0, 0]

print(list(dedupe2(li)))

dicli = [
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 1},
    {'x': 1, 'y': 2},
]

print(list(dedupe(dicli, key=lambda x: (x['x'], x['y']))))
