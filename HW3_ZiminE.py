class ColorizeMixin:
    """Provides common code for colour representation"""

    def __repr__(self):
        """
        :return: Changes formatting of the main text
        """
        return f'\033[1;{Advert.repr_color_code};40m'


class Advert(ColorizeMixin):
    """Creates dynamically the attributes of class from a dictionary"""
    repr_color_code = 33

    def __init__(self, sent: dict):

        for k, v in sent.items():
            if isinstance(v, dict):
                v = Advert(v)
            self.__dict__[k] = v

        if 'price' not in self.__dict__:
            self.price = 0
        elif self.__dict__['price'] < 0:
            raise ValueError('must be >= 0')

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('must be >= 0')
        elif key == 'price':
            self.__dict__['price'] = value

    @property
    def class_(self):
        """Provide property for 'class'"""
        return self.__dict__['class']

    def __repr__(self):
        return f'{super().__repr__()} {self.title} | {self.price} ₽'


if __name__ == '__main__':
    import json

    # Test 1
    lesson_str = """{
    "title": "python", "price": 1,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""

    lesson_ad = Advert(json.loads(lesson_str))
    print(lesson_ad.title)
    print(lesson_ad.location.address)  # город Москва, Лесная, 7
    print(lesson_ad.price)  # 1
    # lesson_ad.price = -1               # ValueError: must be >= 0

    # Task 2
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"    }    }"""
    corgi_dict = json.loads(corgi_str)
    corgi = Advert(corgi_dict)
    print(corgi.class_)  # dogs
    print(corgi)  # Вельш-корги | 1000 ₽ (желтым цветом)
