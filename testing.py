# task 1
import unittest


class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


def test_pokemon():
    assert str(Pokemon(name='Bulbasaur', poketype='grass')) == r'Bulbasaur/grass'
    assert str(Pokemon(name='Pikachu', poketype='electric\r\npower')) == f'Pikachu/electric\r\npower'
    assert str(Pokemon(name='Squirtle', poketype='water' * 30)) == f'Squirtle/{"water" * 30}'
    # print(Pokemon(name='Pikachu', poketype='electric\r\npower'))


# task 2
# def test_pokemon_v2():
#     """
#     Concatenation of two strings.
#
#     >>> str(Pokemon(name='Bulbasaur', poketype='grass'))
#     r'Bulbasaur/grass'
#     >>> str(Pokemon(name='Bulbasaur', poketype='grass'))
#     f'Pikachu/electric\r\npower'
#     >>> str(Pokemon(name='Bulbasaur', poketype='grass'))
#     f'Squirtle/{"water" * 30}'
#     """
#     # print(Pokemon(name='Pikachu', poketype='electric\r\npower'))
# task 3
#
# class TestPokemon(unittest.TestCase):
#     def test_pokemon_1(self):
#         actual = str(Pokemon(name='Bulbasaur', poketype='grass'))
#         expected = r'Bulbasaur/grass'
#         self.assertEqual(actual, expected)
#
#     def test_pokemon_2(self):
#         actual = str(Pokemon(name='Pikachu', poketype='electric\r\npower'))
#         expected = f'Pikachu/electric\r\npower'
#         self.assertEqual(actual, expected)
#
#     def test_pokemon_3(self):
#         actual = str(Pokemon(name='Squirtle', poketype='water' * 30))
#         expected = f'Squirtle/{"water" * 30}'
#         self.assertEqual(actual, expected)
#

# TestPokemon.test_pokemon_1()
# TestPokemon.test_pokemon_2()
# TestPokemon.test_pokemon_3()
if __name__ == '__main__':
    pytest.main()
    test_pokemon()
    print(Pokemon(name='Pikachu', poketype='electric\r\npower'))
# test_pokemon_v2()
# print(0.3 + 0.3 + 0.3 + 0.1)
# for method in dir(unittest.TestCase):
#     if method.startswith('assert'):
#         print(method)
