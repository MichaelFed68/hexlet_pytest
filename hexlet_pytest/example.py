def reverse(string):
    '''

    >>> reverse('')
    ''

    >>> reverse('Misha')
    'ahsiM'
    '''

    return string[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
