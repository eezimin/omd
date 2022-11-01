from one_hot_encoder import fit_transform


def test_cities():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_samewords():
    assert fit_transform(['Moscow', 'Moscow']) == [('Moscow', [1]), ('Moscow', [1])]


def test_tuple_integers():
    assert fit_transform((1, 0, 0, 1)) == [(1, [0, 1]), (0, [1, 0]), (0, [1, 0]), (1, [0, 1])]


def test_range():
    assert fit_transform(range(3)) == [(0, [0, 0, 1]), (1, [0, 1, 0]), (2, [1, 0, 0])]


def test_one_string():
    assert fit_transform('ars') == [('ars', [1])]


def test_empty_string():
    try:
        assert fit_transform() == ''
    except (AssertionError, TypeError):
        pass
    else:
        print('Test failed!')