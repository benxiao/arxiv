
def smart_copy(_object):
    """
    recursively copy the built-in containers but no the underlying user objects
    :param _object:
    :return:
    """

    if not isinstance(_object, (list, dict, set, tuple)):
        return _object

    if isinstance(_object, list):
        return [smart_copy(x) for x in _object]

    if isinstance(_object, set):
        return {smart_copy(x) for x in _object}

    if isinstance(_object, tuple):
        return tuple(smart_copy(x) for x in _object)

    if isinstance(_object, dict):
        return {x: smart_copy(_object[x]) for x in _object}


if __name__ == '__main__':
    a = [[1,2,3], {():[], 2:[1,2]}, {1,2,3}, (1,2,3)]
    b = smart_copy(a)
    print(b)